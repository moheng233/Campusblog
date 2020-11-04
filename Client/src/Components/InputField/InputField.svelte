<script lang="typescript">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher<{
        "change": HTMLInputElement
    }>();


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
        <div class="btn"><span>上传</span><input type="file" on:change="{(r) => {dispatch("change",r.currentTarget)}}" /></div>
        <div class="file-path-wrapper">
            <input class="file-path validate" type="text" />
        </div>
    {/if}
    {#if (label_name && type != "file")}<label for={label_name}>{label_name}</label>{/if}
</div>
