# 针对某辣鸡BUAA的微信签到 #

自从睡过了n场高代课的扫码签到后，我决定找一个方法不去上课就能签到-_-所以就花一晚上做了这个辣鸡爬虫

目前来看，只要是用签到助手的，无论是博雅课还是课堂、班会都能找到2333

你需要先登录一下签到页面，例如[zhege](http://weixin.buaa.edu.cn/w_checkin/actions/detail.html?id=1000)

然后按下图所示找到cookie：

![](imgs/1.png)

将目标区域中的值复制到对应的cookie中（qiandao/spiders/__init__.py文件中，有时候会有PHPSESSID）

接着配置一下活动时间、名称和大致范围（不知道的话设大一点）

然后命令行切换到当前文件下，输入`scrapy crawl Qiandao`

就可以在输出链接的文件里看到期望的链接了，点开，单击签到，OK~

使用需自己安装Python3和scrapy，谢谢