from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from django.http import HttpResponseRedirect


from.models import Message


def index(request):
    latest_message_list = Message.objects.order_by('-pub_date')[:5]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'billboard_app/index.html', context)


def new_msg(request):
    new_title = request.POST.get("title")
    new_content = request.POST.get("content")
    new_author = request.POST.get("author")
    new_message = Message.objects.create(pub_date=timezone.now(), title=new_title, content=new_content, author=new_author)
    new_message.save()
    return redirect('/billboard_app')

