import selenium.webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from zheye import zheye

def shibie():
    z = zheye()  # 实例化对象
    positions = z.Recognize(r'./yanzhengma.png')  # 将验证码本地路径传入Recognize方法识别，返回倒立图片的坐标
    print(positions)  # 默认倒立文字的y坐标在前，x坐标在后
    # 知乎网要求的倒立文字坐标是x轴在前，y轴在后，所以我们需要定义一个列表来改变默认的，倒立文字坐标位置
    pos_arr = []
    if len(positions) == 2:
        if positions[0][1] > positions[1][1]:  # 判断列表里第一个元祖里的第二个元素如果大于,第二个元祖里的第二个元素
            pos_arr.append([positions[1][1], positions[1][0]])
            pos_arr.append([positions[0][1], positions[0][0]])
        else:
            pos_arr.append([positions[0][1], positions[0][0]])
            pos_arr.append([positions[1][1], positions[1][0]])
    else:
        pos_arr.append([positions[0][1], positions[0][0]])
    return pos_arr
if __name__ == '__main__':

    driver=selenium.webdriver.Firefox()
    driver.get("https://www.zhihu.com/#signin")
    driver.find_element_by_class_name("signin-switch-password").click()
    driver.find_element_by_name("account").send_keys("15759101796")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("chen19931107")
    time.sleep(2)
    img=driver.find_element_by_tag_name("img")
    img.screenshot("yanzhengma.png")
    time.sleep(3)
    result=shibie()
    action=ActionChains(driver)
    if len(result)==1:
        action.move_to_element_with_offset(driver.find_element_by_class_name("Captcha-image"),result[0][0],result[0][1]).click().perform()
    else:
        action.move_to_element_with_offset(driver.find_element_by_class_name("Captcha-image"), result[0][0],
                                           result[0][1]).click().perform()
        action = ActionChains(driver)
        action.move_to_element_with_offset(driver.find_element_by_class_name("Captcha-image"), result[1][0],
                                           result[1][1]).click().perform()
    time.sleep(2)
    driver.find_element_by_class_name("sign-button").click()


