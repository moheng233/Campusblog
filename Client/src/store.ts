import { writable, readable, derived } from 'svelte-persistent-store/dist/local';

export const Login = {
    Login: writable<boolean>('Login',false),
    LoginToken: writable<string>('LoginToken',''),
    RefToken: writable<string>('RefToken','')
}