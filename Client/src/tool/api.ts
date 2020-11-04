import * as msgpack from '@msgpack/msgpack';

import { get } from "svelte/store";
import { Login } from "../store";

type HTTPmethod = "GET" | "POST" | "PUT" | "DELETE";

interface IErr {
    code: string,
    detail: string
}

interface IAuth_Login {
    username: string,
    password: string
}

export interface IBlog {
    "id": number,
    "title": string,
    "user": {
        "id": number,
        "last_name": string
    },
    "posts": IPost[],
    "subtitle": string,
    "content": string,
    "subimage": string,
    "created_at": string,
    "updated_at": string
}

export interface IBlogCreater {
    title: string,
    subtitle: string,
    subimage: string | ArrayBuffer,
    content: string
}

export interface IPost {
    "id": number,
    "blog": number,
    "user": {
        "id": number,
        "last_name": string
    },
    "content": string,
    "created_at": string
}

export interface IUser {
    "avatar": string,
    "email": string,
    "first_name": string,
    "id": number,
    "last_login": string,
    "last_name": string,
    "username": string
}

/**
 * 单例模式的API接口
 */
export class ClientApi {
    /**
     * 单例
     */
    static object = new ClientApi();

    HTTPHeader: string = "http://127.0.0.1:8000";
    PageSize: number = 20;

    async decode(data: Response, type: "json" | "msgpack" = "json") {
        if (type == "json") {
            return await data.json();
        } else if (type == "msgpack") {
            return msgpack.decode(await data.arrayBuffer());
        }
    }

    /**
     * 对于Fetch的一个访问封装
     * @param url 要访问的接口URL
     * @param searchparams 查询参数
     * @param body 数据
     * @param method 方法
     * @param token 是否使用token访问
     * @param H 自定义HTTPHeader
     * @param type 数据的格式化方法
     */
    async api<I extends {}, R extends {}>(url: string, searchparams: { [keys: string]: string } = {}, body: I | undefined = undefined, method: HTTPmethod = "GET", token: boolean = true, H: Headers = new Headers(), type: "json" | "msgpack" = "json"): Promise<R> {
        if (token === true) {
            H.set("Authorization", `Bearer ${get(Login.LoginToken)}`)
        }


        let RI: RequestInit = {};
        RI.method = method;
        RI.headers = H;
        H.set('content-type', `application/${type}`);
        searchparams['format'] = type;
        if (method == 'POST') {
            if (body != undefined) {
                if (type == "json") {
                    RI.body = JSON.stringify(body);
                } else if (type == "msgpack") {
                    RI.body = msgpack.encode(body);
                }

            }
        } else if (method == 'GET') {

        }
        // if (searchparams != undefined) {
        //     url += `?${new URLSearchParams(searchparams).toString()}`;
        // }


        let F = await fetch(`${this.HTTPHeader}${url}?${new URLSearchParams(searchparams)?.toString() ?? ''}`, RI).then(async r => {
            if (r.ok) {
                return await this.decode(r, type);

            } else {
                let b: IErr = await this.decode(r, type);
                if (r.status == 401 && b.code == "token_not_valid" && token === true) {
                    let { access } = await this.AuthRefToken(get(Login.RefToken));

                    Login.LoginToken.set(access);

                    return await this.api<I, R>(url, searchparams, body, method, token, H, type);
                } else {
                    throw b;
                }
            }
        });

        return F;
    }

    /**
     * 在认证Token失效的情况下刷新Token（无需自己执行）
     * @param reftoken 刷新token
     */
    async AuthRefToken(reftoken: string) {
        let r = await this.api<{
            "refresh": string
        }, {
            "access": string
        }>('/auth/jwt/refresh/', {}, {
            refresh: reftoken
        }, "POST", false);

        return r;
    }

    /**
     * 使用用户名和密码认证登陆
     * @param data 登陆数据
     */
    async AuthLogin(data: IAuth_Login) {
        let r = await this.api<IAuth_Login, {
            'code': string,
            'refresh': string,
            'access': string
        }>('/auth/jwt/create/', {}, data, "POST", false).catch((r: IErr) => {
            if(r.detail == "No active account found with the given credentials"){
                throw "password err";
            }
        });

        return r;
    }

    async AuthLoginOut() {
        Login.LoginToken.set("");
        Login.RefToken.set("");
    }

    async UserCreater(email: string, username: string, password: string) {
        return await this.api<{
            email: string,
            username: string,
            password: string
        }, {
            email: string,
            username: string,
            password: string
        }>("/auth/users/", {}, {
            email,
            username,
            password
        }, "POST", false);
    }

    async UsersGet(id?: number) {
        return await this.api<{}, IUser>(`/auth/users/${id ?? "me"}/`);
    }

    async BlogList(page?: number) {
        let r = await this.api<{}, {
            "count": number,
            "results": IBlog[]
        }>(`/blogs/`, { "page": `${page}` }, undefined, "GET", true, new Headers(), "msgpack");

        return r;
    }

    // async * BlogListIterator(start: number = 0, end: number = 50) {
    //     let page: { [keys: number]: IBlog[] } = {};

    //     while (true) {
    //         if (start >= end) {
    //             break;
    //         }

    //         let pageNumber = Math.floor(start / this.PageSize);
    //         if (page[pageNumber] == undefined) {
    //             let { results } = await this.BlogList(pageNumber);
    //             page[pageNumber] = results;
    //         }
    //         let n = start - (pageNumber * this.PageSize);
    //         yield page[pageNumber][n];

    //         start++;
    //     }
    // }

    async BlogGet(id: number) {
        return await this.api<{}, IBlog>(`/blogs/${id}/`).catch();
    }

    async BlogCreater(data: IBlogCreater) {
        return await this.api<IBlogCreater, IBlog>("/blogs/", undefined, data, "POST", true);
    }

    async BlogUpdata(bid: number, data: IBlogCreater) {
        return await this.api<IBlogCreater, IBlog>(`/blogs/${bid}/`, undefined, data, "PUT", true);
    }

    async BlogPost(bid: number, content: string) {
        return await this.api<{
            blog: number,
            content: string
        }, IPost>("/posts/", undefined, {
            blog: bid,
            content
        }, "POST")
    }
}