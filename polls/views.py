from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# 引用方式package.模块.类（或方法）
from polls.models import Question
# 引用Django自带的404页面
from django.http import Http404
# 引用HTML模板
from django.template import loader
# 引入JSON
import json
from django.core import serializers
from django.urls import reverse
from .models import Choice, Question
from django.views import generic

# 通用视图1
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # 你可以改变你的模板来匹配新的 context 变量 —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# Leave the rest of the views (detail, results, vote) unchanged
# 通用视图2
class DetailView(generic.DetailView):
    # 定义此视图的绑定model， 一般一个视图绑定一个对象，类似JAVA控制器
    model = Question
    template_name = 'polls/detail.html'

# results 视图和 detail 视图在渲染时具有不同的外观，即使它们在后台都是同一个 DetailView
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def test_JSON(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    json_data = serializers.serialize('json', latest_question_list)
    return HttpResponse(json_data, content_type="application/json")
