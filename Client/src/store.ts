
    import { writable as localwritable } from "svelte-persistent-store/dist/local";
    import {
        derived,
        writable,
        get,
        Readable,
    } from "svelte/store";
    import { ClientApi } from "./tool/api";
    import type { IUser,IUploadImage } from "./tool/api";

    export const Login = {
        LoginToken: localwritable<string>("LoginToken", ""),
        RefToken: localwritable<string>("RefToken", ""),
    };

    export const LoginSwitch = derived(
        [Login.LoginToken, Login.RefToken],
        ([$a, $b], set) => {
            if ($a != "" && $b != "") {
                set(true);
            } else {
                set(false);
            }
        },
        false
    );

    let noLogin: IUser = {
        avatar: undefined,
        first_name: "noLogin",
        id: -1,
        email: "noLogin",
        last_name: "noLogin",
        last_login: new Date().toString(),
        username: "noLogin",
    };

    export const User = derived<[Readable<boolean>], IUser>(
        [LoginSwitch],
        ([$LoginSwitch], set) => {
            if ($LoginSwitch == true) {
                ClientApi.object.UsersGet().then((r) => {
                    set(r);
                });
            } else {
                set(noLogin);
            }
        },
        undefined
    );

    export const getUser = () => {
        return new Promise<IUser>((res, rej) => {
            if (get(User) == undefined) {
                User.subscribe((r) => {
                    if (r != undefined) {
                        res(r);
                    }
                });
            } else {
                res(get(User));
            }
        });
    };

    export const UploadImg = writable<IUploadImage | undefined>(undefined);