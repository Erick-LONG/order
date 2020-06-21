import datetime
from common.models.pay.PayOrder import PayOrder
from application import app,db
from common.libs.pay.PayService import PayService
'''
python manager.py runjob -m pay/index
'''


class JobTask():
    def __init__(self):
        pass

    def run(self):
        now = datetime.datetime.now()
        date_before_30min = now + datetime.timedelta(minutes=-30)
        list = PayOrder.query.filter_by(status=-8)\
            .filter(PayOrder.created_time <= date_before_30min.strftime('%Y-%m-%d %H:%M:%S')).all()
        if not list:
            return

        pay_target = PayService()
        for item in list:
            pay_target.closeOrder(pay_order_id= item.id)


