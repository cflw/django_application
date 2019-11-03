from django import template
import 知识库.models as 模型

register = template.Library()

@register.simple_tag
def f文档(a名称):
	"""只显示一个标题"""
	v文档 = 模型.C文档表.objects.filter(m名称 = a名称)
	if v文档:
		return f"""<a href="/知识库/{a名称}">{v文档[0].m标题}</a>"""
	else:
		return f"""<i title="文档不存在">{a名称}</i>"""

@register.simple_tag
def f文档摘要(a名称):
	"""显示标题和摘要"""
	v文档 = 模型.C文档表.objects.filter(m名称 = a名称)
	if v文档:
		return f"""<a href="/知识库/{a名称}">{v文档[0].m标题}</a>：{v文档[0].m摘要}"""
	else:
		return f"""<i title="文档不存在">{a名称}</i>"""
