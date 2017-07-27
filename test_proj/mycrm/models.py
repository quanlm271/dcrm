from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
# Create your models here.
class Restoration(models.Model):
	id = models.AutoField(primary_key=True, unique=True, verbose_name=u'MS')
	name = models.CharField(max_length=50,verbose_name=u'Tên')
	price = models.IntegerField(verbose_name=u'Giá Tiền')

	def __str__(self):
		return self.name
	
	# def get_absolute_url(self):
	# 	return reverse('server_edit', kwargs={'pk': self.pk})

class Customer(models.Model):
	id = models.AutoField(primary_key=True, unique=True, verbose_name=u'MSKH')
	create_date = models.DateField(blank=False,verbose_name=u'Ngày Tạo')
	name = models.CharField(max_length=50,  verbose_name=u'Tên')
	phone_number = models.CharField(max_length=12,verbose_name=u'SĐT')
	address = models.CharField(max_length=100,verbose_name=u'Địa Chỉ')
	tooth_diagram = models.CharField(max_length=50, verbose_name=u'Sơ đồ răng')
	tooth_number = models.IntegerField(verbose_name=u'Số Lượng Răng')
	restoration_request = models.ForeignKey(Restoration,verbose_name=u'Yêu Cầu Phục Hình')
	amount = models.IntegerField(verbose_name=u'Thành Tiền')
	note = models.CharField(max_length=100, blank=True, verbose_name=u'Ghi Chú')

	def __str__(self):
		return self.name




