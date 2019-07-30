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
#url = "file:///D:/Python37-32/exe/canlendar.html"
#url = "https://blog.csdn.net/weixin_41917563/article/details/80189337"
browser.get(url)

'''
cookies = browser.get_cookies()
print(cookies)
utmb = browser.get_cookie('__utmb')

utmt = browser.get_cookie('__utmt')

print('utmb is ：',utmb, 'utmt is ：',utmt)
'''
#此处测试cookies
'''
import requests
input('登录?')
cookieJar = requests.cookies.RequestsCookieJar()
print(cookieJar)

while True:
    input('查看cookie:')
    cookies = browser.get_cookies()
    print(cookies)


    utmb = browser.get_cookie('__utmb')

    utmt = browser.get_cookie('__utmt')

    print('utmb is ：',utmb, 'utmt is ：',utmt)

time.sleep(50)

input('是否退出？')
browser.quit()
'''
#save_pic()
#time.sleep(3)
#browser.find_element_by_xpath('//input[@type="checkbox"]').click()
'''
text_c = browser.find_element_by_xpath('//input[@id="thePage:SiteTemplate:theForm:addItem"]').get_attribute('value')
print(text_c)
input('刷新')
'''
s_time = input('开始时间：')
e_time = input('结束时间：')

s_list = s_time.split(',')
e_list = e_time.split(',')

#开始时间月份、日期，结束时间月份、日期
start_m,start_d = s_list
end_m,end_d = e_list
#开始时间：start_m, start_d,结束时间：end_m, end_d
start_m = int(start_m)
start_d = int(start_d)

end_m = int(end_m)
end_d = int(end_d)
month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

'''
default_t = browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[1]/div/div/span[1]').text
time_t = browser.find_element_by_xpath('//a[contains(@class, "ui-state-active")]').text
print('默认月份：',default_t,'默认日期：',time_t)
'''
while True:
    try:
        time.sleep(5)
        default_date_str = browser.find_element_by_xpath('//*[@id="myCalendarTable"]/tbody/tr[2]/td[3]').text
        
    except Exception as e:
        time.sleep(10)
        browser.quit()

    print('默认时间：',default_date_str)
            
    #正则匹配默认时间
    pat = ' ([a-zA-Z]*) ([0-9]*),'
    res = re.compile(pat).findall(default_date_str)

    month_num = month_list.index(res[0][0])+1
    day_num = int(res[0][1])

    #判断日期是否在输入的时间范围内
    flag = False
    if month_num >= start_m and month_num <= end_m:
        flag = True
        if month_num == start_m:
            if day_num < start_d:
                flag = False
                print('不在范围内，小于开始时间')
                #小于开始时间，需要拿更多的时间去匹配时间段
        if month_num == end_m:
            if day_num > end_d:
                flag = False
                print('不在范围内，大于结束时间')
        
    if flag:
        print('时间符合！')
        break
    else:
        print('时间不符合！')
        #time.sleep(20)
        '''
        #//*[@id="datepicker"]/div/div[1]/table/tbody/tr[3]/td[5]/span
        try:
            browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[1]/table/tbody/descendant::a[2]').click()
            print(' a12 is clicked ! ')
            get_num = browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[1]/table/tbody/descendant::a[2]').text
            if get_num == '18':
                #提交预约
                browser.find_element_by_xpath('//input[@type="checkbox"]').click()

                save_pic()

                time.sleep(0.3)
                           
                #如果满足条件，click
                browser.find_element_by_xpath('//input[@id="thePage:SiteTemplate:theForm:addItem"]').click()

                time.sleep(3)
                print('提交预约成功！')
                save_pic()
                time.sleep(15)

            time.sleep(28)
        except Exception as e:
            time.sleep(10)
            print('a12 e！')
        
        try:
            browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[1]/table/tbody/descendant::a[1]').click()
            print(' a11 is clicked ! ')
            time.sleep(29)
        except Exception as e:
            time.sleep(10)
            print('a11 e！')
        try:
            browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[2]/table/tbody/descendant::a[1]').click()
            print(' a21 is clicked ! ')
            time.sleep(26)
        except Exception as e:
            time.sleep(10)
            print('a21 e！')
        try:
            browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[3]/table/tbody/descendant::a[1]').click()
            print(' a31 is clicked ! ')
            time.sleep(27)
        except Exception as e:
            time.sleep(10)
            print('a31 e！')
        '''
        
        time.sleep(480)
        print('等待480s！')
        '''
        try:
            #browser.find_element_by_xpath('//a[contains(@class, "ui-state-active")]').click()
            browser.find_element_by_xpath('//*[@id="datepicker"]/div/div[1]/table/tbody/descendant::a[1]').click()
            time.sleep(35)
            print('等待35s，页面自动刷新！')
        except Exception as e:
            time.sleep(10)
            print('a1 e！')
        '''
        browser.refresh()
#提交预约
browser.find_element_by_xpath('//input[@type="checkbox"]').click()

save_pic()

time.sleep(0.3)
           
#如果满足条件，click
browser.find_element_by_xpath('//input[@id="thePage:SiteTemplate:theForm:addItem"]').click()

time.sleep(3)
print('提交预约成功！')
save_pic()
time.sleep(15)

input('ok?')
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

while True:
    
    if order=='click':
        browser.find_element_by_xpath("//a[contains(text(),'查询预约')]").click()
    time.sleep(60)
    #关闭x
    #ui-dialog-title-reschedule-form
    #//a[@id='3']/following-sibling::a[1]
    #生成图片
    save_pic()
    #点击选择重新预约时间
    #j_id0:SiteTemplate:j_id231:j_id235:0
    #获取时间标签内容,匹配最近时间的日期
    str_date = browser.find_element_by_xpath("//label[@for='j_id0:SiteTemplate:j_id231:j_id235:0']").text
    #pat = 'August (.*), 2019'
    #pat = 'July (.*), 2019'
    pat1 = 'July (.*), 2019'
    pat2 = 'August (.*), 2019'
    pat3 = 'September (.*), 2019'

    res1 = re.search(pat1,str_date)
    res2 = re.search(pat2,str_date)
    res3 = re.search(pat3,str_date)
    if res1:
        pat = pat1
    if res2:
        pat = pat2
    if res3:
        pat = pat3
    
    res = re.compile(pat).findall(str_date)

    scr_str = time.time()
    time_str = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(scr_str))
    
    print('date is : ',res[0],' pat is : ',pat,' time is : ',time_str)

    #如果符合期待日期，则选中
    #browser.find_element_by_xpath("//input[@id='j_id0:SiteTemplate:j_id231:j_id235:0']").click()
    time.sleep(0.5)
    #如果日期不符合，则关闭弹出窗口，否则提交日期重新预约
    #关闭弹出窗
    #browser.find_element_by_xpath("//span[@id='ui-dialog-title-reschedule-form']/following-sibling::a[1]").click()
    #提交日期修改预约
    #reschedule-form
    browser.find_element_by_xpath("//div[@id='reschedule-form']/following-sibling::div[1]/div/button[1]").click()
    time.sleep(100)
'''












