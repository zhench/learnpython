# TCP
<!-- TOC -->

- [TCP](#tcp)
    - [创建socket](#创建socket)
    - [发送数据](#发送数据)
    - [接受数据](#接受数据)
- [关闭连接](#关闭连接)
- [服务器](#服务器)
    - [监听端口](#监听端口)
    - [开始监听](#开始监听)
    - [接受一个新的连接](#接受一个新的连接)
    - [创建新线程处理连接](#创建新线程处理连接)

<!-- /TOC -->
## 创建socket ##

```python
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
```
参数是一个tuple

## 发送数据

```python
s.send(data)
```
## 接受数据

```python
s.recv(1024)#每次最多接受1k字节
```
# 关闭连接

```python
s.close()
```

# 服务器

## 监听端口

```python
s.bind(('127.0.0.1',9999))
```

## 开始监听
 
```python
s.listen(5)#参数指定等待连接的最大数量。
```
## 接受一个新的连接

```python
sock,addr=s.accept()#addr是一个带有ip和端口的list
```

## 创建新线程处理连接

```python
t=threading.Thread(target=tcplink,args=(sock,addr))
t.start()
```


# UDP

- sock.SOCK_DGRAM
- data,addr=s.recvfrom(1024)
- sendto(data，addr)

