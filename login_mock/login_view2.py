#!/usr/bin/env python
# !coding:utf-8
from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

# 实例化一个WEB服务对象
from flask_restful import reqparse

server = Flask(__name__)
Swagger(server)
# 增加配置，支持中文显示
server.config['JSON_AS_ASCII'] = False


@server.route('/login_page',methods=['get'])
def get():
    return {'status': 0, 'msg': 'ok', 'data': 'this is a login page'}


# 构造一个接受post请求的响应
@server.route('/login', methods=['POST'])
@swag_from('login_post.yml')
def post():
    # request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据
    json_data = request.json
    print("json_data=%s" % json_data)
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='用户名不能为空')
    parser.add_argument('password', type=str, required=True, help='账户密码不能为空')
    parser.add_argument('age', type=int, help='年龄必须为正正数')
    parser.add_argument('sex', type=str, help='性别只能是男或者女', choices=['女', '男'])
    args = parser.parse_args()
    return jsonify(parser)


if __name__ == "__main__":
    # 运动服务，并确定服务运动 的IP和端口
    server.run(port=5001, debug=True)

