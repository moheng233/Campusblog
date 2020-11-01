<script lang="typescript">

    export let type: "text" | "password" | "email" = "text";
    export let label_name: string;
    export let value: string = "";
</script>

<div class="input-field">
    {#if type == "text"}
        <input type="text" bind:value="{value}">
    {:else if type == "email"}
        <input type="email" bind:value="{value}">
    {:else if type == "password"}
        <input type="password" bind:value="{value}">
    {/if}
    {#if label_name}
        <label for="{label_name}">{label_name}</label>
    {/if}
</div>