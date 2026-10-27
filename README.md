# Port Scanner
一个用 Python 实现的基础多线程 TCP 端口扫描工具，用于网络安全学习。

## 怎么运行
在终端中运行：
`python port_scanner.py --host 127.0.0.1 --start 1 --end 1000`

## 核心功能
- 基于 socket 的 TCP 连接探测
- 多线程并发扫描（ThreadPoolExecutor）
- 扫描结果过滤输出

## 已知不足
- 目前只支持 TCP connect 扫描，尚未实现 SYN 扫描
- 超时时间目前固定为 0.5 秒
