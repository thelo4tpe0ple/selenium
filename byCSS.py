#-*-encoding = utf8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
#import json
def LianjiaSpider():
    start_url = ["https://nj.lianjia.com/ershoufang"]
    #设置需要打开的页面数量
    num = 10
    #start_page = 1
    #print(start_url[0]+'/pg'+str(1))
    #for i in range(1,num):
        #初始化一个主页面驱动
    driver = webdriver.Chrome()
    #driver.get(start_url[0])
    driver.get(start_url[0]+'/pg2')
    #强制等待2秒，防止页面加载不出来
    driver.implicitly_wait(2)
    #获取子页面所有地址
    elements = driver.find_elements(By.CSS_SELECTOR," div.title > a[href]")
    for e in elements:
        #print(e.get_attribute('href'))
        addr =  e.get_attribute('href')
        sub_driver = webdriver.Chrome()
        sub_driver.get(addr)
        sub_driver.implicitly_wait(2)
        item = {'price':'','unitPrice':''}
        price = sub_driver.find_element(By.CSS_SELECTOR,"body > div.overview > div.content > div.price-container > div > span.total")
        item['price'] =price.text
        unitPrice = sub_driver.find_element(By.CSS_SELECTOR,"body > div.overview > div.content > div.price-container > div > div.text > div.unitPrice > span")
        item['unitPrice'] = unitPrice.text
        with open('data2.json', 'a',encoding='utf8') as file:
                # 写入一行文本
                #遍历字典，将value写入文件
            for value in item.values():
                file.write(value)
                file.write("  ")
            file.write("\n")
            #file.write('\n')
        #关闭子页面
        sub_driver.quit()
    driver.quit()
        #遍历地址集合
        # for element in elements:
        #     #获取子页面地址
        #     addr = element.get_attribute('href')
        #     #初始化一个子页面驱动
        #     sub_driver = webdriver.Chrome()
        #     #打开子页面
        #     sub_driver.get(addr)
        #     #强制等待3秒
        #     sub_driver.implicitly_wait(3)
        #     #设置需要爬取的数据字典
        #     item = {'title':'','price':'','unitPrice':'','cmtArea':'','cmtName':''}

        #     #根据XPath爬取子页面数据
        #     item['title']= str(sub_driver.title)
        #     price = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/span[1]')
        #     price =str(price.text)
        #     if price == None:
        #         item['price'] = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/span[1]')
        #     else:
        #         item['price'] = price + '万'
        #     unit_price = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span')
        #     unit_price=str(unit_price.text)
        #     #print(unit_price)
        #     if unit_price == '价格待定':
        #         item['unitPrice'] = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span')
        #     else:
        #         item['unitPrice'] = unit_price
        #     cmtArea = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[1]/a[1]').text
        #     item['cmtArea'] =str(cmtArea)
        #     cmtName = sub_driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[2]/span[2]').text
        #     item['cmtName'] = str(cmtName)
        #     #print(item)
        #     #数据存入json文件
        #     with open('data.json', 'a',encoding='utf8') as file:
        #         # 写入一行文本
        #         #遍历字典，将value写入文件
        #         for value in item.values():
        #             file.write(value)
        #             file.write("  ")
        #         file.write("\n")
        #         #file.write('\n')
            #关闭子页面
            # sub_driver.quit()

        
        #lk= element.get_attribute("href")
        #关闭主页面
    #driver.quit()
        

        

if __name__ == '__main__':
    LianjiaSpider()
    
        
        