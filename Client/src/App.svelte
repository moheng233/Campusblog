<script lang="typescript">
	import Router, { link } from "svelte-spa-router/Router.svelte";
	import type { IPage } from "./main";

	import Modal from "svelte-simple-modal/src/Modal.svelte"

	import login from "./Login/login.svelte";
	import register from "./Login/register.svelte";
	import home from "./Home/home.svelte";
	import blogContent from "./Home/blogContent.svelte";
	import me from "./Login/me.svelte";

	import { push,pop } from 'svelte-spa-router/Router.svelte';
	import wrap from "svelte-spa-router/wrap";
	import { fade, slide } from "svelte/transition";
	import * as store from "./store";
	import BlogEdit from "./Home/blogEdit.svelte";
	import { ClientApi } from "./tool/api";

	let Login = store.LoginSwitch;

	export let RouterData: IPage = {
		title: "主页",
		hideHeader: false,
		HeaderType: "home",
		HeaderText: {
			h1: "",
			h2: "",
		},
	};

	export let RouterList: {} = {
		"/": wrap<IPage>({
			component: home,
			userData: {
				title: "主页",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "来看看今天沙雕的网友是谁？",
					h2: "哦，是我。",
				},
			},
		}),
		"/edit/:id": wrap<IPage>({
			component: BlogEdit,
			userData: {
				title: "发布你的沙雕言论",
				HeaderType: "back",
				hideHeader: true,
			},
		}),
		"/blog/:id": wrap<IPage>({
			component: blogContent,
			userData: {
				title: "详细",
				HeaderType: "back",
				hideHeader: true,
			},
		}),
		"/auth/login": wrap<IPage>({
			component: login,
			userData: {
				title: "登陆",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "听说你还没有我们的账号？！",
					h2: "那还不去注册？！",
				},
			},
		}),
		"/auth/register": wrap<IPage>({
			component: register,
			userData: {
				title: "注册",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "我盲猜你没有账号！",
					h2: "你是来注册的吧！"
				}
			}
		}),
		"/auth/me": wrap<IPage>({
			component: me,
			userData: {
				title: "我的",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "在？看看自己",
					h2: "是个什么沙雕玩意"
				}
			}
		})
	};

	let UserDown: boolean = false;

	function onRouteLoaded(
		event: CustomEvent<{
			route: string;
			location: string;
			querystring: string;
			userData: IPage;
			name: string;
		}>
	) {
		let ud = event.detail.userData;

		RouterData = ud;
	}
</script>

<style type="scss" global>
	@import "./styles/gallery.scss";
	/* @import "./styles/materialize.scss"; */
	/* @import "./styles/_style.scss"; */

	#section-header > nav {
		background-color: #7db557;
	}

	.nav-div-background {
		background-image: url("../static/favicon.png");
	}
</style>

<main class="gallery">
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
						<li><a href="#/" class="site-nav__link">主页</a></li>
						{#if $Login == true}
							<li on:mouseenter={() => {UserDown = true}}
								on:mouseleave={() => {UserDown = false}}>
								{#await store.getUser() then User}
									<a
									use:link
									href="/auth/me"
									class="user-account dropdown-button"><img
										class="circle"
										style="height: 32px;width: 32px;vertical-align: middle;margin-right: 10px;"
										src="{ User.avatar?.file ?? "https://img.zcool.cn/community/01a3865ab91314a8012062e3c38ff6.png@2o.png" }" />{ User.username }</a>
									{#if UserDown}
										<ul
										in:slide out:fade
										class="dropdown-content"
										style="white-space: nowrap;position: absolute;opacity: 1;display: block;margin-left: 20px;">
											<li>
												<a href="#/auth/me">用户</a>
											</li>
											<li>
												<a on:click={ClientApi.object.AuthLoginOut}>退出登陆</a>
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
						<a class="back-btn" on:click="{() => {pop()}}">
							<i class="material-icons">arrow_back</i>
							<span>返回</span>
						</a>
					</div>
				</div>
			</nav>
		{/if}
	</div>
	<div>
		<Modal>
			<Router routes={RouterList} on:routeLoaded={onRouteLoaded} restoreScrollState={true} />
		</Modal>
	</div>
</main>
