#导入selenium webdriver包

from selenium import webdriver

#定义打开浏览器为谷歌

driver = webdriver.Chrome()

#最大化窗口

driver.maximize_window()

#打开百度

driver.get("https://www.baidu.com")

#打印百度窗口标题

print("本窗口标题为：%s"%driver.title)