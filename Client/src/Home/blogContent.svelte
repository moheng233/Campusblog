<script lang="ts">
    import m from "materialize-css";

    import { User as UserStore } from "../store";

    import { ClientApi } from "../tool/api";
    import type { IBlog, IUser } from "../tool/api";

    import { getContext, onMount, setContext } from "svelte";

    import Vditor from "vditor";

    import dayjs from "dayjs";
    import "dayjs/locale/zh-cn";
    import relativeTime from 'dayjs/plugin/relativeTime';

    dayjs.extend(relativeTime);

    import InputField from "../Components/InputField/InputField.svelte";
    import Button from "../Components/Button/Button.svelte";
    import { fade, fly, slide } from "svelte/transition";
    import { link, replace,location } from "svelte-spa-router/Router.svelte";

    import { memoize } from "lodash";

    import reportModal from "./reportModal.svelte";

    export let params: { id: number };

    let floatingbtn: boolean = false;
    let editType: "edit" | "report" = "edit";

    let BlogGet = memoize(async () => {
        return ClientApi.object.BlogGet(params.id).then((r) => {
            let user = $UserStore;
            if (user.id == r.user.id) {
                editType = "edit";
            } else {
                editType = "report";
            }
            return r;
        });
    });

    let preview = (node: HTMLDivElement, blog: IBlog) => {
        Vditor.preview(node, blog.content);
    };

    let PostContent: string = "";

    const { open } = getContext("simple-modal");

    async function PostCreate() {
        ClientApi.object
            .BlogPost((await BlogGet()).id, PostContent)
            .then((r) => {
                m.toast({
                    html: "回复成功",
                });
                // promise = ClientApi.object.BlogGet(params.id);
                BlogGet.cache = new memoize.Cache;
                replace($location);
                PostContent = "";
            });
    }
</script>

<!-- svelte-ignore component-name-lowercase -->
<style lang="scss" global>
    // @import "../styles/github-markdown.scss";

    .author {
        margin: 20px 0 0 0;
        font-weight: 600;
        font-size: 1rem;
    }
</style>

<div class="gallery-curve-wrapper">
    <div class="gallery-action" style="position: absolute;">
        <!-- svelte-ignore a11y-missing-attribute -->
        <a
            class="go-to-comments btn-floating btn-large waves-effect waves-light active"
            style="background-color: rgb(203, 199, 159);">
            <i class="material-icons">comment</i>
        </a>
    </div>
    <div
        style="margin-top: 184px; padding: 40px; min-height: 613px; display: block;"
        class="gallery-body">
        {#await BlogGet() then blog}
            <div class="title-wrapper">
                <h3>{blog.title}</h3>
            </div>
            <div class="">
                <article class="" use:preview={blog} />
                <p class="author">
                    由{blog.user.last_name}发布在
                    <time
                        datetime={dayjs(blog.created_at).toJSON()}>{dayjs(blog.created_at).fromNow()}</time>
                </p>
                <h3>{blog.posts.length}条回复</h3>
                <div id="comments">
                    {#each blog.posts as post}
                        <ul>
                            <li id={post.id.toString()}>
                                <p class="author">
                                    {post.user.last_name}回复于<time>{dayjs(post.created_at).fromNow()}</time>
                                </p>
                                <div class="comment">
                                    <p>{post.content}</p>
                                </div>
                            </li>
                        </ul>
                    {/each}
                </div>
                <div id="">
                    <h3>发表评论</h3>
                    <InputField
                        type="text"
                        label_name="你要bb啥？？？"
                        bind:value={PostContent} />
                    <Button size="large" on:click={PostCreate}>发布</Button>
                </div>
            </div>
        {:catch err}
            <div class="title-wrapper">
                <h3>
                    嗝，这个博客不是被删了就是被封了。<br />也有可能是你不配
                </h3>
            </div>
        {/await}
    </div>
    <div
        class="fixed-action-btn"
        on:mouseenter={() => {
            floatingbtn = true;
        }}
        on:mouseleave={() => {
            floatingbtn = false;
        }}>
        {#await BlogGet() then blog}
            {#if editType == 'edit'}
                <a
                    class="btn-floating btn-large red"
                    use:link
                    href="/edit/{params.id}/">
                    <i class="large material-icons">mode_edit</i>
                </a>
            {:else if editType == 'report'}
                <!-- svelte-ignore a11y-missing-attribute -->
                <a
                    class="btn-floating btn-large red"
                    on:click={() => {
                        open(reportModal, { uid: blog.user.id });
                    }}>
                    <i class="large material-icons">report</i>
                </a>
            {/if}
        {/await}

        {#if floatingbtn}
            <ul style="" in:slide out:fade>
                <li>
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <a class="btn-floating red"><i
                            class="material-icons">insert_chart</i></a>
                </li>
                <li>
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <a class="btn-floating yellow darken-1"><i
                            class="material-icons">format_quote</i></a>
                </li>
                <li>
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <a class="btn-floating green"><i
                            class="material-icons">publish</i></a>
                </li>
                <li>
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <a class="btn-floating blue"><i
                            class="material-icons">attach_file</i></a>
                </li>
            </ul>
        {/if}
    </div>
</div>
<svelte:head>
    <!-- svelte-ignore a11y-missing-attribute -->
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
</svelte:head>
