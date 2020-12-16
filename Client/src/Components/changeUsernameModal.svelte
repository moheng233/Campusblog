<!--
    @component
    修改用户名弹窗
-->
<script lang="ts">
    import { toast, Toast } from "materialize-css";

    import { getContext } from "svelte";
    import { replace } from "svelte-spa-router/Router.svelte";

    import { getUser } from "../store";
    import { ClientApi } from "../tool/api";

    import InputField from "./InputField/InputField.svelte";

    let { close } = getContext("simple-modal");

    let userPromise = getUser().then((r) => {
        username = r.username;
        return r;
    });

    let username = "";
    // let email = "";
    let password = "";

    const updata = () => {
            ClientApi.object.UserSetUsername(username,password).then(r => {
                replace("/auth/me");
                close();  
            }).catch((errs: {
                [key: string]: string[]
            }) => {
                Object.getOwnPropertyNames(errs).forEach((err) => {
                    for(let e of errs[err]){
                        toast({
                            html: `${err}: ${e}`
                        })
                    }
                });
            })
        }
</script>

<div class="card-content">
    <h4>修改信息</h4>
    {#await userPromise then user}
        <InputField bind:value={username} action label_name="用户名"/>
        <InputField bind:value={password} action type="password" label_name="确认密码"/>
    {/await}
</div>
<div class="card-action">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a
        on:click={updata}>修改</a>
</div>
