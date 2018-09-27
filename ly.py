#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import pymongo
import time

def main(page):
	print(page)
	url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

	data = {'qqmusic_ver': 1298, 
	'remoteplace': 'txt.yqq.lyric', 
	'inCharset': 'utf8', 
	'sem': 1, 'ct': 24, 'catZhida': 1, 'p': page,
	'needNewCode': 0, 'platform': 'yqq', 
	'lossless': 0, 'notice': 0, 'format': 'jsonp', 'outCharset': 'utf-8', 'loginUin': 0,
	'jsonpCallback': 'MusicJsonCallback19507963135827455',
	'searchid': '98485846416392878',
	'hostUin': 0, 'n': 10, 'g_tk': 5381, 't': 7,
	'w': '周杰伦', 'aggr': 0
	}

	headers = {'content-type': 'application/json',
	           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
	r = requests.get(url, params = data, headers = headers)
	time.sleep(3)
	text = r.text[35:-1]
	# print(text)
	result = json.loads(text)
	if result['code'] == 0:

		for list in result['data']['lyric']['list']:
			item = {
				'albumname': list['albumname'],
				'content': list['content']
			}
			mongoInsert(item)
		# print (list)
		# print(item)




def mongoInsert(item):

	client = pymongo.MongoClient(host='localhost',port=27017)
	db = client.qqmusic
	# item为指定集合名
	collection = db.JayZhou
	res = collection.insert(item)
	print(res)
	print('插入成功')


if __name__ == '__main__':
	for i in xrange(5, 20):
		main(i)
