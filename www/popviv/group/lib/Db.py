# -*- coding: UTF-8 -*-
import MySQLdb
import MySQLdb.cursors

class Db(object):

	host 		= "localhost"
	root 		= "root"
	password 	= ""
	dbname		= ""
	port		= 3306
	charset		= 'utf8'
	connect_status = False #数据库连接状态
	db          = None #db对象
	cursor      = None
	db_table    = None

	#config 初始化配置
	def __init__(self,config=None):
		if isinstance(config,dict):
			self.host 		= config.get('host',self.host)
			self.root 		= config.get('root',self.root)
			self.password 	= config.get('password',self.password)
			self.dbname     = config.get('dbname',self.dbname)
			self.port      	= config.get('port',self.port)
			self.charset    = config.get('charset',self.charset)
		'''
		print "====config====="
		print self.host
		print self.root
		print self.password
		print self.dbname
		print self.port
		print self.charset
		print "=============="
		'''

	#数据库连接
	def connect(self,dbname=None):
		#self.dbname = self.dbname if dbname!=None else dbname
		#print self.dbname
		if self.connect_status==False:
			#cursorclass 设置返回dict数据类型格式
			self.db = MySQLdb.connect(self.host,self.root,self.password,self.dbname,self.port,self.charset,cursorclass = MySQLdb.cursors.DictCursor)
			self.connect_status = True

		self.cursor = self.db.cursor()

	#获取单条数据
	def getRow(self,sql):
		self.connect() 
		
		try:	
			self.cursor.execute(sql)
			# 使用 fetchone() 方法获取一条数据库。
			return self.cursor.fetchone()
		except:
		   # Rollback in case there is any error
		   self.db.rollback()
		return {}

	#获取多条数据
	def getList(self,sql):
		self.connect() 
		
		try:	
			self.cursor.execute(sql)
			# 使用 fetchone() 方法获取一条数据库。
			return self.cursor.fetchall()
		except:
		   # Rollback in case there is any error
		   self.db.rollback()
		return {}

	#写入数据
	def insert(self,sql):
		self.connect() 
		try:
			# 执行sql语句
			if isinstance(sql,str):	
				self.cursor.execute(sql)
				# 提交到数据库执行
				return self.db.commit()

		except:
			pass
			#self.db.rollback()

	#更新数据
	def update(self,sql):
		self.connect() 
		try:
			if isinstance(sql,str):
				# 执行sql语句
				self.cursor.execute(sql)
				# 提交到数据库执行
				return self.db.commit()
		except:
			self.db.rollback()
	#删除数据
	def delete(self,sql):
		self.connect() 
		try:
			if isinstance(sql,str):
				# 执行sql语句
				self.cursor.execute(sql)
				# 提交到数据库执行
				return self.db.commit()
		except:
			self.db.rollback()
	
	def close(self):
		if self.db!=None:
			self.db.close()

	#析构函数
	def __del__(self):
		self.close()
