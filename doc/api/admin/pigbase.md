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
- `body_temp` `string` `option` 体温
- `env_temp` `string` `option` 环境温度
- `env_humi` `string` `option` 环境湿度
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
