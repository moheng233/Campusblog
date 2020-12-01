<script lang="ts">
    import moment from "moment";
    import "moment/locale/zh-cn";

    moment.locale("zh-cn");

    import Blog from "./blog.svelte";

    import { fade, fly } from "svelte/transition";
    import { ClientApi } from "../tool/api";
    import { link } from "svelte-spa-router/Router.svelte";
    import { LoginSwitch } from "../store";

    let ClassifyFilter: boolean = false;

    let bloglist = ClientApi.object.BlogList(1).then((r) => {
        console.log(r);
        return r;
    });

    let classifylist = ClientApi.object.ClassifyList().then((r) => {
        console.log(r);
        return r;
    });
</script>

<nav class="filter-navbar" style="">
    <div class="categories-wrapper" style="height: 48px; ">
        <div class="categories-container pin-top" style="top: 0px;">
            <ul class="categories container" data-filter="type">
                <li class=""><a href="/" use:link>所有</a></li>
                {#await classifylist then classifys}
                    {#each classifys as classify}
                        <li class=""><a href="/" use:link>{classify.title}</a></li>
                    {/each}
                {/await}
            </ul>
        </div>
    </div>
</nav>
<div
    style="margin-top: 20px"
    in:fly={{ delay: 300, x: -500 }}
    out:fly={{ x: -500 }}>
    {#await bloglist then blogs}
        {#each blogs.results as blog}
            <Blog
                id={blog.id}
                post_user={blog.user.last_name}
                created_at={moment(blog.created_at).fromNow()}
                title={blog.title}
                subtitle={blog.subtitle}
                subimage={blog.subimage.file} />
        {/each}
    {/await}
</div>

{#if $LoginSwitch}
    <div class="fixed-action-btn">
        <a class="btn-floating btn-large red" href="/edit/creater" use:link><i
                class="large material-icons">mode_edit</i></a>
    </div>
{/if}
