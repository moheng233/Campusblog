<!--
    @component
    搜索弹窗
-->
<script lang="ts">
    import { getContext } from 'svelte';
    import Vditor from 'vditor';
import { ClientApi } from '../tool/api';

    import InputField from './InputField/InputField.svelte';

    let { close } = getContext('simple-modal');

    export let nid: number;
    export let content: string;

    const preview = (node: HTMLDivElement) => {
        Vditor.preview(node, content);
    };

    const readed = () => {
        ClientApi.object.ReadedNotices(nid);
        close();
    }
</script>

<div class="card-content">
    <div use:preview></div>
</div>
<div class="card-action">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a on:click={readed}>已读</a>
</div>