from django.db import models

# Create your models here.
# 类名Question代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
# 1. 第一个表单Question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 重写 str方法
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        # datetime对象减去timedelta对象返回的还是datetime对象
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
# 2. 第二个表单Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 重写 str方法
    def __str__(self):
        return self.choice_text

