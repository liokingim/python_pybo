from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from django.views import generic
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
import logging

# logger = logging.getLogger(__name__)
logger = logging.getLogger('mysite')

# Create your views here.
def index(request):
    # 페이지
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    # 페이지당 10개씩 보여 주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # question_list는 페이징 객체(page_obj)
    context = {'question_list': page_obj}
    logger.debug('context:')
    logger.debug(page_obj.paginator.num_pages )
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question

            logger.debug("answer: %s", answer)

            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

# 제네릭 뷰
# class IndexView(generic.ListView):
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')

# class DetailView(generic.DetailView):
#     model = Question