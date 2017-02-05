from django.db import models

# Create your models here.

class dl_testdemo(models.Model):
    #id 		= models.IntegerField()
    count 	= models.IntegerField()

    class Meta:     
        db_table = 'dl_testdemo'