from rest_framework import serializers
from digital_twins_service.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# ModelSerializer 类并不会做任何特别神奇的事情，它们只是创建序列化器类的快捷方式：
#
# 自动确定一组字段。(不用重复去定义类属性)
# 默认简单实现的 create() 和 update() 方法。
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
