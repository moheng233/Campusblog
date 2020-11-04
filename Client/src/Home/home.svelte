<script lang="ts">
    import moment from 'moment';
    import 'moment/locale/zh-cn';

    moment.locale('zh-cn');
    
    import Blog from "./blog.svelte";

    import { fade, fly } from "svelte/transition";
    import { ClientApi } from "../tool/api";
    import { link } from 'svelte-spa-router/Router.svelte';

    export let name: string = "name";

    let promis = ClientApi.object.BlogList(1);

</script>

<div
    style="margin-top: 20px"
    in:fly={{ delay: 300, x: -500 }}
    out:fly={{ x: -500 }}>
    {#await promis then blogs}
        {#each blogs.results as blog}
            <Blog
                id={blog.id}
                post_user={blog.user.last_name}
                created_at={moment(blog.created_at).fromNow()}
                title={blog.title}
                subtitle={blog.subtitle}
                subimage={blog.subimage} />
        {/each}
    {/await}
</div>

<div class="fixed-action-btn">
    <a class="btn-floating btn-large red" href="/edit/creater" use:link><i
            class="large material-icons">mode_edit</i></a>
</div>
