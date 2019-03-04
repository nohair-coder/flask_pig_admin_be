# admin/login

### `POST` /admin/login/sigup
用户注册
__params__
- `username` `string` `required` 用户名 [1,30]
- `password` `string` `required` 密码 [6,30]
- `email` `string` `required` 邮箱
- `phone` `string` `required` 手机号 11位

__return__
```js
ret = {
    success: boolean,  // true || false
    data: {
        user: {
            username: String, // 用户名
            token: String, // 校验 token
            rank: String, // 用户级别 super || common
        },
    },
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `POST` /admin/login/signin
用户注册
__params__
- `username` `string` `required` 用户名 [1,30]
- `password` `string` `required` 密码 [6,30]

__return__
```js
ret = {
    success: boolean,  // true || false
    data: {
        user: {
            username: String, // 用户名
            token: String, // 校验 token
            rank: String, // 用户级别 super || common
        },
    },
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `POST` /admin/login/forget_pass
忘记密码，用邮箱激活新密码
__params__
- `email` `string` `required` 邮箱
- `password` `string` `required` 新密码 [6,30]

__return__
```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `GET` /admin/login/forget_pass_confirm
通过网页get请求激活新密码

__params__
- `code` `string` `required` 128 位校验码

__return__
```js
ret = 'html string' // 返回html字符串
```
