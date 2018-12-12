# back 端的 api 文档

### `POST` /back/piginfo/insert_piginfo/
__params__
- `earid` `string(12)` 耳标 id
- `stationid` `string(12)` 测定站 id
- `foodintake` `number`  进食量（料重）
- `weight` `number` 猪体重
- `bodylong` `number` 体长
- `bodywidth` `number` 体宽
- `bodyheight` `number` 体高
- `bodytemperature` `number` 温度
- `stationtime` `number(10)` 测定站的时间（10位的时间戳）

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

### `POST` /back/piginfo/stationinfo/
__params__
- `stationid` `string(12)` 测定站 id
- `status` `string(5)` 测定站机器的运行状态（'on', 'off'）
- `changetime` `number(10)` 状态变化时间
- `errorcode` `string(5)` 故障编号（代表不同的机器的故障状态）

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```


