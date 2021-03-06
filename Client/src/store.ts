
import { writable as localwritable } from "svelte-persistent-store/dist/local";
import {
    derived,
    writable,
    get,
    Readable,
} from "svelte/store";
import { ClientApi } from "./tool/api";
import type { IUser, IUploadImage } from "./tool/api";

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

export const Fabulous = localwritable<
    { [keys: number]: boolean }
>("fabulous", {});


export const User = derived<[Readable<boolean>], IUser>(
    [LoginSwitch],
    ([$LoginSwitch], set) => {
        if ($LoginSwitch == true) {
            ClientApi.object.UsersGet().then((r) => {
                set(r);
            });
        } else {
            set(undefined);
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