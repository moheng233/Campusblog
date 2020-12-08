<script lang="ts">
    import Vditor from "vditor";
    import { ClientApi } from "../tool/api";
    import type { IBlog, IBlogCreater } from "../tool/api";
    import m from "materialize-css";

    import InputField from "../Components/InputField/InputField.svelte";
    import { push, replace } from "svelte-spa-router/Router.svelte";
    import { get } from "svelte/store";
    import { Login } from "../store";
    import { getContext } from "svelte";

    export let params: {
        id: number | "creater";
    };

    async function BlogGetByCreater(id: number | "creater") {
        if (id == "creater") {
            let data: IBlogCreater = {
                content: "",
                subimage: undefined,
                classify: undefined,
                subtitle: "",
                title: "",
            };
            return data;
        } else {
            let data = await ClientApi.object.BlogGet(id);
            let newdata: IBlogCreater = {
                content: data.content,
                subimage: (data.subimage as unknown) as number,
                classify: undefined,
                subtitle: data.subtitle,
                title: data.title,
            };
            return newdata;
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
        classify: undefined,
        subimage: undefined,
    };

    const onSubimage = async (event: CustomEvent<HTMLInputElement>) => {
        ClientApi.object
            .UploadImages(
                await ClientApi.object.File2Base64(event.detail.files[0])
            )
            .then((e) => {
                BlogData.subimage = e.id;
            });
    };

    const onCheckClick = async () => {
        if (params.id == "creater") {
            let blog = await ClientApi.object.BlogCreater(BlogData);
            m.toast({
                html: "发布成功",
            });
            replace(`/blog/${blog.id}`);
        } else {
            console.log(BlogData);
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
                upload: {
                    url: `${ClientApi.object.HTTPHeader}/uploadimage/`,
                    accept: "image/*",
                    headers: {
                        Authorization: `Bearer ${get(Login.LoginToken)}`,
                    },
                    format: (Files: File[], responseText: string) => {
                        let rj: {
                            id: number;
                            user: {
                                id: number;
                                last_name: string;
                            };
                            file: string;
                        } = JSON.parse(responseText);

                        let filename = new URL(rj.file).pathname
                            .split("/")
                            .pop();
                        let r: {
                            msg: string;
                            code: number;
                            data: {
                                errFiles: string[];
                                succMap: {
                                    [keys: string]: string;
                                };
                            };
                        } = {
                            msg: "上传成功",
                            code: 0,
                            data: {
                                errFiles: [],
                                succMap: {},
                            },
                        };

                        r.data.succMap[filename] = rj.file;
                        return JSON.stringify(r);
                    },
                    fieldName: "file",
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
            <label>选择分类</label>
            <select class="browser-default" bind:value={BlogData.classify}>
                <option value="" disabled selected>选择文章分类</option>
                {#await ClientApi.object.ClassifyList() then classifys }
                    {#each classifys as classify}
                        <option value={classify.id}>{ classify.title }</option>
                    {/each}
                {/await}
            </select>
            <InputField
                label_name="首页大图"
                type="file"
                on:change={onSubimage} />
            <div use:init={blog} />
        {/await}
    </div>
</div>
<div class="fixed-action-btn">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a class="btn-floating btn-large red" on:click={onCheckClick}><i
            class="large material-icons">check</i></a>
</div>

<svelte:head>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
</svelte:head>
