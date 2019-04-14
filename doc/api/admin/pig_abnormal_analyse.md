# admin/pig_abnormal_analyse

### `GET` /admin/pig_abnormal_analyse/

预警分析（测定站下种猪），查询一个测定站下所有的猪的采食、体重值和同前日的差值

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
        "data": [
            {
                "03-25": {
                    "food_intake_total": 0, // 在当天没有数组则会被自动给填充为 0 
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1311,
                    "prev_foodintake_compare": -346,
                    "prev_weight_compare": 0.68,
                    "weight_ave": 47.3
                },
                "animalNum": "",
                "earId": "000009000401"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1569,
                    "prev_foodintake_compare": 244,
                    "prev_weight_compare": 0.63,
                    "weight_ave": 44.01
                },
                "animalNum": "",
                "earId": "000009000402"
            },
            {
                "03-25": {
                    "food_intake_total": 1123,
                    "prev_foodintake_compare": -8206,
                    "prev_weight_compare": 0.43,
                    "weight_ave": 48.48
                },
                "03-26": {
                    "food_intake_total": 828,
                    "prev_foodintake_compare": -295,
                    "prev_weight_compare": 0.17,
                    "weight_ave": 48.65
                },
                "animalNum": "",
                "earId": "000009000406"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1356,
                    "prev_foodintake_compare": 58,
                    "prev_weight_compare": 0.23,
                    "weight_ave": 45.25
                },
                "animalNum": "",
                "earId": "000009000427"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1509,
                    "prev_foodintake_compare": 219,
                    "prev_weight_compare": 0.86,
                    "weight_ave": 42
                },
                "animalNum": "",
                "earId": "000009000449"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 2046,
                    "prev_foodintake_compare": 438,
                    "prev_weight_compare": 0.65,
                    "weight_ave": 49.65
                },
                "animalNum": "",
                "earId": "000009000420"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1754,
                    "prev_foodintake_compare": 568,
                    "prev_weight_compare": 0.84,
                    "weight_ave": 47.99
                },
                "animalNum": "",
                "earId": "000009000409"
            },
            {
                "03-25": {
                    "food_intake_total": 1252,
                    "prev_foodintake_compare": -8843,
                    "prev_weight_compare": 1.82,
                    "weight_ave": 45.16
                },
                "03-26": {
                    "food_intake_total": 1574,
                    "prev_foodintake_compare": 322,
                    "prev_weight_compare": 0.31,
                    "weight_ave": 45.47
                },
                "animalNum": "",
                "earId": "000009000425"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1284,
                    "prev_foodintake_compare": -344,
                    "prev_weight_compare": 0.47,
                    "weight_ave": 52.14
                },
                "animalNum": "",
                "earId": "000009000448"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1985,
                    "prev_foodintake_compare": 151,
                    "prev_weight_compare": 1.38,
                    "weight_ave": 54.24
                },
                "animalNum": "",
                "earId": "000009000413"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 2286,
                    "prev_foodintake_compare": 779,
                    "prev_weight_compare": 0.46,
                    "weight_ave": 51.35
                },
                "animalNum": "",
                "earId": "000009000421"
            },
            {
                "03-25": {
                    "food_intake_total": 0,
                    "prev_foodintake_compare": 0,
                    "prev_weight_compare": 0,
                    "weight_ave": 0
                },
                "03-26": {
                    "food_intake_total": 1981,
                    "prev_foodintake_compare": 275,
                    "prev_weight_compare": 0.89,
                    "weight_ave": 54.02
                },
                "animalNum": "",
                "earId": "000009000407"
            }
        ],
        // 记录所在的日期构成的数组
        "dateArr": [
            "03-25",
            "03-26"
        ]
    },
}
```
