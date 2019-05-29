# admin/piglist


### `GET` /admin/piglist/get_piglist_from_station/

查询一栏里面的所有猪

__params__

- `stationId` `string` `required` 测定站号

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: [
       {
            "id": 1, // 种猪 id
            "earId": "00000001254s", // 耳标号
            "animalNum": "00000001254s", // 种猪号
            "facNum": "icbc", // 猪场代码
            "stationId": "xxxdddeeedbn", // 测定站号
            "entryTime": 1551856710, // 入栏时间
            "exitTime": null, // 出栏时间
            "recordId": '0000000000000001', // 记录的 id
        }, // ...
    ],
}
```

### `POST` /admin/piglist/entry_one/

入栏一头猪（手动入栏的情况，必须输入符合规范的猪场代码、种猪号、耳标号、测定站号）

__params__

- `pid` `string` `required` 测定编号
- `animalNum` `string` `required` 种猪号
- `earId` `string` `required` 耳标号
- `stationId` `string` `required` 测定站号

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "pid": "111", // 测定编号
        "earid": "earidxxxaxx1", // 耳标号
        "animalnum": "animalnum000", // 种猪号
        "stationid": "000000012545", // 测定站号
        "entry_time": 1554113474, // 入栏时间
    },
}
```

### `PUT` /admin/piglist/exit_one/

出栏一头猪，出栏不是删除一头猪，而是将该猪的出栏时间填充上即可

__params__

- `recordId` `string` `required` 记录 id

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `PUT` /admin/piglist/exit_one_station/

出栏一个测定站的所有猪

__params__

- `stationId` `string` `required` 测定站 id

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `PUT` /admin/piglist/update_piginfo/

出栏一个测定站的所有猪

__params__

- `pid` `string` `required` 种猪测定编号
- `recordId` `string` `required` 记录 id
- `animalNum` `string` `required` 种猪号
- `earId` `string` `required` 耳标号

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

