SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME= "mooc_food"

#过滤URL
IGNORE_URLS = [
    "^/user/login",
]

API_IGNORE_URLS = [
    '^/api'
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

PAGE_SIZE = 10 #每页多少条

PAGE_DISPLAY = 10

STATUS_MAPPING = {
    '1':'正常',
    '0':'已删除'
}

MINA_APP = {
    'appid':'wx08ccaf894d8554b9',
    'appkey':'81418753fba4fbd2ff5e92324e756538', #注意隐蔽
    'paykey':'',
    'mch_id':'1443337302',
    'callback_url':'/api/order/callback'
}

UPLOAD = {
    'ext':['jpg','gif','bmp','jpeg','png'],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://10.211.55.4:8999'
}

PAY_STATUS_DISPLAY_MAPPING = {
    "-8":"待付款",
    "-7":"待发货",
    "-6":"待收货",
    "-5":"待评价",
    "1":"已完成",
    "0":"已关闭"
}
