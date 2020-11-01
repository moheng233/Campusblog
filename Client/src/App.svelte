<script lang="typescript">
	import Router from "svelte-spa-router/Router.svelte";
	import type { IPage } from "./main";

	import login from "./Login/login.svelte";
	import home from "./Home/home.svelte";
	import homeContent from "./Home/blogContent.svelte";

	import Blogedit from "./Home/blogEdit.svelte";

	import wrap from "svelte-spa-router/wrap";
	import { fade, slide } from "svelte/transition";
	import * as store from "./store";
	import BlogEdit from "./Home/blogEdit.svelte";
	import { ClientApi } from "./tool/api";

	let Login = store.Login.Login;

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
		"/edit": wrap<IPage>({
			component: BlogEdit,
			userData: {
				title: "发布你的沙雕言论",
				HeaderType: "back",
				hideHeader: true,
			},
		}),
		"/blog/:id": wrap<IPage>({
			component: homeContent,
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
	};

	let Title: string = "CampusBlog";

	let UserData = ClientApi.object.UsersGet();

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

		// if (ud.title != undefined) {
		// 	Title = ud.title;
		// } else {
		// 	Title = "CampusBlog";
		// }

		// if (ud.hideHeader != undefined) {
		// 	hideHeader = ud.hideHeader;
		// } else {
		// 	hideHeader = false;
		// }

		// if (ud.HeaderType != undefined) {
		// 	HeaderType = ud.HeaderType;
		// } else {
		// 	HeaderType = "home";
		// }

		RouterData = ud;
	}
</script>

<style type="scss" global>
	@import "./styles/gallery.min.scss";

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
							<li>
								{#await UserData then User}
									<a
									href="#/auth/me"
									class="user-account dropdown-button"><img
										class="circle"
										style="height: 32px;width: 32px;vertical-align: middle;margin-right: 10px;"
										src="{ User.avatar }" />{ User.last_name }</a>
								{/await}
							</li>
						{:else}
							<li>
								<a
									href="#/auth/login"
									class="site-nav__link">登陆</a>
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
						<a class="back-btn" href="#/">
							<i class="material-icons">arrow_back</i>
							<span>返回</span>
						</a>
					</div>
				</div>
			</nav>
		{/if}
	</div>
	<div>
		<Router routes={RouterList} on:routeLoaded={onRouteLoaded} />
	</div>
</main>
