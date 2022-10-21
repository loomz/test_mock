# Battle API手册

## 介绍


访问入口：
restful（http://127.0.0.1:8088/)
普通http（http://127.0.0.1:8087/)

示例系统python3.6及其以上运行的，安装好python后，需要安装如下安装包

	pip install bottle
	pip install beaker

    pip install bravado-core
    pip install swagger-spec-validator
    pip install bottle-swagger-2

如果出现异常：ModuleNotFoundError: No module named 'jsonschema.compat'
说明安装的依赖jsonschema版本不对，需要卸载安装指定版本  
    pip install jsonschema==3.2.0

系统按照一种类似对战游戏的模式设计。

系统运行方法：
 
 	 python __init__.py

## 1.1 首页

接口描述：访问主页

调用方式：get

访问路由：/ 或者/index

响应内容：说明性文本

## 1.2 登录


接口描述：登录

调用方式: post

访问路由：/login

入参格式：param1=1&param2=2

入参内容：body


|名称|类型|长度限制|可空|备注|
|---|---|---|---|---|
|username|String|30|no|英文名称|
|password|String|30|no|英文名称|



响应格式：文本

响应内容：说明性文字


## 1.3 选择装备

接口描述：选择装备

调用方式: post

访问路由：/selectEq

入参格式：param1=1&param2=2

入参内容：body

|名称|类型|长度限制|可空|备注|
|---|---|---|---|---|
|equipmentid|int|4|no|装备编号|


响应格式：json

响应内容：


|名称|类型|长度|可空|备注|
|---|---|---|---|---|
|equipmentid|int| |	no|选择的装备id| 
|message|String	||yes|交互结果描述 |


## 1.4 杀敌

接口描述：选择装备

调用方式: post

访问路由：/kill

入参格式：param1=1&param2=2

入参内容：body



|名称|类型|长度限制|可空|备注|
|equipmentid|int|4|no|装备编号|
|enemyid|int|4|no|打怪兽编号|

响应格式：文本

响应内容：说明性文本，说明战斗结果

