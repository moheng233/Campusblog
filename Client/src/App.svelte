<script lang="typescript">
	import m from "materialize-css";

	import Router, { link } from "svelte-spa-router/Router.svelte";
	import type { IPage } from "./main";

	import Modal from "./Components/Modal/Modal.svelte";

	import Nav from "./nav.svelte";

	import login from "./Login/login.svelte";
	import register from "./Login/register.svelte";
	import home from "./Home/home.svelte";
	import blogContent from "./Home/blogContent.svelte";
	import me from "./Login/me.svelte";

	import wrap from "svelte-spa-router/wrap";
	import * as store from "./store";
	import BlogEdit from "./Home/blogEdit.svelte";
	import type { WrappedComponent } from "svelte-spa-router";

	export let RouterData: IPage = {
		title: "主页",
		hideHeader: false,
		HeaderType: "home",
		HeaderText: {
			h1: "",
			h2: "",
		},
	};

	export let RouterList: { [keys: string]: WrappedComponent } = {
		"/": wrap({
			// @ts-ignore
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
		"/search": wrap({
			// @ts-ignore
			component: home,
			userData: {
				title: "搜索",
				HeaderType: "back",
				hideHeader: true
			}
		}),
		"/edit/:id": wrap({
			// @ts-ignore
			component: BlogEdit,
			userData: {
				title: "发布你的沙雕言论",
				HeaderType: "back",
				hideHeader: true,
			},
		}),
		"/blog/:id": wrap({
			// @ts-ignore
			component: blogContent,
			userData: {
				title: "详细",
				HeaderType: "back",
				hideHeader: true,
			},
		}),
		"/auth/login": wrap({
			// @ts-ignore
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
		"/auth/register": wrap({
			// @ts-ignore
			component: register,
			userData: {
				title: "注册",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "我盲猜你没有账号！",
					h2: "你是来注册的吧！",
				},
			},
		}),
		"/auth/me": wrap({
			// @ts-ignore
			component: me,
			userData: {
				title: "我的",
				HeaderType: "home",
				hideHeader: false,
				HeaderText: {
					h1: "在？看看自己",
					h2: "是个什么沙雕玩意",
				},
			},
		}),
	};

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

<!-- svelte-ignore a11y-missing-attribute -->
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
	<Modal>
		<Nav {RouterData} />
		<div>
			<Router
				routes={RouterList}
				on:routeLoaded={onRouteLoaded}
				restoreScrollState={true} />
		</div>
	</Modal>
</main>
