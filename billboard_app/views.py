from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from.models import Message


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request,  new_user)
            return HttpResponseRedirect("/billboard_app/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form,
                                                                    })


@login_required
def index(request):
    latest_message_list = Message.objects.order_by('-pub_date')[:5]
    context = {'latest_message_list': latest_message_list}
    now = timezone.now()
    return render(request, 'billboard_app/index.html', context)


@login_required
def new_msg(request):
    new_title = request.POST.get("title")
    new_content = request.POST.get("content")
    new_author = request.POST.get("author")
    new_message = Message.objects.create(pub_date=timezone.now(), title=new_title, content=new_content, author=new_author)
    new_message.save()
    return redirect('/billboard_app')

