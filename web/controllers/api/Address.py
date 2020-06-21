import json

from flask import request, jsonify, g

from application import db
from common.models.member.MemberAddress import MemberAddress
from common.models.member.MemberComments import MemberComment
from web.controllers.api import route_api
from common.models.food.Food import Food
from common.models.pay.PayOrder import PayOrder
from common.models.pay.PayOrderItem import PayOrderItem

from common.libs.Helper import selectFilterObj, getDictFilterField, getCurrentDate
from common.libs.UrlManager import UrlManager


@route_api.route('/my/address/set',methods=['POST'])
def myAddressSet():
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    member_info = g.member_info
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    address = req['address'] if 'address' in req else ''

    province_str = req['province_str'] if 'province_str' in req else ''
    city_str = req['city_str'] if 'city_str' in req else ''
    district_str = req['district_str'] if 'district_str' in req else ''

    province_id = int(req['province_id']) if ('province_id' in req and req['province_id']) else 0
    city_id = int(req['city_id']) if ('city_id' in req and req['city_id']) else 0
    district_id = int(req['district_id']) if ('district_id' in req and req['district_id']) else 0

    member_info = g.member_info

    if not nickname:
        resp['code'] = -1
        resp['msg'] = "请填写联系人姓名~~"
        return jsonify(resp)

    if not mobile:
        resp['code'] = -1
        resp['msg'] = "请填写手机号码~~"
        return jsonify(resp)

    if province_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择地区~~"
        return jsonify(resp)

    if city_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择地区~~"
        return jsonify(resp)

    if district_id < 1:
        district_str = ''

    if not address:
        resp['code'] = -1
        resp['msg'] = "请填写详细地址~~"
        return jsonify(resp)

    if not member_info:
        resp['code'] = -1
        resp['msg'] = "系统繁忙，请稍后再试~~"
        return jsonify(resp)

    address_info = MemberAddress.query.filter_by(id=id, member_id=member_info.id).first()
    if address_info:
        model_address = address_info
    else:
        default_address_count = MemberAddress.query.filter_by(is_default=1, member_id=member_info.id, status=1).count()
        model_address = MemberAddress()
        model_address.member_id = member_info.id
        model_address.is_default = 1 if default_address_count == 0 else 0
        model_address.created_time = getCurrentDate()

    model_address.nickname = nickname
    model_address.mobile = mobile
    model_address.address = address
    model_address.province_id = province_id
    model_address.province_str = province_str
    model_address.city_id = city_id
    model_address.city_str = city_str
    model_address.area_id = district_id
    model_address.area_str = district_str
    model_address.updated_time = getCurrentDate()
    db.session.add(model_address)
    db.session.commit()

    return jsonify(resp)

