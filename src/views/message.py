#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from ..utils.http import success
from src.tasks.email import send_welcome_email
from src.extensions import jsonrpc_message

bp = Blueprint('message', __name__)


@jsonrpc_message.method('MessageService.send_welcome_email')
def send_welcome_email(email):
    """
    发送欢迎邮件
    :return:
    """
    send_welcome_email.delay(email)
    return success()
