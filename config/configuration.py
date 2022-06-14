#配置浏览器
from jinja2 import pass_eval_context


driver_type = "chrome"

def driver():
    if driver_type == "Chrome":
        pass
    elif driver_type == "Firefox":
        pass




#配置地址
def test_url():
    return "http://avengers.wandianzhang.com"



if __name__ == 'main':
    url = test_url()