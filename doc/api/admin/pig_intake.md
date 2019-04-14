# admin/pig_intake

### `GET` /admin/pig_intake/intake_trend/

个体采食量趋势图数据获取

__params__

- `pid` `string` `required` 种猪 id
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "ave": 7.38, // 均值
        "data": [
            {
                "date": "03-11", // 日期
                "intake_total": 6.88 // 当日采食总量
            },
            {
                "date": "03-12",
                "intake_total": 7.88
            }, // ...
        ],
        "total": 14.76, // 总采食量
    },
}
```

### `GET` /admin/pig_intake/total_perstation/

测定站某日所有猪的采食总量的统计表

__params__

- `stationId` `string` `required` 测定站 id
- `time` `string` `required` 日期（当天开始的时间戳 10 位）

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "ave": 7.21, // 均值
        "data": [
            {
                "animalNum": "", // 种猪号
                "earId": "sss0sa01254s", // 耳标号
                "facNum": "", // 猪场代码
                "intake": 7.55 // 当日采食量
            },
            {
                "animalNum": "00000001254s",
                "earId": "00000001254s",
                "facNum": "icbc",
                "intake": 6.88
            }
        ],
        "total": 14.43 // 总和
    },
}
```
