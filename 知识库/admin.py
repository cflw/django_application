from django.contrib import admin
from . import models
# Register your models here.
class C文章管理(admin.ModelAdmin):
	fields = [
		"m名称",
		"m标题",
		"m摘要",
		"m内容",
		"mi目录显示",
		"m排列位置",
		"m上级文档",
	]
	list_display = ("m名称", "m标题", "mi目录显示", "m排列位置")
	list_editable = ("mi目录显示", "m排列位置")
	#动作
	actions = ["f排列位置加一百", "f排列位置减一百"]
	def f排列位置加一百(self, a请求, a查询集):
		for v记录 in a查询集:
			v记录.m排列位置 += 100
			v记录.save()
	f排列位置加一百.short_description = "排列位置 +100"
	def f排列位置减一百(self, a请求, a查询集):
		for v记录 in a查询集:
			v记录.m排列位置 -= 100
			v记录.save()
	f排列位置减一百.short_description = "排列位置 -100"

admin.site.register(models.C文档表, C文章管理)
admin.site.register(models.C文件表)
admin.site.register(models.C图片表)