<script lang="ts">
    import Vditor from "vditor";
    import { ClientApi } from "../tool/api";
    import type { IBlog, IBlogCreater } from "../tool/api";
    import m from "materialize-css";

    import InputField from "../Components/InputField/InputField.svelte";
    import { push,replace } from "svelte-spa-router/Router.svelte";
    import Blog from "./blog.svelte";

    export let params: {
        id: number | "creater";
    };

    async function BlogGetByCreater(id: number | "creater") {
        if (id == "creater") {
            let data: IBlogCreater = {
                content: "",
                subimage: "",
                subtitle: "",
                title: "",
            };
            return data;
        } else {
            return await ClientApi.object.BlogGet(id);
        }
    }

    let UpdataBlogData: Promise<IBlogCreater> = BlogGetByCreater(
        params.id
    ).then((r) => {
        BlogData = r;

        return r;
    });

    let BlogData: IBlogCreater = {
        content: "",
        title: "",
        subtitle: "",
        subimage: "",
    };

    $: console.log(BlogData);

    const onSubimage = (event: CustomEvent<HTMLInputElement>) => {
        console.log(event);
        if (event.detail.files.length > 0) {
            let fr = new FileReader();
            fr.onload = (e) => {
                BlogData.subimage = e.target.result;
            };
            fr.onerror = (e) => {};
            let file = event.detail.files[0];

            console.log(file);

            fr.readAsDataURL(file);
        }
    };

    const onCheckClick = async () => {
        if (params.id == "creater") {
            let blog = await ClientApi.object.BlogCreater(BlogData);
            m.toast({
                html: "发布成功",
            });
            replace(`/blog/${blog.id}`);
        } else {
            let blog = await ClientApi.object.BlogUpdata(params.id, BlogData);
            m.toast({
                html: "修改成功",
            });
            replace(`/blog/${blog.id}/`);
        }
    };

    function init(node: HTMLDivElement, blog: IBlogCreater) {
        (async () => {
            const vditor = new Vditor(node, {
                value: blog.content,
                minHeight: 300,
                cache: {
                    enable: false,
                    id: `vditor-${params.id}`,
                },
                input: (v) => {
                    BlogData.content = v;
                },
                icon: "material",
                preview: {
                    hljs: {
                        lineNumber: true,
                    },
                },
            });
        })();
    }
    // $: BlogData.content = vditor?.getValue();
</script>

<div class="gallery-curve-wrapper">
    <div
        style="margin-top: 184px; padding: 40px; min-height: 613px; display: block;"
        class="gallery-body">
        {#await UpdataBlogData then blog}
            <InputField
                label_name="标题"
                type="text"
                bind:value={BlogData.title} />
            <InputField
                label_name="副标题"
                type="text"
                bind:value={BlogData.subtitle} />
            <InputField
                label_name="首页大图"
                type="file"
                on:change={onSubimage} />
            <div use:init={blog} />
        {/await}
    </div>
</div>
<div class="fixed-action-btn">
    <a class="btn-floating btn-large red" on:click={onCheckClick}><i
            class="large material-icons">check</i></a>
</div>

<svelte:head>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
</svelte:head>
