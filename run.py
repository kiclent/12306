# -*- coding=utf-8 -*-
from config.emailConf import sendEmail
from init import select_ticket_info


def run():
    select_ticket_info.select().main()


def Email():
    sendEmail(u"订票结束，请在浏览器登陆12306网站查看待支付订单.")


if __name__ == '__main__':
    run()
    Email()
