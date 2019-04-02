# admin/graphanalyse

### `GET` /admin/graphanalyse/food_intake_interval_analysis/
采食量区间分析
__params__
- `stationId` `string` `required` 测定站 id
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__
```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "0-200": 0.5, // [0, 200)
        "200-400": 0.5, // [200, 400)
        "400-600": 0,
        "600-800": 0,
        "800-1000": 0,
        "1000-1200": 0,
        "1200-1400": 0,
        "1400-1600": 0,
        ">1600": 0,
        "count": 58, // 总的统计记录数
    },
}
```

### `GET` /admin/graphanalyse/weight_change/
体重变化趋势图
__params__
- `type` `string` `required` 是显示一个测定站的数据还是显示一头猪的数据 `station` 查询一个测定站的所有猪的体重变化，`pig` 一头猪的体重变化
- `stationId` `string` `required` 测定站 id，`type=station` 时
- `pid` `string` `required` 种猪 id，`type=pig` 时
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__
```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "data": [
            {
                "00000001254s": 119.42, // 数组的在当天有值，没有数据的则没有该耳标号和值
                "date": "03-11",
                "sss0sa01254s": 123.45,
            },
            {
                "00000001254s": 120.22,
                "date": "03-12",
                "sss0sa01254s": 124.35
            },
            {
                "00000001254s": 121.22,
                "date": "03-13",
                "wss0sav12547": 180.11,
                "xxx0sav12547": 180.11
            }
        ],
        // 耳标号数组，和上面的耳标号对应上
        "earIdArr": [
            "sss0sa01254s",
            "00000001254s",
            "xxx0sav12547",
            "wss0sav12547"
        ]
    },
}
```
