import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os,sys,re


def save_pic():
    scr_str = time.time()

    time_str = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(scr_str))
    #print(time_str)
    browser.get_screenshot_as_file(time_str+".png")

    
browser = webdriver.Chrome()


url = "https://cgifederal.secure.force.com"
#url = "https://blog.csdn.net/weixin_41917563/article/details/80189337"
browser.get(url)

#save_pic()
#browser.get_screenshot_as_file("test.png")


#By.XPATH

#browser.find_element(By.XPATH("//div[contains(text(),'modifyFilterTest002')]")).click();
#browser.find_element(By.XPATH("//a[contains(text(),'新用户')]")).click();
#browser.find_element(By.XPATH("//a[text()='隐私政策']")).click();

#browser.find_element(By.XPATH("//a[text='aaa']"))
#browser.find_element(By.XPATH("//*[contains(text(),'隐私政策')]")) TypeError: 'str' object is not callable

#.click()
#browser.find_element(By.XPATH,'//*[@id="kw"]')
order = input('输入操作关键词:')

'''
#第一次跳转
browser.find_element_by_xpath("//a[contains(text(),'查询预约')]").click()
time.sleep(3)
Reschedule
browser.find_element_by_xpath("//a[contains(text(),'查询预约')]").click()
'''
while True:
    
    if order=='click':
        browser.find_element_by_xpath("//a[contains(text(),'查询预约')]").click()
    time.sleep(120)
    #关闭x
    #ui-dialog-title-reschedule-form
    #//a[@id='3']/following-sibling::a[1]
    #生成图片
    #save_pic()
    #点击选择重新预约时间
    #j_id0:SiteTemplate:j_id231:j_id235:0
    #获取时间标签内容,匹配最近时间的日期
    str_date = browser.find_element_by_xpath("//label[@for='j_id0:SiteTemplate:j_id231:j_id235:0']").text
    print('默认时间：',str_date)
    #pat = 'August (.*), 2019'
    #pat = 'July (.*), 2019'
    #pat1 = 'July (.*), 2019'
    #pat2 = 'August (.*), 2019'
    '''
    res = re.search(pat1,str_date)
    if res:
        pat = pat1
    else:
        pat = pat2
    '''
    #pat = ' August 14,'
    pat = ' ([a-zA-Z]*) ([0-9]*),'
    res = re.compile(pat).findall(str_date)

    scr_str = time.time()
    time_str = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(scr_str))
    
    print('date is : ',res , ' time is : ', time_str)

    #点击第一个时间选项
    browser.find_element_by_xpath("//input[@id='j_id0:SiteTemplate:j_id231:j_id235:0']").click()
    time.sleep(0.5)
    #点击关闭按钮
    browser.find_element_by_xpath("//span[@id='ui-dialog-title-reschedule-form']/following-sibling::a[1]").click()
    time.sleep(120)


