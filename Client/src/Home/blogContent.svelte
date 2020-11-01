<script lang="ts">
    import { ClientApi } from "../tool/api";
    import type { IBlog } from "../tool/api";

    import Vditor from "vditor";

    import moment from "moment";
import InputField from "../Components/InputField/InputField.svelte";
import Button from "../Components/Button/Button.svelte";

    let BackColor: string;
    let BackImage: string = "";

    export let params: { id: number };

    let promise = ClientApi.object.BlogGet(params.id);

    let preview = (node: HTMLDivElement, blog: IBlog) => {
        Vditor.preview(node, blog.content, {
            anchor: 0,
        });
    };
</script>

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
        {#await promise then blog}
            <div class="title-wrapper">
                <h3>{blog.title}</h3>
            </div>
            <div class="">
                <article class="" use:preview={blog} />
                <p class="author">
                    由{blog.user.last_name}发布在
                    <time
                        datetime="{moment(blog.created_at).toJSON()}">{moment(blog.created_at).fromNow()}</time>
                </p>
                <h3>{ blog.posts.length }条回复</h3>
                <div id="comments">
                    {#each blog.posts as post}
                        <ul>
                            <li id="{post.id.toString()}" >
                                <p class="author">
                                    {post.user.last_name}回复于<time>{moment(post.created_at).fromNow()}</time>
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
                    <InputField type="text" label_name="你要bb啥？？？" />
                    <Button size="large">发布</Button>
                </div>
            </div>
        {/await}
    </div>
</div>
<!-- <div
    id="placeholder-overlay"
    style="background: {BackColor} url({BackImage}) repeat-x;background-blend-mode: lighten;"
    class="visible" /> -->
<svelte:head>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
</svelte:head>
