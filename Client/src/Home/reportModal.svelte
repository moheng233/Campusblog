<!--
    @component
    举报弹窗
-->
<script lang="ts">
    import { getContext } from 'svelte';
    import m from 'materialize-css';
    import InputField from '../Components/InputField/InputField.svelte';
    import { ClientApi } from '../tool/api';

    let { close } = getContext('simple-modal');

    export let uid:number;
    let content: string = ""

    const onClickBtn = () => {
        ClientApi.object.BlogReport({
            informants: uid,
            reason: content
        }).then(e => {
            m.toast({
                html: "举报成功，成功后本贴将会被封禁"
            })
            close()
        }).catch(err => {
            m.toast({
                html: "这点内容还要当海军？？？"
            })
        })
    }
</script>
<div class="modal-content">
    <h4>举报这篇文章</h4>
    <InputField label_name="快！开始你的表演！" bind:value="{content}" ></InputField>
</div>
<div class="modal-footer">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a class="waves-effect waves-green btn-flat" on:click="{onClickBtn}">确定</a>
</div>
