# Socket App

## 数据传输过程
使用 Socket 连接 C 端，传送数据到 api 接口

使用 Socket 连接 C 端，传送数据到 C 端

## 数据传输格式
### 种猪信息
```js
// 传入信息
req = {
    _type: 1, // 传送的数据的类型：1 猪，2 测定站工作状态, 3 USBCAN 连接状态
    id: number, // 测定站的id号
    label: number, // 猪的耳标
    weight: number, // 体重
    temperature: number, // 体温
    feed: number, // 采食量
    length: number, // 长度
    wide: number, // 宽度
    high: number, // 身高
    time: number, // 时间 12 位数字，精确到秒，2018 12 18 12 13
}
// 返回
res = {
    _type: 1, // 0 返回操作反馈信息
    success: boolean, // true || false
    err_msg: string, // error message
}
```

### 测定站机器运行状态
```js
// 传入信息
req = {
    _type: 2, // 2 控制机器开关
    status: number, // 0 表示关，1 表示开
    id: number, // 测定站的 id
    errorcode: string, // 错误码 5 位字符串
}
// 返回
res = {
    _type: 2, // 0 返回操作反馈信息
    success: boolean, // true || false
    err_msg: string, // error message
}
```

### 测定站 USBCAN 状态
```js
// 传入信息
req = {
    _type: 3, // 3 USBCAN 的连接状态
    id: number, // 测定站的id
    status: number, // 连接状态： 0 disconnect  1 connect
}
// 返回
res = {
    _type: 3, // 0 返回操作反馈信息
    success: boolean, // true || false
    err_msg: string, // error message 
}
```

## 发送指令
### 界面部分发送关闭或者打开测定站的指令
```js
// 传入信息
send = {
    _type: 4, // 1 控制机器开关
    machineId: number, // 测定站的站号，将数据库12位的字符串转换成纯数字，去除前导0
    operation: number, // 0: 关 ，1: 开
}
```
