# admin/stationinfo

### `GET` /admin/stationinfo

获取所有测定站信息

__params__

- `errFirst` `string` 将 off、或者有故障的测定站放在首部

__return__

```js
ret = {
    success: boolean,  // true || false
    data: [
        {
            id: Number, // 在表中记录的id
            stationid: String, // 12位字符串
            changetime: Number, // 10位数字
            comment: String || null, // 字符串或者 null
            errorcode: String, // 5位数字 
            status: "off", // on || off
            reason: String, // 故障描述
        }, // ...
    ],
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `POST` /admin/stationinfo

添加一条测定站记录

__params__

- `stationid` `string` `required` 12位字符串
- `comment` `string` `required` 50个字符以内的备注
- `status` `string` `required` `on` `off`

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `DELETE` /admin/stationinfo

删除一条测定站记录

__params__

- `stationid` `string` `required` 12位字符串

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `PUT` /admin/stationinfo

更改一个测定站的记录信息

__params__

- `stationid` `string` `required` 12位字符串
- `comment` `string`  50个字符以内的备注
- `status` `string` `on` `off`
- `errorcode` `string` 5位的故障码 

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```


### `PUT` /admin/stationinfo/set_station
设定测定站的开关机状态

__params__

- `settingPairs` `array` `required` 类似 [['000000000010', 'open_device'], ['000000000011', 'close_device']]

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```
