from django.http import HttpResponse,Http404
from .models import *
from django.shortcuts import render,get_object_or_404

# Create your views here.

def Frontpage(request):
    return render(request, "Frontpage.html",{})

def search(request):
    q = request.GET.get('index')

    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'errors.html', {'error_msg': error_msg})

    post_list = Actor.objects.filter(actor_name=q)
    return render(request, 'results.html', {'error_msg': error_msg,
                                               'post_list': post_list})

def actor(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'actor.html', {})
    
def director(request, question_id):
    return render(request, 'director.html', {})
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'detail.html',{'question':question})

def user(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)