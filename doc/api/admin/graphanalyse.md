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
