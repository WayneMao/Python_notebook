## 爬虫抓取今日头条数据

requests继承了urllib2的所有特性

web <----> servers <----> database

打开**开发者工具** 可以看到**Elements,Network**等，如下图所示：

![spider1](img\spider1.png)

从中我们可以看到请求方式：`GET`等

复制**Request URL**后面的URL，粘贴到浏览器，可以返回json数据。

**注意：**可以安装一个jsonview插件，便于查看json数据。

### 对Request URL进行分析

```html
https://www.toutiao.com/api/pc/feed/?
max_behot_time=1581261896&
category=__all__&
utm_source=toutiao&
widen=1&
tadrequire=true&
as=A1F5BEA431B0404&
cp=5E41E05470848E1&
_signature=S4u4tAAgEBq5pIrzX1qh60uLuKAABXM

https://www.toutiao.com/api/pc/feed/?
max_behot_time=1581257918&
category=__all__&
utm_source=toutiao&
widen=1&
tadrequire=true&
as=A1F5DEB41106502&
cp=5E41B6359082FE1&
_signature=S4u4tAAgEBq5pIrzX1qTX0uLuKAABXM
```

仔细分析之后，我们可以发现其中有一个参数`max_behot_time`这个参数代表时间戳。





### Reference:

 https://mp.weixin.qq.com/s/uKGn28eBEhWj8Mgcd8x3XA 