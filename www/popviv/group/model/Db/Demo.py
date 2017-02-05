# -*- coding: UTF-8 -*-
from group.lib.Db import Db
from group.config.db_config import DB_CONFIG
# Create your models here.

class Demo(Db):
        
    db_table = 'dl_testdemo'

    def __init__(self,config=None):
    	if config == None:
    		config = DB_CONFIG

    	super(Demo, self).__init__(config)