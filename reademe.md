## 启动 - 单进程
* export ops_config=local|production && pytho manager.py runserver

##flask-sqlacodegen
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask

## 安装git clone到服务器

## 创建目录

## 启动uwsgi - 多进程
    uwsgi --ini uwsgi.ini
    
## 配置NGINX
nginx_order.conf

## 配置HTTPS
