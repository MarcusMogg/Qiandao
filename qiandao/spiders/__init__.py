import scrapy
import re
import datetime

class QiandaoSpider(scrapy.spiders.Spider):
    name = "Qiandao"
    baseurl =  "http://weixin.buaa.edu.cn/w_checkin/actions/detail.html?id=" 
    start_urls = []
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 micromessenger/5.0.1.352",
    }
    cookie = {
        'PHPSESSID':"",
        'appunion':"1",
        "ounion":""
    }
    #签到页面的大致范围，2017-2018上的话暂时够用
    begin = 1000
    end = 2000
    #活动日期
    date = datetime.datetime.strptime("2017.12.28 15:30", "%Y.%m.%d %H:%M")
    #活动名称，不确定的话输单字
    des = ['高','等','代','数']
    #输出所有签到的文件
    filename1 = 't.txt'
    #输出目标签到的文件
    filename2 = 'link.txt'

    def start_requests(self):
        with open(self.filename1,'wb') as target:
            target.write('活动名称 签到开始时间 签到结束时间\n'.encode())
        with open(self.filename2,'wb') as target:
            target.write('符合要求的链接\n'.encode())
        for i in range(self.begin,self.end):
            self.start_urls.append(self.baseurl+str(i))
        for i in self.start_urls:
            yield scrapy.FormRequest(
                i,
                meta = {'url':i},
                cookies = self.cookie,
                headers = self.headers,    
                callback=self.parse)

    def parse(self, response):
        if "密码账号错误，请重新登录".encode() in response.body:
            print("登录错误")
            return
        title = response.xpath('//head/title/text()').extract()[0]
        if(title == '403'):
            return
        timea = response.xpath('//p[@class="flowexp"]//span/text()').extract()
        if(len(timea)==2):
            time_b = datetime.datetime.strptime(timea[0], "%Y.%m.%d %H:%M")
            time_e = datetime.datetime.strptime(timea[1], "%Y.%m.%d %H:%M")
        print(title)
        with open(self.filename1,'a',encoding='utf-8') as target:
            target.write(title)
            target.write(timea[0])
            target.write(timea[1]+'\n')
        with open(self.filename2 ,'a',encoding='utf-8') as target:
            if self.date > time_b and self.date < time_e :
                for i in self.des:
                    if(title.find(i)>=0):
                        target.write(response.meta['url']+'\n')
                        return


        


