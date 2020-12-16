<!--
    @component
    修改密码弹窗
-->
<script lang="ts">
    import { toast, Toast } from "materialize-css";

    import { getContext } from "svelte";
    import { replace } from "svelte-spa-router/Router.svelte";

    import { getUser } from "../store";
    import { ClientApi } from "../tool/api";


    import InputField from "./InputField/InputField.svelte";

    let { close } = getContext("simple-modal");

    let userPromise = getUser();

    let new_password = "";
    // let email = "";
    let current_password = "";

    const updata = () => {
        ClientApi.object
            .UserSetPassword({
                new_password,
                current_password,
            })
            .then((r) => {
                close();
                ClientApi.object.AuthLoginOut();
                replace("/");
            })
            .catch((errs: { [key: string]: string[] }) => {
                Object.getOwnPropertyNames(errs).forEach((err) => {
                    for (let e of errs[err]) {
                        toast({
                            html: `${err}: ${e}`,
                        });
                    }
                });
            });
    };
</script>

<div class="card-content">
    <h4>修改密码</h4>
    {#await userPromise then user}
        <InputField
            bind:value={new_password}
            type="password"
            label_name="新密码" />
        <InputField
            bind:value={current_password}
            type="password"
            label_name="确认密码" />
    {/await}
</div>
<div class="card-action">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a on:click={updata}>修改</a>
</div>
