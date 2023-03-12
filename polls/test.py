from django.http import HttpResponse

from polls.models import Question


def query(request):
    list = Question.objects.all()
    response = ""
    response1 = ""
    for var in list:
        response1 += var.question_text + " "
    response = response1
    return HttpResponse("<p>" + "查询数据库返回的数据为：" + response + "</p>")
