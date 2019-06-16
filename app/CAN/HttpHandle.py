# coding: utf8
import requests,json
def dataPost(json_object) :
	'数据上传'
	try:
		r=requests.post('http://localhost:5000/admin/pigbase/',json=json_object)
		ack=json.loads(r.text)
		if(ack['success'] != True):
			print('dataPost',ack)
			print('dataPost err',json_object)
			return False
		else:
			return True
	except :
		print('connect failed !')
		return False

def devicePost(json_object) :
	'设备新增'
	try :
		r=requests.post('http://localhost:5000/admin/stationinfo/', json=json_object)
		ack=json.loads(r.text)
		if(ack['success'] != True):
			print('devicePost',ack)
	except :
		print('connect failed !')
		return False
def devicePut(json_object) :
	'设备状态修改'
	try:
		r=requests.put('http://localhost:5000/admin/stationinfo/', json=json_object)
		ack=json.loads(r.text)
		if(ack['success'] != True):
			print('devicePut',ack)
	except :
		print('connect failed !')
		return False

