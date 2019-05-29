# admin/pigbase

### `POST` /admin/pigbase/

添加一条测定站记录

__params__

- `earid` `string` `required` 耳标号
- `stationid` `string` `required` 测定站id
- `food_intake` `string` `required` 采食量
- `weight` `string` `required` 体重
- `body_long` `string` `required` 体长
- `body_width` `string` `required` 体宽
- `body_height` `string` `required` 体高
- `body_temp` `string` 体温
- `env_temp` `string` 环境温度
- `env_humi` `string` 环境湿度
- `start_time` `string` `required` 采食开始时间
- `end_time` `string` `required` 采食结束时间

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

demo
<p>处理成功的时候<p>
<img src=http://qiniu1.lxfriday.xyz/WaterM/bfb1d2ff-c6d1-42d9-9205-e591220057f4_QQ20190319-093732.png>
<p>处理失败的时候</p>
<img src=http://qiniu1.lxfriday.xyz/WaterM/f7511041-4364-4f3e-8d97-c5908f7b7aaf_QQ20190319-093756.png>


### `GET` /admin/pigbase/

查询种猪基础数据信息

__params__

- `type` `string` `required` 类型 `s` `station` `one`
- `fromId` `string` 起始查找的 id （不包括）
- `pid` `string` `type='one'` 时，需要输入测定编号
- `stationId` `string` 测定站号，`type='station'` 时，需要输入测定站号
- `fromTime` `string` 起始时间（10位时间戳）
- `endTime` `string` 结束时间（10位时间戳）

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "hasNextPage": false, // 是否有下一页
        "lastId": 0, // 下一次加载的时候的起始id
        "list": [ // 列表数据
            {
                "id": 452, // 在 pig_base 中的 id
                "pid": 14, // 在 pig_list 中的 id
                "foodIntake": 7.22, // 采食量
                "weight": 181.11, // 体重
                "bodyLong": 120.33, // 体长
                "bodyWidth": 30.22, // 体宽
                "bodyHeight": 50.44, // 体高
                "bodyTemp": 1, // 体温
                "envTemp": 2, // 环境温度
                "envHumi": 3, // 环境湿度
                "startTime": 1552017439, // 采食开始时间
                "endTime": 1552017448, // 采食结束时间
                "sysTime": 1553082227, // 系统处理该记录的系统时间

                "facNum": "", // 猪场代码
                "stationId": "asdfghjklqwe", // 测定站号
                "earId": "xxxxxxxxxcde", // 耳标号
                "animalNum": "", // 种猪号
                "entryTime": 1553082227, // 种猪入栏时间
            }, // ...
        ]
    },
}
```

