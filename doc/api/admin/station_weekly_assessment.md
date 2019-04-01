# admin/station_weekly_assessment

### `GET` /admin/station_weekly_assessment_info/
添加一条测定站记录
__params__
- `stationId` `string` `required` 测定站号
- `startTime` `string` `required` 开始时间
- `endTime` `string` `required` 结束时间

__return__
```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    "data": [
        {
            "pid": 1, // pig_list 中的 id
            "earId": "00000001254s", // 耳标号
            "animalNum": "00000001254s", // 种猪号
            "facNum": "icbc", // 猪场代码
            "day1": 6.88, // 第一天
            "day2": 7.88, // 第二天
            "day3": 7.98, // 第三天
            "day4": 0, // 第四天
            "day5": 0, // 第五天
            "day6": 0, // 第六天
            "day7": 0, // 第七天
            "total": 22.74, // 一周采食总量
            "ave": 3.25, // 一周采食均值(total/有采食数据的天数)
        }, // ...
    ],
}
```
