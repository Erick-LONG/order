var app = getApp();
Page({
    data: {
        statusType: ["待付款", "待发货", "待收货", "待评价", "已完成", "已关闭"],
        status: ["-8", "-7", "-6", "-5", "1", "0"],
        currentType: 0,
        tabClass: ["", "", "", "", "", ""]
    },
    statusTap: function (e) {
        var curType = e.currentTarget.dataset.index;
        this.data.currentType = curType;
        this.setData({
            currentType: curType
        });
        this.onShow();
    },
    orderDetail: function (e) {
        wx.navigateTo({
            url: "/pages/my/order_info?order_sn=" + e.currentTarget.dataset.id
        })
    },
    onShow: function () {
        var that = this;
        this.getPayOrder();
    },
    getPayOrder: function () {
        var that = this;
        wx.request({
            url: app.buildUrl('/my/order'),
            header: app.getRequestHeader(),
            data: {
                status: that.data.status[that.data.currentType]
            },
            success: function (res) {
                var resp = res.data;
                if (resp.code != 200) {
                    app.alert({'content': resp.msg});
                    return;
                }

                that.setData({
                    order_list: resp.data.pay_order_list
                })
            }

        })

    },
    toPay: function (e) {
        var that = this;
        wx.request({
            url: app.buildUrl('/order/pay'),
            header: app.getRequestHeader(),
            method: 'POST',
            data: {
                order_sn: e.currentTarget.dataset.id
            },
            success: function (res) {
                var resp = res.data;
                if (resp.code != 200) {
                    app.alert({'content': resp.msg});
                    return;
                }
                var pay_info = resp.data.pay_info;
                wx.requestPayment({
                    'timeStamp': pay_info.timeStamp,
                    'nonceStr': pay_info.nonceStr,
                    'package': pay_info.package,
                    'signType': 'MD5',
                    'paySign': pay_info.paySign,
                    'success': function (res) {

                    },
                    'fail': function (res) {

                    }
                })

            }

        })
    },
    orderCancel: function (e) {
        this.orderOps(e.currentTarget.dataset.id, 'cancel', '确认取消订单？')
    },
    orderConfirm: function (e) {
        this.orderOps(e.currentTarget.dataset.id, 'confirm', '确认收到货了吗？')
    },
    orderComment: function (e) {
        wx.navigateTo({
            url:'/pages/my/comment?order_sn='+e.currentTarget.dataset.id
        });
    },
    orderOps: function (order_sn, act, msg) {
        var that = this;
        var params = {
            'content': msg,
            'cb_confirm': function () {
                wx.request({
                    url: app.buildUrl('/order/ops'),
                    header: app.getRequestHeader(),
                    method: 'POST',
                    data: {
                        order_sn: order_sn,
                        act: act
                    },
                    success: function (res) {
                        var resp = res.data;
                        app.alert({'content': resp.msg});
                        if (resp.code != 200) {
                            that.getPayOrder();
                            return;
                        }
                    }
                })
            }
        };
        app.tip(params);
    }
});
