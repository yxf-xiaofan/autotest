import sys
sys.path.append("C:\\Users\\fanhao\\Desktop\\auto\\autotest\\configuration.py")




#配置浏览器
driver_type = "chrome"

#配置地址
def test_url():
    return "http://avengers.wandianzhang.com"



if __name__ == 'main':
    url = test_url()