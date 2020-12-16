<!--
    @component
    首页
-->
<script lang="ts">
    import dayjs from 'dayjs';
    import "dayjs/locale/zh-cn";

    dayjs.locale("zh-cn");

    import Blog from "./blog.svelte";

    import { fade, fly } from "svelte/transition";
    import { ClientApi } from "../tool/api";
    import { link, querystring } from "svelte-spa-router";
    import { LoginSwitch } from "../store";
    import { memoize, range } from "lodash";

    export let ClassifyFilter: boolean = false;

    $: query = new URLSearchParams($querystring);

    $: console.log(emptygGet(query.get('hide')));

    function getQuery(
        option: {
            classify?: number;
            page?: number;
            hide?: boolean;
        } = {}
    ) {
        let q = new URLSearchParams(query.toString());

        if (option.classify != undefined) {
            q.set("classify", emptygGet(option.classify));
        }

        if (option.page != undefined) {
            q.set("page", emptygGet(option.page));
        }

        return q.toString();
    }

    function getCPage() {
        return Number(new URLSearchParams($querystring).get("page") ?? 1);
    }

    let emptygGet = memoize(ClientApi.object.emptygGet);
</script>

{#if emptygGet(query.get('hide')) == undefined}
<nav class="filter-navbar" style="">
    <div class="categories-wrapper" style="height: 48px; ">
        <div class="categories-container pin-top" style="top: 0px;">
            <ul class="categories container" data-filter="type">
                <li class="">
                    <a
                        href="/"
                        use:link
                        class:active={ClientApi.object.emptygGet(query.get('classify')) == undefined}>所有</a>
                </li>
                {#await ClientApi.object.ClassifyList() then classifys}
                    {#each classifys as classify}
                        <li class="">
                            <a
                                href="/?{getQuery({
                                    classify: classify.id,
                                    page: 1,
                                })}"
                                use:link>{classify.title}</a>
                        </li>
                    {/each}
                {/await}
            </ul>
        </div>
    </div>
</nav>
{/if}
<div
    style="margin-top: 80px"
    in:fly={{ delay: 300, x: -500 }}
    out:fly={{ x: -500 }}>
    {#await ClientApi.object.BlogList(Number(query.get('page') ?? 1), emptygGet(query.get('search')), emptygGet(query.get('classify')),emptygGet(query.get('search'))) then blogs}
        {#each blogs.results as blog}
            <Blog
                id={blog.id}
                post_user={emptygGet(blog.user.last_name) ?? blog.user.username}
                created_at={blog.created_at}
                title={blog.title}
                subtitle={blog.subtitle}
                subimage={blog.subimage.file} />
        {/each}
        {#if blogs.count >= ClientApi.object.PageSize}
            <div class="container">
                <ul class="pagination">
                    <li class:disabled={getCPage() == 1}>
                        <a
                            href="/?{getQuery({ page: getCPage() - 1 })}"
                            use:link><i
                                class="material-icons">chevron_left</i></a>
                    </li>
                    {#each range(1, Math.ceil(blogs.count / 20) + 1) as page}
                        <li
                            class="waves-effect"
                            class:active={getCPage() == page}>
                            <a
                                href="/?{getQuery({ page: page })}"
                                use:link>{page}</a>
                        </li>
                    {/each}
                    <li
                        class:disabled={getCPage() == Math.ceil(blogs.count / 20)}>
                        <a
                            href="/?{getQuery({ page: getCPage() + 1 })}"
                            use:link><i
                                class="material-icons">chevron_right</i></a>
                    </li>
                </ul>
            </div>
        {/if}
    {/await}
</div>

{#if $LoginSwitch}
    <div class="fixed-action-btn">
        <a class="btn-floating btn-large red" href="/edit/creater" use:link><i
                class="large material-icons">mode_edit</i></a>
    </div>
{/if}
