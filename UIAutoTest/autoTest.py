from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] ='10'
desired_caps['deviceName'] ='1'
desired_caps['appPackage'] ='com.lingan.seeyou'
desired_caps['appActivity'] ='.ui.activity.main.SeeyouActivity'
#针对send_keys输入中文无效的解决方法
desired_caps['unicodekeyboard'] = True
desired_caps['resetkeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(3)

#输出页面含有’码‘的元素
mas = driver.find_elements(by=By.XPATH,value="//*[contains(@text,'码')]")

print(len(mas))
for ma in mas:
    print(ma.text)

# #切换密码登录
# driver.find_element(by=By.ID, value="com.lingan.seeyou:id/login_et_password_click").click()
#输入手机号
driver.find_element(by=By.CLASS_NAME,value="android.widget.EditText").send_keys('15619222222')
#清空输入的内容
driver.find_element(by=By.CLASS_NAME,value="android.widget.EditText").clear()
# #输入密码
# driver.find_element(by=By.XPATH,value="//*[@text='请填写美柚密码']").send_keys('a123456')
# #勾选隐私协议
# driver.find_element(by=By.CLASS_NAME,value="android.widget.CheckBox").click()
# #点击登录
# driver.find_element(by=By.CLASS_NAME,value="android.widget.Button").click()

#等待
#隐式等待-- 所有元素等待时间相同  在设定时间范围内 找到即进行后续操作 未找到报错
# driver.implicitly_wait(200)
# driver.find_element(by=By.CLASS_NAME,value="android.widget.Button").click()

#显式等待
wait = WebDriverWait(driver,25,5) #25s范围内 每5s执行一次
wait.until(lambda x:x.find_element(by=By.CLASS_NAME,value="android.widget.Button")).click()

#获取元素文本内容  .text方法
#获取元素位置和大小  .location   .size
login_button = driver.find_element(by=By.CLASS_NAME,value="android.widget.Button")
print(login_button.location)
print(login_button.location['x'])
print(login_button.size)
print(login_button.sise['width'])


#根据属性名获取元素的属性值 element.get_attribute(value)
mas = driver.find_elements(by=By.XPATH,value="//*[contains(@text,'码')]")
print(len(mas))
for ma in mas:
    print(ma.get_attribute('enabled'))
    print(ma.get_attribute('clickable'))
    print(ma.get_attribute('text'))
    print(ma.get_attribute('resourceId'))   #特殊 实际为resource-id
    print(ma.get_attribute('className'))    #特殊 实际为class
    print(ma.get_attribute('name'))    #特殊 实际为content-desc  除了三个特殊的 其他都可参考uiautomator viewer中的属性名


time.sleep(5)
driver.quit()