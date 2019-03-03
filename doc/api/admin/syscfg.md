# admin/syscfg

### `GET` /admin/syscfg/get_all_kvs
__params__
无

__return__
```js
ret = {
    success: boolean,  // true || false
     // 请求成功
    "data": [
        {
            "comment": "系统设置-猪场代码",
            "name": "FAC_NUM",
            "value": "hzaa"
        },
        {
            "comment": "基础数据页面允许显示的字段",
            "name": "PIG_BASE_DATA_FIELDS",
            "value": "id,earid,stationid"
        },
        {
            "comment": "系统设置-显示选择语言",
            "name": "SHOW_SELECT_LANGUAGE",
            "value": "false"
        },
        {
            "comment": "系统设置-显示时间同步区域",
            "name": "SHOW_TIME_SYNC",
            "value": "false"
        }
    ],
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```
### `PUT` /admin/syscfg/update_kv
__params__
- `name` `string` `required`
- `value` `string` `required`
    - `FAC_NUM` -> 四位的字符串
    - `PIG_BASE_DATA_FIELDS` -> 其中的组合构成的数组 ("id", "earid", "animalnum", "stationid", "food_intake", "weight", "body_long", "body_width", "body_height", "body_temp", "env_temp", "env_humi", "start_time", "end_time", "sys_time")
    - `SHOW_SELECT_LANGUAGE` -> 'true' || 'false'
    - `SHOW_TIME_SYNC` -> 'true' || 'false'

__return__
```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
}
```

