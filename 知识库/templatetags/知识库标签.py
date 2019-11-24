from django import template
from django.utils.html import format_html
import 知识库.models as 模型
#===============================================================================
# 标签
#===============================================================================
register = template.Library()
@register.simple_tag
def f文档(a名称):
	"""只显示一个标题"""
	if v文档 := 模型.C文档表.objects.filter(m名称 = a名称):
		return format_html("""<a href="/知识库/{}">{}</a>""", a名称, v文档[0].m标题)
	else:
		return f文档不存在(a名称, "文档不存在")
@register.simple_tag
def f文档摘要(a名称):
	"""显示标题和摘要"""
	if v文档 := 模型.C文档表.objects.filter(m名称 = a名称):
		return format_html("""<a href="/知识库/{}">{}</a>：{}""", a名称, v文档[0].m标题, v文档[0].m摘要)
	else:
		return f文档不存在(a名称, "文档不存在")
@register.simple_tag
def f文件(a名称):
	if v文件 := 模型.C文件表.objects.filter(m名称 = a名称):
		return format_html("""<a href="{}">{}</a>""", v文件[0].m文件.url, v文件[0].m标题)
	else:
		return f文档不存在(a名称, "文件不存在")
@register.simple_tag
def f图片(a名称):
	if v图片 := 模型.C图片表.objects.filter(m名称 = a名称):
		return format_html("""<img src="{}" title="{}"/>""", v图片[0].m图片.url, v图片[0].m标题)
	else:
		return f文档不存在(a名称, "图片不存在")
#===============================================================================
# 模板
#===============================================================================
def f文档不存在(a名称, a标题):
	return format_html("""<i title="{}">({})</i>""", a标题, a名称)