# admin 端的 api 文档

### `POST` /admin/contact/add/
__params__
- `email` `string(100)` 邮箱
- `comment` `string(250)` 备注

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `GET` /admin/dashboard/stationinfo/
__params__
None

__return__

```js
ret = {
    success: boolean,  // true || false
    data: [
        {
            changetime, // 状态的变更时间 1544414826
            errorcode, // 错误码 "12345"
            id, // 记录 id  1
            stationid, // 测定站id "qwertyuiopas"
            status, // 状态 "on" "off"
        }, // ...
    ],
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```
