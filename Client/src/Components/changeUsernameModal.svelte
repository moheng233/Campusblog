<script lang="ts">
    import { toast, Toast } from "materialize-css";

    import { getContext } from "svelte";

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
        <InputField bind:value={username} label_name="昵称"/>
        <InputField bind:value={password} type="password" label_name="确认密码"/>
    {/await}
</div>
<div class="card-action">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a
        on:click={updata}>修改</a>
</div>
