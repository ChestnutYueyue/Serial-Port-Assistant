<div align="center">
<h1 align="center">串口通信</h1>
</div>

## 开发环境
+ 编程语言：python 3.8.10
+ 图像界面：PySide2
+ 串口通信：pyserial
+ 测试运行IDE：vscode和PyCharm \
![演示](https://gitee.com/ricocosoul/Serial-Port-Assistant/raw/main/img/1.png)

## Gitee仓库
+ [Gitee仓库](https://gitee.com/ricocosoul/Serial-Port-Assistant)

## 下载运行文件
+ [releases](https://gitee.com/ricocosoul/Serial-Port-Assistant/releases/)

## 实现的功能

### 端口设置选项
- [x] 自动获取端口号
- [x] 波特率设置
- [x] 数据位设置
- [x] 效验位设置
- [x] 停止位设置
- [x] 按钮状态切换

### 接收设置选项
- [x] 十六进制设置
- [x] 暂停接收显示
- [x] 消息循环接收
### 字符编码设置选项

#### 同步支持发送和接收字符编码设置
- [x] GBK
- [x] UTF-8
- [x] BIG5
- [x] ASCii
- [x] GB2312
- [x] shift_jis
### 发送设置选项
- [x] 单点发送
- [x] 十六进制发送[功能缺陷：期待修复]
- [x] 定时发送[同步获取输入文本发送]
- [x] 暂停定时发送
- [x] 发送时间设置[功能缺陷：只能在取消定时发送或者暂停发送时设置。期待修复]
### 计数复位
- [x] 计数复位
