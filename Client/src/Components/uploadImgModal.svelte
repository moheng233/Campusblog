<script lang="ts">
    import { Tabs } from "materialize-css";
    import { ClientApi } from "../tool/api";

    import Button from "./Button/Button.svelte";

    const init = (node: HTMLUListElement) => {
        Tabs.init(node);
    };

    let select = 0;

    let uploadfile: string;

    const onUploadChange = async (r: Event & {currentTarget: EventTarget & HTMLInputElement}) => {
        let files = r.currentTarget.files;
        if(files.length != 0){
            uploadfile = await ClientApi.object.File2Base64(files[0]);
        }
    }

    const upload = () => {
        // ClientApi.object.UploadImages(ClientApi.object.File2Base64(uploadfile.))
        console.log(uploadfile)
        ClientApi.object.UploadImages(uploadfile)
    }
</script>

<style>
    .masonry {
        display: grid;
        grid-gap: 40px;
        grid-auto-flow: dense;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-rows: auto;
    }
</style>

<div class="card-content">
    <h4>图片库</h4>
</div>
<div class="card-tabs">
    <ul class="tabs tabs-fixed-width" use:init>
        <li class="tab">
            <a
                class:active={select == 0}
                on:click={() => {
                    select = 0;
                }}>上传图片</a>
        </li>
        <li class="tab">
            <a
                class:active={select == 1}
                on:click={() => {
                    select = 1;
                }}>选择图片</a>
        </li>
    </ul>
</div>

{#if select == 0}
    <div class="card-content">
        <div class="input-field file-field">
        <div class="btn"><span>选择</span><input type="file" on:change="{onUploadChange}" /></div>
            <div class="file-path-wrapper">
                <input class="file-path validate" type="text" />
            </div>
        </div>
        <Button size="large" style="width: 100%" on:click={upload} >上传</Button>
    </div>
{/if}
{#if select == 1}
    <div class="card-content masonry">
        {#await ClientApi.object.GetImagesListByUser() then ImagesList}
            {#each ImagesList as Images}
                <div class="card" style="">
                    <div class="card-image">
                        <img class="" src="{Images.file}" />
                    </div>
                    <div class="card-action">
                        <a>选择</a>
                        <a>删除</a>
                    </div>
                </div>
            {/each}
        {/await}
    </div>
{/if}
