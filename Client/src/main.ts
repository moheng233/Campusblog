import App from './App.svelte';


// import S from './s';

// import '@fortawesome/fontawesome-free/css/all.css'

export interface IPage {
	title: string;
	hideHeader: boolean;
	HeaderType: "home" | "back",
	HeaderText?: {
		h1?: string,
		h2?: string
	}
}

const app = new App({
	target: document.body,
	props: {
		name: '登陆'
	}
});

export default app;