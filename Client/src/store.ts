import { writable as localwritable } from 'svelte-persistent-store/dist/local';
import { derived, get, Readable, readable, Writable } from 'svelte/store'
import { ClientApi, IBlog } from './tool/api';
import type {IUser} from './tool/api';

export const Login = {
    LoginToken: localwritable<string>('LoginToken',''),
    RefToken: localwritable<string>('RefToken',''),
}

export const LoginSwitch = derived([Login.LoginToken,Login.RefToken], ([$a,$b],set) => {
    if($a != "" && $b != ""){
        set(true);
    } else {
        set(false);
    }
},false)

let noLogin:IUser = {
    "avatar": "http://127.0.0.1:8000/static/avatar/avatar.jpg",
    "first_name": "noLogin",
    "id": -1,
    "email": "noLogin",
    "last_name": "noLogin",
    "last_login": new Date().toString(),
    "username": "noLogin"
}

export const User = derived<[Readable<boolean>], IUser>([LoginSwitch], ([$LoginSwitch],set) => {
    if($LoginSwitch == true){
        // const RefUser = async () => {
        //     let u = await ClientApi.object.UsersGet();

        //     localStorage.setItem("user", JSON.stringify({
        //         updata_time: new Date(),
        //         data: u
        //     }))

        //     return u;
        // }
    
        // let userjson  = localStorage.getItem("user");
        // if(userjson == null){
        //     set(await RefUser())
        // } else {
        //     let Data: {
        //         updata_time: Date,
        //         data: IUser
        //     } = JSON.parse(userjson);
        //     if(Data.updata_time.valueOf() - new Date().valueOf() >= 1200000){
        //         RefUser()
        //     }
        // }
        ClientApi.object.UsersGet().then((r) => {
            set(r);
        })
    } else {
        set(noLogin)
    }
    
},undefined)

export const getUser =  () => {
    return new Promise<IUser>((res,rej) => {
        if(get(User) == undefined){
            User.subscribe((r) => {
                if(r != undefined){
                    res(r);
                }
            })
        } else {
            res(get(User))
        }
    })
}