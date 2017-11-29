# coding: utf-8
import xlrd
import pymysql
import sys
reload(sys)   
sys.setdefaultencoding('utf8')


class ExchangeData(object):
	
	def reader(self):
		area = []
		area_id = []
		data = xlrd.open_workbook('***xlsx')
		table = data.sheets()[0]
		for i in range(1, table.nrows):
			area.append(str(table.row_values(i)[1]))
			area_id.append(str(table.row_values(i)[2]))
		return area,area_id
	
	def get_sql(self, name):
		connection = pymysql.connect(host='192.168.7.250',
                             port=3308,
                             user='z******qi',
                             password='j*****!',
                             db='t******',
							 charset='utf8')
		try:
			cursor = connection.cursor()
			cursor.execute("""SELECT *
							FROM c***_qg
							WHERE name='%s'
							""" % name)
			data = cursor.fetchone()
			if data:
				return data, ''
			else:
				return '', name
		except:
			print ("%s, 数据插入失败" % name.decode('utf-8'))
			return '', ''
		
	def insert_sql(self, name, area_id):
		print name[0], name[1], name[2], name[3], name[4], name[5], name[6], name[7]
		connection = pymysql.connect(host='192.168.7.250',
                             port=3308,
                             user='z***qi',
                             password='jia***7!',
                             db='tbk**r',
							 charset='utf8')
		cursor = connection.cursor()
		#INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
		sta = cursor.execute("""INSERT INTO comm*****y_ln
						VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
						""" % (name[0], area_id, name[2], name[3], name[4], name[5], name[6], name[7]))
		connection.commit()  
		cursor.close()      
		connection.close() 
		print sta
		return sta

if __name__ == '__main__':
	bad_name = []
	area,area_id = ExchangeData().reader()
	for i in range(len(area)):
		res, bad = ExchangeData().get_sql(area[i])
		if bad:
			bad = bad.encode('utf8')
			bad_name.append(bad)
		if res:
			ExchangeData().insert_sql(res, area_id[i])
	
	print bad_name
