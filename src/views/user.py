#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash
from flask import Blueprint, request
from ..models.user import User
from src.extensions import jsonrpc_user

bp = Blueprint('user', __name__)


@jsonrpc_user.method('UserService.login')
def login(username, password):
    """
    用户登录
    :param username:
    :param password:
    :return:
    """
    user = User.authenticate(username, password)
    if user is None:
        return {
            "success": False,
            "message": "登录失败"
        }

    return {
        "success": True,
        "message": "登录成功",
        "data": user.to_dict()
    }


@jsonrpc_user.method('UserService.register_user')
def register_user(username, password, email, gender):
    """
    注册用户
    :param username:
    :param password:
    :param email:
    :param gender:
    :return:
    """
    password_hash = generate_password_hash(password, method="pbkdf2:sha1", salt_length=8)
    user = User(username=username,
                password_hash=password_hash,
                email=email,
                gender=gender)
    user.save()

    return {
        "success": True,
        "message": "注册成功",
        "data": user.to_dict()
    }

