<script lang="ts">
    import { getContext } from "svelte";

    import { link } from "svelte-spa-router";
    import { pop } from "svelte-spa-router/Router.svelte";
    import { get } from "svelte/store";
    import { fade, slide } from "svelte/transition";
    import type { IPage } from "./main";
    import {LoginSwitch,getUser} from "./store";
    import { ClientApi } from "./tool/api";

    import SearchModal from './Components/searchBlogsModal.svelte';

    let { open } = getContext('simple-modal');

    export let RouterData: IPage;

    let UserDown: boolean = false;

</script>
<div id="section-header" class="CampusBlog-section nav">
    {#if RouterData.HeaderType == 'home'}
        <nav class="nav-extended" out:fade in:fade>
            <div class="nav-background">
                <div class="pattern active nav-div-background" />
            </div>

            <div class="nav-wrapper container">
                <a href="#/" itemprop="url" class="brand-logo site-logo">
                    {RouterData.title}
                </a>
                <ul class="right hide-on-med-and-down">
                    <li>
                        <a href="/" class="site-nav__link" use:link>主页</a>
                    </li>
                    <li>
                        <a
                            on:click="{() => {open(SearchModal);}}"
                            class="site-nav__link"
                            >搜索</a>
                    </li>
                    {#if $LoginSwitch == true}
                        <li
                            on:mouseenter={() => {
                                UserDown = true;
                            }}
                            on:mouseleave={() => {
                                UserDown = false;
                            }}>
                            {#await getUser() then User}
                                <a
                                    use:link
                                    href="/auth/me"
                                    class="user-account dropdown-button"><img
                                        class="circle"
                                        style="height: 32px;width: 32px;vertical-align: middle;margin-right: 10px;"
                                        src={User.avatar?.file ?? 'https://img.zcool.cn/community/01a3865ab91314a8012062e3c38ff6.png@2o.png'} />{ClientApi.object.emptygGet(User.last_name) ?? User.username}</a>
                                {#if UserDown}
                                    <ul
                                        in:slide
                                        out:fade
                                        class="dropdown-content"
                                        style="white-space: nowrap;position: absolute;opacity: 1;display: block;margin-left: 20px;">
                                        <li>
                                            <a href="#/auth/me">用户</a>
                                        </li>
                                        <li>
                                            <a href="{`#/search?search=${User.username}&hide=true`}">我的博客</a>
                                        </li>
                                        <li>
                                            <a
                                                on:click={ClientApi.object.AuthLoginOut}>退出登陆</a>
                                        </li>
                                    </ul>
                                {/if}
                            {/await}
                        </li>
                    {:else}
                        <li>
                            <a
                                use:link
                                href="/auth/login"
                                class="site-nav__link">登陆</a>
                        </li>
                        <li>
                            <a
                                use:link
                                href="/auth/register"
                                class="site-nav__link">注册</a>
                        </li>
                    {/if}
                </ul>
            </div>
            {#if RouterData.hideHeader == false}
                <div
                    class="nav-header center"
                    out:slide={{ delay: 400 }}
                    in:slide>
                    <h1>{RouterData.HeaderText.h1}</h1>
                    <div class="tagline">{RouterData.HeaderText.h2}</div>
                </div>
            {/if}
        </nav>
    {:else if RouterData.HeaderType == 'back'}
        <nav
            id="placeholder-navbar"
            style="background-color: rgb(220, 220, 210);"
            out:fade
            in:fade>
            <div class="nav-wrapper">
                <div class="container">
                    <a
                        class="back-btn"
                        on:click={() => {
                            pop();
                        }}>
                        <i class="material-icons">arrow_back</i>
                        <span>返回</span>
                    </a>
                </div>
            </div>
        </nav>
    {/if}
</div>