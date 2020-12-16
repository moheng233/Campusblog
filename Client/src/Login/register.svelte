<!--
    @component
    注册界面
-->
<script lang="ts">
    import M from 'materialize-css'

    import Card from '../Components/Card/Card.svelte';
    import InputField from '../Components/InputField/InputField.svelte';
    import Button from '../Components/Button/Button.svelte';
    import { fly } from 'svelte/transition';
    import { ClientApi } from '../tool/api';
    import { replace } from 'svelte-spa-router/Router.svelte';

    let form:{
        "username": string,
        "email": string,
        "password": string
    } = {
        "username": "",
        "email": "",
        "password": ""
    }

    let Register = async () => {
        let data = await ClientApi.object.UserCreater(form.email,form.username,form.password).then(r => {
            M.toast({html: "注册成功！"});
            replace("/auth/login")
        }).catch((r:{
            username?: string[],
            email?: string[],
            password?: string
        }) => {
            console.log(r['username'])
            for (let input in r){
                for(let err of r[input]){
                    console.log(err)
                    M.toast({
                        html: `${input}:${err}`
                    })
                }
            }
        })
        
    }
</script>

<div class="section container">
    <div class="row">
        <div
            class="col s12 m6 offset-m3"
            in:fly={{ delay: 350, x: 500 }}
            out:fly={{ x: 500, y: 0 }}>
            <Card>
                <h4 class="center">注册</h4>
                <InputField label_name="用户名" bind:value={form.username} />
                <InputField label_name="邮箱" bind:value={form.email} />
                <InputField
                    label_name="密码"
                    type="password"
                    bind:value={form.password} />
                <Button size="large" style="width: 100%" on:click={Register}>
                    注册
                </Button>
            </Card>
        </div>
    </div>
</div>