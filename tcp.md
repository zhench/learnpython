# TCP

## 创建socket ##

```python
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
```
参数是一个tuple

## 发送请求

