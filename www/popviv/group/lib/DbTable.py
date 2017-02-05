# -*- coding: UTF-8 -*-

class DbTable:

	@staticmethod
	def Db(model):
		#动态加载模块
		import_string = "from group.model.Db."+model+" import "+model
		#print import_string
		exec import_string
		return eval(model+"()")