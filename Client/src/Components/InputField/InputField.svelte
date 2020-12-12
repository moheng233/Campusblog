<script lang="typescript">
    import { createEventDispatcher, getContext } from 'svelte';
    import uploadModal from '../uploadImgModal.svelte';
    import { UploadImg } from '../../store';
    import type { IUploadImage } from '../../tool/api';

    const dispatch = createEventDispatcher<{
        "change": HTMLInputElement,
        "selectUploadFile": IUploadImage
    }>();

    const { open } = getContext("simple-modal");

    export const openUploadImgModal = () => {
        return new Promise<IUploadImage>((res,rej) => {
            UploadImg.set(undefined);
            open(uploadModal);
            
            UploadImg.subscribe((value) => {
                if(value != undefined){
                    res(value);
                }
            })
        })
    }

    async function uploadClick(){
        openUploadImgModal().then((r) => {
            dispatch("selectUploadFile",r);
        })
    }

    export let type: "text" | "password" | "email" | "file" = "text";
    export let label_name: string;
    export let value: string = "";

</script>

<div class="input-field" class:file-field={type == "file"}>
    {#if type == 'text'}
        <input type="text" bind:value on:change="{(r) => {dispatch("change",r.currentTarget)}}" />
    {:else if type == 'email'}
        <input type="email" bind:value on:change="{(r) => {dispatch("change",r.currentTarget)}}" />
    {:else if type == 'password'}
        <input type="password" bind:value on:change="{(r) => {dispatch("change",r.currentTarget)}}" />
    {:else if type == 'file'}
        <!-- <div class="btn"><span>上传</span><input type="file" on:change="{(r) => {dispatch("change",r.currentTarget)}}" /></div>
        <div class="file-path-wrapper">
            <input class="file-path validate" type="text" />
        </div> -->
        <div class="btn" on:click="{uploadClick}"><span>上传</span></div>
        <div class="file-path-wrapper">
            <input class="file-path validate" value="{($UploadImg)?.file ?? ""}" type="text" />
        </div>
    {/if}
    {#if (label_name && type != "file")}<label for={label_name}>{label_name}</label>{/if}
</div>
