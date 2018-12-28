# admin 端的 api 文档

### `POST` /admin/contact/add/
__params__
- `email` `string(100)` `required` 邮箱
- `comment` `string(250)` `required` 备注

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

### `POST` /admin/piginfo/
__params__
- `type` `string` `required` all、station、one
- `fromId` `number` 查询起始的id
- `earid` `string` 种猪的耳标号 type == one 时
- `stationid` `string` 测定站id type == station
- `fromTime` `number` 起始时间 10 位数字时间戳
- `endTime` `number` 起始时间 10 位数字时间戳
__return__

```js
ret = {
    success: boolean,  // true || false
    data: [
        {
            bodyheight: 60,
            bodylong: 150,
            bodytemperature: 375,
            bodywidth: 45,
            earid: "1234567890",
            foodintake: 72,
            id: 341,
            stationid: "5",
            stationtime: 1545224700,
            systime: 1545229649,
            weight: 50
        }, // ...
    ],
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `POST` /admin/piginfo/export
__params__
- `type` `string` all、station、one
- `earid` `string` 种猪的耳标号 type == one 时
- `stationid` `string` 测定站id type == station
- `fromTime` `number` 起始时间 10 位数字时间戳
- `endTime` `number` 起始时间 10 位数字时间戳

- `path` `string` 保存的路径，默认为 `~`
- `filename` `string` 保存时的文件名，默认为 `YYYYMMDD-pig.csv`
- `timeasc` `boolean` 按照时间顺序离现在远的时间排在前面，默认为 `false` 倒序
- `keys` `array` 选中的字段名，不能为空数组
__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```
