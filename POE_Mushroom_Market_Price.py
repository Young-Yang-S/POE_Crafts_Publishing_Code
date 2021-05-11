# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:57:50 2021

@author: daiya
"""

############################################################


#import required packages

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import socket
from selenium.webdriver.support.ui import Select
import re

############################################################



# Define the initial category


category = [
        '给物品移除一个随机非施法词缀，再给它添加一个新施法词缀（简称：非施法）',
        '用一个新施法词缀增幅魔法或稀有物品（简称：施法E）',
        '给物品移除一个随机施法词缀（简称：移除施法）',
        '给物品移除一个随机施法词缀，再给它添加一个新施法词缀（简称：施法置换）',
        '给物品移除一个随机非物理词缀，再给它添加一个新物理词缀（简称：非物理）',
        '用一个新物理词缀增幅一个魔法或稀有物品（简称：物理E）',
        '给物品移除一个随机物理词缀（简称：移除物理）',
        '给物品移除一个随机物理词缀，再给它添加一个新物理词缀（简称：物理置换）',
        '给物品移除一个随机非火焰词缀，再给它添加一个新火焰词缀（简称：非火焰）',
        '用一个新火焰词缀增幅一个魔法或稀有物品（简称：火焰E）',
        '给物品移除一个随机火焰词缀（简称：移除火焰）',
        '给物品移除一个随机火焰词缀，再给它添加一个新火焰词缀（简称：火焰置换）',
        '重铸一个稀有物品，保留所有前缀（简称：锁前洗后）',
        '重铸一个稀有物品，保留所有后缀（简称：锁后洗前）',
        '给物品移除一个随机非速度词缀，再给它添加一个新速度词缀（简称：非速度）',
        '用一个新速度词缀增幅一个物品（简称：速度E）',
        '给物品移除一个随机速度词缀（简称：移除速度）',
        '给物品移除一个随机速度词缀，再给它添加一个新速度词缀（简称：速度置换）',
        '给物品移除一个随机非影响效果词缀，再给它添加一个新影响效果词缀（简称：非势力）',
        '用一个新影响效果词缀增幅一个物品（简称：势力词缀增幅）',
        '给物品移除一个随机影响效果词缀（简称：移除势力）',
        '给物品移除一个随机影响效果词缀，再给它添加一个新影响效果词缀（简称：势力置换）',
        '给稀有物品重铸新随机词缀，其中包括一个影响效果词缀。影响效果词缀更常见（简称：强化势力C）',
        '使物品变为六个插槽（简称：6孔）',
        '给物品移除一个随机非攻击词缀，再给它添加一个新攻击词缀（简称：非攻击）',
        '用一个新攻击词缀增幅一个物品（简称：攻击E）',
        '给物品移除一个随机攻击词缀（简称：移除攻击）',
        '给物品移除一个随机攻击，再给它添加一个新攻击词缀（简称：攻击置换）',
        '给物品移除一个随机非冰霜词缀，再给它添加一个新冰霜词缀（简称：非冰霜）',
        '用一个新冰霜词缀增幅一个物品（简称：冰霜E）',
        '给物品移除一个随机冰霜词缀（简称：移除冰霜）',
        '给物品移除一个随机冰霜词缀，再给它添加一个新冰霜词缀（简称：冰霜置换）',
        '给物品移除一个随机非生命词缀，再给它添加一个新生命词缀（简称：非生命）',
        '用一个新生命词缀增幅一个物品（简称：生命E）',
        '给物品移除一个随机生命词缀（简称：移除生命）',
        '给物品移除一个随机生命词缀，再给它添加一个新生命词缀（简称：生命置换）',
        '给物品移除一个随机非暴击词缀，再给它添加一个新暴击词缀（简称：非暴击）',
        '用一个新暴击词缀增幅一个物品（简称：暴击E）',
        '给物品移除一个随机暴击词缀（简称：移除暴击）',
        '给物品移除一个随机暴击词缀，再给它添加一个新暴击词缀（简称：暴击置换）',
        '用一个随机忆境基底合成物品。不能用于传奇物品、影响效果物品、虚空忆境物品、分裂过的物品（简称：忆境化装备，添加1-3基底）',
        '给物品移除一个随机非防御词缀，再给它添加一个新防御词缀（简称：非防御）',
        '用一个新防御词缀增幅一个物品（简称：防御E）',
        '给物品移除一个随机防御词缀（简称：防御移除）',
        '给物品移除一个随机防御词缀，再给它添加一个新防御词缀（简称：防御置换）',
        '给物品移除一个随机非闪电词缀，再给它添加一个新闪电词缀（简称：非闪电）',
        '用一个新闪电词缀增幅一个物品（简称：闪电E）',
        '给物品移除一个随机闪电词缀（简称：移除闪电）',
        '给物品移除一个随机闪电词缀，再给它添加一个新闪电词缀（简称：闪电置换）',
        '给物品移除一个随机非混沌词缀，再给它添加一个新混沌词缀（简称：非混沌）',
        '用一个新混沌词缀增幅一个物品（简称：混沌E）',
        '给物品移除一个随机混沌词缀（简称：移除混沌）',
        '给物品移除一个随机混沌词缀，再给它添加一个新混沌词缀（简称：混沌置换）',
        '分裂物品上一个随机词缀，将其锁定。该物品至少要有 5 词缀才可分裂，无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品（简称：分裂5词缀）',
        '分裂物品的一个随机后缀。该物品至少要有 3 个后缀才可分裂。无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品（简称：分裂3后）',
        '分裂物品的一个随机前缀。该物品至少要有 3 个前缀才可分裂。无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品（简称：分裂3前）'
        ]

category2 = category

category3 = []
for i in category2:
    i = i.replace('（', '(')
    i = i.replace('）', ')')
    category3 .append(i)
    
    
    
number_list = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13
               ,13.5,14,14.5,15]


input_dictionary = {'fsf':'给物品移除一个随机非施法词缀，再给它添加一个新施法词缀(简称：非施法)',
 'sfe':'用一个新施法词缀增幅魔法或稀有物品(简称：施法E)',
 'ysf':'给物品移除一个随机施法词缀(简称：移除施法)',
 'sfz':'给物品移除一个随机施法词缀，再给它添加一个新施法词缀(简称：施法置换)',
 'fwl':'给物品移除一个随机非物理词缀，再给它添加一个新物理词缀(简称：非物理)',
 'wle':'用一个新物理词缀增幅一个魔法或稀有物品(简称：物理E)',
 'ywl':'给物品移除一个随机物理词缀(简称：移除物理)',
 'wlz':'给物品移除一个随机物理词缀，再给它添加一个新物理词缀(简称：物理置换)',
 'fhy':'给物品移除一个随机非火焰词缀，再给它添加一个新火焰词缀(简称：非火焰)',
 'hye':'用一个新火焰词缀增幅一个魔法或稀有物品(简称：火焰E)',
 'yhy':'给物品移除一个随机火焰词缀(简称：移除火焰)',
 'hyz':'给物品移除一个随机火焰词缀，再给它添加一个新火焰词缀(简称：火焰置换)',
 'sq':'重铸一个稀有物品，保留所有前缀(简称：锁前洗后)',
 'sh':'重铸一个稀有物品，保留所有后缀(简称：锁后洗前)',
 'fsdu':'给物品移除一个随机非速度词缀，再给它添加一个新速度词缀(简称：非速度)',
 'sdue':'用一个新速度词缀增幅一个物品(简称：速度E)',
 'ysdu':'给物品移除一个随机速度词缀(简称：移除速度)',
 'sduz':'给物品移除一个随机速度词缀，再给它添加一个新速度词缀(简称：速度置换)',
 'fsl':'给物品移除一个随机非影响效果词缀，再给它添加一个新影响效果词缀(简称：非势力)',
 'sle':'用一个新影响效果词缀增幅一个物品(简称：势力词缀增幅)',
 'ysl':'给物品移除一个随机影响效果词缀(简称：移除势力)',
 'slz':'给物品移除一个随机影响效果词缀，再给它添加一个新影响效果词缀(简称：势力置换)',
 'slc':'给稀有物品重铸新随机词缀，其中包括一个影响效果词缀。影响效果词缀更常见(简称：强化势力C)',
 '6k':'使物品变为六个插槽(简称：6孔)',
 'fgj':'给物品移除一个随机非攻击词缀，再给它添加一个新攻击词缀(简称：非攻击)',
 'gje':'用一个新攻击词缀增幅一个物品(简称：攻击E)',
 'ygj':'给物品移除一个随机攻击词缀(简称：移除攻击)',
 'gjz':'给物品移除一个随机攻击，再给它添加一个新攻击词缀(简称：攻击置换)',
 'fbs':'给物品移除一个随机非冰霜词缀，再给它添加一个新冰霜词缀(简称：非冰霜)',
 'bse':'用一个新冰霜词缀增幅一个物品(简称：冰霜E)',
 'ybs':'给物品移除一个随机冰霜词缀(简称：移除冰霜)',
 'bsz':'给物品移除一个随机冰霜词缀，再给它添加一个新冰霜词缀(简称：冰霜置换)',
 'fsm':'给物品移除一个随机非生命词缀，再给它添加一个新生命词缀(简称：非生命)',
 'sme':'用一个新生命词缀增幅一个物品(简称：生命E)',
 'ysm':'给物品移除一个随机生命词缀(简称：移除生命)',
 'smz':'给物品移除一个随机生命词缀，再给它添加一个新生命词缀(简称：生命置换)',
 'fbj':'给物品移除一个随机非暴击词缀，再给它添加一个新暴击词缀(简称：非暴击)',
 'bje':'用一个新暴击词缀增幅一个物品(简称：暴击E)',
 'ybj':'给物品移除一个随机暴击词缀(简称：移除暴击)',
 'bjz':'给物品移除一个随机暴击词缀，再给它添加一个新暴击词缀(简称：暴击置换)',
 'yj':'用一个随机忆境基底合成物品。不能用于传奇物品、影响效果物品、虚空忆境物品、分裂过的物品(简称：忆境化装备，添加1-3基底)',
 'ffy':'给物品移除一个随机非防御词缀，再给它添加一个新防御词缀(简称：非防御)',
 'fye':'用一个新防御词缀增幅一个物品(简称：防御E)',
 'yfy':'给物品移除一个随机防御词缀(简称：防御移除)',
 'fyz':'给物品移除一个随机防御词缀，再给它添加一个新防御词缀(简称：防御置换)',
 'fsdi':'给物品移除一个随机非闪电词缀，再给它添加一个新闪电词缀(简称：非闪电)',
 'sdie':'用一个新闪电词缀增幅一个物品(简称：闪电E)',
 'ysdi':'给物品移除一个随机闪电词缀(简称：移除闪电)',
 'sdiz':'给物品移除一个随机闪电词缀，再给它添加一个新闪电词缀(简称：闪电置换)',
 'fhd':'给物品移除一个随机非混沌词缀，再给它添加一个新混沌词缀(简称：非混沌)',
 'hde':'用一个新混沌词缀增幅一个物品(简称：混沌E)',
 'yhd':'给物品移除一个随机混沌词缀(简称：移除混沌)',
 'hdz':'给物品移除一个随机混沌词缀，再给它添加一个新混沌词缀(简称：混沌置换)',
 'flw':'分裂物品上一个随机词缀，将其锁定。该物品至少要有 5 词缀才可分裂，无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品(简称：分裂5词缀)',
 'flsh':'分裂物品的一个随机后缀。该物品至少要有 3 个后缀才可分裂。无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品(简称：分裂3后)',
 'flsq':'分裂物品的一个随机前缀。该物品至少要有 3 个前缀才可分裂。无法用于有影响效果的物品、虚空忆境物品，或者分裂过的物品(简称：分裂3前)'}


####################################################################

# define the functions 

"""
(1) get price  is to get the recent average price of items in category, the set of price follows
certain rules. Firstly I get the lowest price within the recent 1 hour. Then if the percentage of 
number of sellers with the lowest price is more than 50%, then I set the price is equal to 
lowest price - 0.5 exalted orb. Otherwise, set it as the lowest price as the price made by other sellers.
If the price can't be found within 1 hour, then search the price within 5 hours.
"""

def getprice():
    # switch to window is to switch between different tags 
    driver.switch_to.window(driver.window_handles[0])
    
    Final_price_list = pd.DataFrame(columns=['Name','Price','Number_Seller', 'Note'])
    
    
    # this is to use the select method to select the 大区 in the page. 
    for k in category:
        
        selector = Select(driver.find_element_by_xpath('//*[@id="league"]'))
        
        selector.select_by_visible_text("永久区") 
        
        
        selector = Select(driver.find_element_by_xpath('//*[@id="garden"]'))
        
        selector.select_by_visible_text(k) 
        
        
        driver.find_element_by_class_name('btn-search').click()
        
        
    # this webdriverwait is important to know because it is a way to completely know the page has been successfully loaded
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "td-shelves-time")))            
        except:
              real_name = k
              short_name = real_name.split('：')[1][:-1] 
              value = None
              note = 'No Price'
              number_seller = 0
              data = [[short_name, value,number_seller, note]]
              tmp = pd.DataFrame(data=data, columns=['Name','Price','Number_Seller','Note'])
              Final_price_list = Final_price_list.append(tmp)
              continue
            
            
        # get the all the prices within 1 hour
        
        items = driver.find_elements_by_class_name('td-shelves-time')
        
        
        price_number = []
        for i in range(0,50):
            try:
                 texx = driver.find_element_by_xpath('//*[@id="tGarden"]/tbody/tr[{}]/td[3]'.format(i)).text
                 price_number.append(texx)
            except:
                True
                
        
        price = driver.find_elements_by_class_name('icon-currency')
        
        
        
        price_list = []
        
        note = ''
        value = 100
        
        
        for i in range(0,len(items)):
            temp= items[i].text.split('\n')
            if re.search('秒前', temp[0]) or re.search('刚刚', temp[0]):
                if  price[i].get_attribute("title") == '崇高石':
                    text = price_number[i] + ' 崇高石'
                    price_list.append(text)
                elif price[i].get_attribute("title") == '混沌石':
                    text = str(int(price_number[i])/120) + ' 崇高石'
                    price_list.append(text)
                else:
                    True
                
            elif re.search('分钟前', temp[0]):
                try:
                    judge = int(items[i].text.split('\n')[0].split(' ')[0])
                    if judge < 59:
                        if  price[i].get_attribute("title") == '崇高石':
                            text = price_number[i] + ' 崇高石'
                            price_list.append(text)
                        elif price[i].get_attribute("title") == '混沌石':
                            text = str(int(price_number[i])/120) + ' 崇高石'
                            price_list.append(text)
                        else:
                            True
                    else:
                        True
                except:
                    True
            
            else:
                True
                
        
            
            # this is to remove some wrong prices, it is not a serious way to do it, which can 
            # be improved
            
            for kj in price_list:
                temp = float(kj.split(" ")[0])
                if temp < 0.2 or temp > 20:
                    price_list.remove(kj)
                
        
            # this is to get the price I need to sell
            number_seller = len(price_list)
            
            if number_seller !=0:
            
                price_list_number = []
                
                for kk in price_list:
                    temp = float(kk.split(" ")[0])
                    price_list_number.append(temp)
                    
                 
                minin = 10000
                for g in price_list_number:
                    if g < minin:
                        minin = g
                 
                
                count1 = 0
                if number_seller >=3:
                    for gg in price_list_number:
                        if gg == minin:
                            count1 +=1
                    
                    percent1 = count1/number_seller
                
                    if percent1 > 0.5 :
                        value = minin - 0.5
                        if value < 0.3:
                            value = minin
                
                    else:
                        value = minin
                    
                else:
                     value = minin
                            
        # If the price can't be found within 1 hour, then get the price within 5 hours   
        if number_seller == 0:
            for i in range(0,len(items)):
                temp= items[i].text.split('\n')
                if re.search('小时前', temp[0]) :
                    try:
                        judge = int(items[i].text.split('\n')[0].split(' ')[0])
                        if judge < 5:
                            if  price[i].get_attribute("title") == '崇高石':
                                text = price_number[i] + ' 崇高石'
                                price_list.append(text)
                            elif price[i].get_attribute("title") == '混沌石':
                                text = str(int(price_number[i])/120) + ' 崇高石'
                                price_list.append(text)
                            else:
                                True
                        else:
                            True
                    except:
                        True
                    
            
            for kj in price_list:
                temp = float(kj.split(" ")[0])
                if temp < 0.2 or temp > 20:
                    price_list.remove(temp)
                
            
            
            number_seller = len(price_list)
            
            if number_seller !=0:
                price_list_number = []
                
                for kk in price_list:
                    temp = float(kk.split(" ")[0])
                    price_list_number.append(temp)
                    
                 
                minin = 10000
                for g in price_list_number:
                    if g < minin:
                        minin = g
                 
                
                count1 = 0
                if number_seller >=5:
                    for gg in price_list_number:
                        if gg == minin:
                            count1 +=1
                    
                    percent1 = count1/number_seller
                
                    if percent1 > 0.5 :
                        value = minin - 0.5
                        if value < 0.333:
                            value = minin
                
                    else:
                        value = minin
                    
                else:
                     value = minin
            
            note = 'Price within recent 5 hours'
                            
        
        if number_seller == 0:
            value = None
            note = 'No Price'
            
        
        real_name = k
        
        short_name = real_name.split('：')[1][:-1] 
        
        print(value)
        data = [[short_name, value,number_seller, note]]
        tmp = pd.DataFrame(data=data, columns=['Name','Price','Number_Seller','Note'])
        Final_price_list = Final_price_list.append(tmp)   
        
    return Final_price_list 



# this is to get the price for the crafts you want to sell
def get_price(key1):
    location = list(input_dictionary).index(key1)
    price = Final_price_list.iloc[location,1]
    return price
    

# this is to publish the crafts 
    
def publish(info,price):
    
    driver.switch_to.window(driver.window_handles[1])
    
    
    selector = Select(driver.find_element_by_xpath('//*[@id="league"]'))
        
    selector.select_by_visible_text("永久区") 
        
        
    selector = Select(driver.find_element_by_xpath('//*[@id="garden"]'))
        
    selector.select_by_visible_text(info) 
    
    l = driver.find_element_by_xpath('//*[@id="frmMain"]/div[3]/div[2]/input')

    l.clear()
    
    if price in number_list: 
        
        l.send_keys(str(price))
    
        selector = Select(driver.find_element_by_xpath('//*[@id="unit"]'))
        
        selector.select_by_visible_text("崇高石") 
    
        l2 = driver.find_element_by_xpath('//*[@id="frmMain"]/div[4]/div[1]/div[2]/input')

        l2.clear()
        
        l2.send_keys('100')
        
        
        driver.find_element_by_xpath(' //*[@id="frmMain"]/div[5]/input').click()
    

    else:
        price = int(price* 120)
        
        price = price//10 *10
        
        l.send_keys(str(price))
    
        selector = Select(driver.find_element_by_xpath('//*[@id="unit"]'))
        
        selector.select_by_visible_text("混沌石") 
    
        l2 = driver.find_element_by_xpath('//*[@id="frmMain"]/div[4]/div[1]/div[2]/input')
        
        l2.clear()
        
        l2.send_keys('100')
        
        
        driver.find_element_by_xpath(' //*[@id="frmMain"]/div[5]/input').click()
    
    

############################################################
        
"""
Main Part: Before running the code, we shoud start the chrome and open three tabs, main page of crafts
, publish crafts page, my crafts and the sequence of tabs should follow the above sequence.
"""      
        
# start the chrome 

# chrome.exe --remote-debugging-port=9555 --user-data-dir="C:\selenum_1\AutomationProfile


socket.setdefaulttimeout(150)  # set the max loading time 30
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9555")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver11.exe"
chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")    
driver = webdriver.Chrome(chrome_driver,  chrome_options=chrome_options)
agent = driver.execute_script("return navigator.userAgent")     


link = 'https://www.caimogu.net/poe/garden.html'
driver.get(link)


# this is the link for the publish of crafts
# https://www.caimogu.net/poe/garden/publish.html?from=index


######################################################################
  

# Then we can run the code and PUBLISH our crafts， we just need to change the x value to the crafts
# we want to sell, and then run it, we can publish it in the fastast way.


# This function is to get the price list of crafts, we can run it per hour. It would take 3-5 mins to complete

Final_price_list = getprice()


# This is the most important part, we just need to revise the value of x and then everything done.

x = 'fgj'

price = get_price(x)

info = input_dictionary[x]

publish(info,price)


driver.minimize_window()


# this craft publishing code is only an easy version, anyone who is interested in it and make many changes, like how we set price for crafts, which kind of rules we should follow, and 
# this code doesn't include the procedure of removing the crafts that you have sold, but it is important and easy to have, anyone who is interested in it can have try.

# Have fun with poe and do something good analysis or play some funny games on it!!!!!!!!!
