from django.shortcuts import render
from django.template import Context, Template
import 知识库.models as 模型
import markdown
# Create your views here.
c文档头 = """
{% load static %}
{% load 知识库标签 %}
"""
c上下文 = Context()
def f渲染文档内容(a内容):
	v文档模板 = Template(c文档头 + markdown.markdown(a内容))
	return v文档模板.render(c上下文)
def f网页(a请求, a名称 = "首页"):
	v文档 = 模型.C文档表.f找名称(a名称)
	if v文档:
		# 如果有子文档,分割目录
		va子文档 = v文档.c文档表_set.filter(mi目录显示 = True).order_by("m排列位置")
		if v上级文档 := v文档.m上级文档:
			va兄弟文档 = v上级文档.c文档表_set.filter(mi目录显示 = True).order_by("m排列位置")
		else:
			va兄弟文档 = 模型.C文档表.objects.filter(m上级文档 = None).filter(mi目录显示 = True).order_by("m排列位置")
		va文档0 = va兄弟文档.filter(m排列位置__lte = v文档.m排列位置)
		va文档1 = va兄弟文档.filter(m排列位置__gt = v文档.m排列位置)
		def fe导航():
			yield v文档
			v = v文档.m上级文档
			while v:
				yield v
				v = v.m上级文档
		va导航 = list(fe导航())
		va导航.reverse()
		v模板变量 = {
			"va导航": va导航,
			"v内容" : f渲染文档内容(v文档.m内容),
			"v上级": v文档.m上级文档,
			"va文档0": va文档0,
			"va子文档": va子文档,
			"va文档1": va文档1,
		}
	else:
		v模板变量 = {
			"va导航": [],
			"v内容" : "文档不存在",
			"v上级": None,
			"va文档0": 模型.C文档表.objects.filter(m上级文档 = None).filter(mi目录显示 = True).order_by("m排列位置"),
			"va子文档": [],
			"va文档1": [],
		}
	return render(a请求, "网页.html", v模板变量)