<!--
    @component
    登陆插件
-->
<script lang="ts">
    import M from "materialize-css";

    import { fly, slide } from "svelte/transition";

    import { push } from "svelte-spa-router/Router.svelte";

    import InputField from "../Components/InputField/InputField.svelte";
    import Card from "../Components/Card/Card.svelte";
    import Button from "../Components/Button/Button.svelte";
    import { Login } from "../store";
    import { ClientApi } from "../tool/api";

    let user = {
        username: "",
        password: "",
    };

    let LoginClick = () => {
        if (user.password != "" && user.username != "") {
            ClientApi.object
                .AuthLogin({
                    username: user.username,
                    password: user.password,
                })
                .then(async (r) => {
                    Login.LoginToken.set(r.access);
                    Login.RefToken.set(r.refresh);
                    M.toast({
                        html: "登陆成功",
                    });
                    push("/");
                })
                .catch();
        }
    };

    $: console.log(user);
</script>

<style>
    .RecoverPassword {
        display: inline-block;
        font-size: 14px;
        margin-top: 15px;
    }
</style>

<div class="section container">
    <div class="row">
        <div
            class="col s12 m6 offset-m3"
            in:fly={{ delay: 350, x: 500 }}
            out:fly={{ x: 500, y: 0 }}>
            <Card>
                <h4 class="center">登陆</h4>
                <InputField label_name="用户名" bind:value={user.username} />
                <InputField
                    label_name="密码"
                    type="password"
                    bind:value={user.password} />
                <Button size="large" style="width: 100%" on:click={LoginClick}>
                    登陆
                </Button>
                <a
                    href="#/auth/recover"
                    class="RecoverPassword">什么？！你忘记了你的密码？</a>
                <a
                    href="#/auth/register"
                    class="RecoverPassword">不会吧！不会吧！<br />竟然还有人没有注册我们的账号？！</a>
            </Card>
        </div>
    </div>
</div>
