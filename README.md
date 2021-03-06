# Nttttbot
## 框架
基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp), 配置在vps上，系统为Ubuntu18.04.
使用http接口，端口设为5700。

## Python本地服务器
在本地搭设一个主机端，端口设为7496。
接收cqhttp上传的数据，在服务器内部对接收到的json进行分析以及响应。

## 响应调用API
对cq服务器发送POST，从而调用cqhttp的API。

## 功能列表

### Python计算
对收到的字符串进行运算，通过eval()实现。

调用示例：

```
$ @bot 计算1+1
> 2
```

### 简单问答
使用了chatterbot效果并不好，用几个常用短语随机回答，偶尔效果还不错。
对含有关键字的语句也可以触发回复。
用字典储存固定问答，用户可以增减字典元素。

调用示例：
```
$ @bot 问：XXX 答：YYY
$ @bot XXX
> YYY
```
### 图片转发
利用了[lolicon图片接口](https://api.lolicon.app),使用CQ码进行图片传输。

调用示例：
```
$ 图来
> [image]
```

### 词语查询
在[小鸡词典](https://jikipedia.com/)上进行词语查询，将查询结果作为字符串返回。

调用示例：
```
$ @bot 0是什么
> 0  
  同性恋性生活中受的一方，与1相对。
```

### 德州扑克
主要利用[deuces](https://github.com/worldveil/deuces)框架实现（适用于python3的库名是treys）

调用示例：
```♠ ♥ ♦ ♣
$ 开始德州    
> 创建成功    
$ 给我发牌    
> 发牌成功
(private)> 你的手牌是：[T♠][9♦]   
$ 翻牌  
> 牌桌：
[J♥]
[A♦]
[8♠]  
$ 翻牌    
> 牌桌：
[J♥]
[A♦]
[8♠]
[9♠]    
$ 翻牌  
> 牌桌：
[J♥]
[A♦]
[8♠]
[9♠]
[4♦]    
$ 翻牌   
> 赢家：@User
手牌：[T♠][9♦] 
牌型：Pair
```

### RSS订阅
利用[feedparser](https://github.com/kurtmckee/feedparser)框架实现。

调用示例：
```
$ [rss源名]
> [rss内容]
```

