from bottle import Bottle,run,get,post,request,static_file,redirect
import os
import yaml
from bottle_swagger import SwaggerPlugin
from beaker.middleware import SessionMiddleware

app = Bottle()

this_dir = os.path.dirname(os.path.abspath(__file__))
with open("{}/swagger.yml".format(this_dir)) as f:
    swagger_def = yaml.load(f, Loader=yaml.SafeLoader)

app.install(SwaggerPlugin(swagger_def,serve_swagger_schema=True, serve_swagger_ui=True))

session_opts = {
   'session.type':'file',              #以文件的方式保存session
   'session.cookei_expires':300,       #session过期时间为300秒
   'session.data_dir':'/tmp/sessions_dir', #session保存目录
   'session.auto':True               #自动保存session
    }

@app.get('/index')
def index():
    return {'code': 0, 'msg': 'please post /login and input your username(your english name) and password(your english name)'}

@app.post('/login')
def login():
    user = request.json;
    username = user['username']
    password = user['password']

    if username == password:
        session = request.environ.get('beaker.session')

        session['user'] = username
        session.save

        return {'code': 0, 'msg': 'please select One Equipment:\n10001:Knife\n10002:Big Sword\n10003:KuiHuaBaoDian'}
    else:
        return {'code': 999, 'msg': 'Error 9901: Username or PassWord!!'}

@app.get('/selectEq/<equipmentid>')
def selectEq(equipmentid):
    print('equipmentid=' + equipmentid)

    session = request.environ.get('beaker.session')
    # print('session=' + session['equipmentid'])

    if equipmentid is not None:
        if str(equipmentid).isdigit():
            session['equipmentid']=equipmentid
            session.save
            return {'code': 0,
                    'msg': 'your pick up equipmentid:'+equipmentid+' please select your  enemyid:\n20001:Terran\n20002:ORC\n20003:Undead',
                    'data': {'equipmentid': equipmentid}}
    else:
        return {'code': 999, 'msg': 'Error 9902: Your kill yourself!!'}

@app.post('/kill')
def kill():
    requestJson = request.json;

    enemyid = requestJson['enemyid']
    print('enemyid' + enemyid)

    equipmentid = requestJson['equipmentid']
    print('equipmentid' + equipmentid)

    coockies = request.get_cookie("account", secret='some-secret-key')

    if enemyid is None:
        return {'code': 999, 'msg': 'Error 9904: Your kill yourself!!'}
    if equipmentid is None:
        return {'code': 999, 'msg': 'Error 9905: Your fight your enemy by nothing!And you are  died!'}
    if equipmentid in ['10001','10002','10003']:
        if enemyid in ['20001','20002','20003']:

            if (int(equipmentid) - int(enemyid)+10000)>0:
                return {'code': 0, 'msg': 'You win Level 1!'}
            elif (int(equipmentid) - int(enemyid)+10000)==0:
                return {'code': 0, 'msg': 'Your and your enemy all dead!!!'}
            else:
                return {'code': 0, 'msg': 'Your dead!'}
        else:
            return {'code': 900, 'msg': 'Error 9902: Your kill yourself!!'}
    else:
        return {'code': 901, 'msg': 'Error 9903: You Broken The Rule!And Kill yourself'}

app = SessionMiddleware(app, session_opts)
if __name__ == '__main__':
    run(app=app, port=8088)