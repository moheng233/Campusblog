import * as msgpack from '@msgpack/msgpack';

import { get } from "svelte/store";
import { Login, LoginSwitch } from "../store";

type HTTPmethod = "GET" | "POST" | "PUT" | "DELETE";

interface IErr {
    code: string,
    detail: string
}

interface IAuth_Login {
    username: string,
    password: string
}

export interface IUploadImage {
    "id": number
    "user": {
        "id": number,
        "last_name": string
    },
    "file": string
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
    "subimage": IUploadImage,
    "created_at": string,
    "updated_at": string
}

export interface IBlogCreater {
    title: string,
    subtitle: string,
    subimage: number,
    content: string
}

export interface IPost {
    "id": number,
    "informants": number,
    "user": {
        "id": number,
        "last_name": string
    },
    "content": string,
    "created_at": string
}

export interface IReport {
    "user": number
    "blog": number
    "created_at": string,
    "reason": string,
    "permit": boolean
}

export interface IUser {
    "avatar": IUploadImage,
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

    HTTPHeader: string = "http://localhost:8000";
    PageSize: number = 20;

    async decode(data: Response, type: "json" | "msgpack" = "json") {
        if (type == "json") {
            return await data.json();
        } else if (type == "msgpack") {
            return msgpack.decode(await data.arrayBuffer());
        }
    }

    /**
     * 将文件转换为base64编码
     * 这仅仅是一个Promise封装而已！
     * @param file 文件
     */
    File2Base64(file: File) {
        return new Promise<string>((res, rej) => {
            let fr = new FileReader();
            fr.onload = (e) => {
                res(e.target.result as string)
            };
            fr.onerror = (e) => {
                rej(e)
            };

            fr.readAsDataURL(file);
        })
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
        if (token === true && get(LoginSwitch) == true) {
            H.set("Authorization", `Bearer ${get(Login.LoginToken)}`)
        }


        let RI: RequestInit = {};
        RI.method = method;
        RI.headers = H;
        H.set('content-type', `application/${type}`);
        searchparams['format'] = type;
        if (method == 'POST' || method == 'PUT' || method == "DELETE") {
            if (body != undefined) {
                if (type == "json") {
                    RI.body = JSON.stringify(body);
                    console.log(RI.body)
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
                    let { access } = await this.AuthRefToken(get(Login.RefToken))

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
        }>('/auth/jwt/create/', {}, data, "POST", false)

        return r;
    }

    /**
     * 退出登陆
     */
    async AuthLoginOut() {
        Login.LoginToken.set("");
        Login.RefToken.set("");
    }

    /**
     * 注册新用户
     * @param email 邮箱
     * @param username 用户名
     * @param password 密码
     */
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

    /**
     * 获得用户信息
     * @param id 用户id（可以为未定义，即获取自己的信息）
     */
    async UsersGet(id?: number) {
        return await this.api<{}, IUser>(`/auth/users/${id ?? "me"}/`);
    }

    async UsersUpdata(data: { last_name: string, email: string, avatar: number }, id?: number) {

    }

    async ClassifyList() {
        let r = await this.api<{},{
            "id": number,
            "title": string
        }[]>(`/classify/`,undefined,undefined,"GET",true);

        return r;
    }

    /**
     * 获得Blog列表
     * @param page 页
     */
    async BlogList(page?: number) {
        let r = await this.api<{}, {
            "count": number,
            "results": IBlog[]
        }>(`/blogs/`, { "page": `${page}` }, undefined, "GET", true);

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

    async BlogReport(data: {
        informants: number,
        reason: string
    }) {
        return await this.api<{
            informants: number,
            reason: string
        },IReport>("/reports/", undefined, data,"POST",true);
    }

    async UploadImages(file: string) {
        return await this.api<{
            file: string
        }, IUploadImage>("/uploadimage/", undefined, {
            file
        }, "POST", true)
    }
}