<script lang="ts">
    import { toast } from "materialize-css";

    import { getContext } from "svelte";

    import { getUser } from "../store";
    import { ClientApi } from "../tool/api";

    import InputField from "./InputField/InputField.svelte";

    let { close } = getContext("simple-modal");

    let userPromise = getUser().then((r) => {
        last_name = r.last_name;
        email = r.email;
        return r;
    });

    let last_name = "";
    let email = "";

    const updata = () => {
            ClientApi.object.UserSetInfo({
                last_name,
                email
            }).then(r => {
                toast({
                    html: "修改成功"
                })
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
        <InputField bind:value={last_name} label_name="昵称"/>
        <InputField bind:value={email} label_name="电子邮箱"/>
    {/await}
</div>
<div class="card-action">
    <!-- svelte-ignore a11y-missing-attribute -->
    <a
        on:click={updata}>修改</a>
</div>
