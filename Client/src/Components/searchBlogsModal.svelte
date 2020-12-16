<script lang="ts">
    import { getContext } from 'svelte';

    import InputField from './InputField/InputField.svelte';

    let { close } = getContext('simple-modal');

    let search:string = "";
</script>

<div class="card-content">
    <h4>搜索</h4>
    <InputField bind:value={search}></InputField>
</div>
<div class="card-action">
    <a href="#/search?search={search}&hide=true" on:click="{() => {close()}}">搜索</a>
</div>