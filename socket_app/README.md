# Socket App

## 数据传输过程
使用 Socket 连接 C 端，传送数据到 api 接口

使用 Socket 连接 C 端，传送数据到 C 端

## 数据传输格式
### 种猪信息
```js
// 传入信息
req = {
    _type: string, // 传送的数据的类型：1 猪，2 机器
    label: string, // 猪的耳标
    temperature: number, // 体温
    feed: number, // 采食量
    length: number, // 长度
    wide: number, // 宽度
    high: number, // 身高
    time: number, // 时间 10 位数字，精确到秒，[ x ]
}
// 返回
res = {
    success: boolean, // true || false
    err_msg: string, // error message
}
```

### 测定站机器运行状态
```js
// 传入信息
req = {
    _type: string, // 2 控制机器开关
    operation: number, // 0 表示关，1 表示开
    machineId: string, // 测定站的 id
}
// 返回
res = {
    success: boolean, // true || false
    err_msg: string, // error message 
}

```
