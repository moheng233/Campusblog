<script lang="ts">
    import Card from "../Components/Card/Card.svelte";
    import * as store from "../store";
    import uploadModal from '../Components/uploadImgModal.svelte';
    import { ClientApi } from "../tool/api";
    import type { IUploadImage } from "../tool/api";
    import { getContext } from "svelte";
    import { replace,location } from "svelte-spa-router/Router.svelte";

    const { open } = getContext("simple-modal");

    export const openUploadImgModal = () => {
        return new Promise<IUploadImage>((res,rej) => {
            
            store.UploadImg.set(undefined);
            open(uploadModal);
            
            let sub = store.UploadImg.subscribe((value) => {
                if(value != undefined){
                    res(value);
                    sub();
                }
            })
        })
    }

    const ChangeAvatar = async () => {
        openUploadImgModal().then(r => {
            ClientApi.object.UserSetAvatar(r.id).finally(() => {
                replace($location);
            })
            
        })
    }
</script>

<style>
    .list {
        padding-top: 15px;
        padding-bottom: 16px;
        display: flex;
        /* justify-content: center; */
        align-items: center;
        align-content: center;
    }
</style>

{#await store.getUser() then user}
    <div class="section container">
        <div class="row">
            <Card>
                <div class="card-title">个人资料</div>
                <div class="list">
                    <div class="col s4">头像</div>
                    <div class="col s4" style="">
                        <!-- svelte-ignore a11y-missing-attribute -->
                        <img
                            on:click="{ChangeAvatar}"
                            src={user.avatar?.file ?? 'https://img.zcool.cn/community/01a3865ab91314a8012062e3c38ff6.png@2o.png'}
                            class="circle"
                            style="height: 60px;width: 60px;margin-right: 10px;" />
                    </div>
                </div>
                <div class="divider" />
                <div class="list">
                    <div class="col s4">昵称</div>
                    <div class="col s4">{user.last_name}</div>
                </div>
                <div class="divider" />
                <div class="list">
                    <div class="col s4">电子邮件</div>
                    <div class="col s4">{user.email}</div>
                </div>
                <div class="divider" />
            </Card>
        </div>
    </div>
{/await}

<div class="fixed-action-btn">
    <!-- svelte-ignore a11y-missing-attribute -->
        <a
            class="btn-floating btn-large red"
            on:click={() => {
                
            }}><i class="large material-icons">mode_edit</i></a>
</div>
