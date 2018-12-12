# admin 端的 api 文档

### `POST` /admin/contact/add/
__params__
- `email` `string` 邮箱
- `comment` `string` 备注

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```
