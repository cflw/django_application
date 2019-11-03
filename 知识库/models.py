from django.db import models

# Create your models here.
class C文档表(models.Model):
	m标识 = models.AutoField(primary_key = True)
	m名称 = models.CharField(max_length=20)	#用来引用文档，不可修改
	m标题 = models.CharField(max_length=50)	#显示文档标题
	m摘要 = models.CharField(max_length=100, default="(没有描述)")	#简短描述
	m创建者 = models.IntegerField(default = 0)
	m创建时间 = models.TimeField(auto_now_add = True)
	m修改者 = models.IntegerField(default = 0)
	m修改号 = models.IntegerField(default = 0)
	m修改时间 = models.TimeField(auto_now = True)
	m内容 = models.TextField()
	mi目录显示 = models.BooleanField(default = False)
	m排列位置 = models.IntegerField(default = 9999)	#同一级别中的位置
	m上级文档 = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
	def __str__(self):
		return self.m名称
	@staticmethod
	def f找标识(a标识):
		if not a标识:
			return None
		v找 = C文档表.objects.filter(m标识 = a标识)
		if v找:
			return v找[0]
		else:
			return None
	@staticmethod
	def f找名称(a名称):
		if not a名称:
			return None
		v找 = C文档表.objects.filter(m名称 = a名称)
		if v找:
			return v找[0]
		else:
			return None

class C人员表(models.Model):
	m标识 = models.AutoField(primary_key = True)
	m姓名 = models.CharField(max_length=20)
	m单位 = models.CharField(max_length=20)
	m职务 = models.CharField(max_length=10)
	m电话 = models.CharField(max_length=20)
	m邮箱 = models.CharField(max_length=40)
	def __str__(self):
		return self.m姓名

# class C管理员表(models.Model):
# 	m标识 = models.AutoField(primary_key = True)
# 	m名称 = models.CharField(max_length=20)	#显示的名称
# 	m用户名 = models.CharField(max_length=20)
# 	m密码 = models.CharField(max_length=200)	#加密存储