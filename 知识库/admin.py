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

admin.site.register(models.C文档表, C文章管理)
admin.site.register(models.C文件表)
admin.site.register(models.C图片表)