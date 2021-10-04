# from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Friend
# from .forms import HelloForm
from .forms import FriendForm
# from django.db.models import QuerySet
from django.views.generic import ListView
from django.views.generic import DetailView


# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title': 'Hello',
#             # 'message': 'your data:',
#             'form': HelloForm(),
#             'result': None
#         }

#     def get(self, request):
#         return render(request, 'hello/index.html', self.params)

#     def post(self, request):
# form
# msg = 'あなたは、<b>' + request.POST['name'] + \
#     '(' + request.POST['age'] + \
#     ') </b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + \
#     '</b> ですね。'
# self.params['message'] = msg

# BooleanField checkbox
# if ('check' in request.POST):
#     self.params['result'] = 'Checked!!'
# else:
#     self.params['result'] = 'Not checked...'

# NullBooleanField
# chk = request.POST['check']
# self.params['result'] = 'you selected: "' + chk + '".'

# ChoiceField pulldownmenu, radiobuttons
# ch = request.POST['choice']
# self.params['result'] = 'selected: "' + ch + '".'

# MultipleChoiceField getlist
# ch = request.POST.getlist('choice')
# result = '<ol class="list-group"><b>selected:</b>'
# for item in ch:
#     result += '<li class="list-group-item">' + item + '</li>'
# result += '</ol>'
# self.params['result'] = result

# self.params['form'] = HelloForm(request.POST)
# return render(request, 'hello/index.html', self.params)

# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result


# QuerySet.__str__ = __new_str__


def index(request):
    # num = Friend.objects.all().count()
    # first = Friend.objects.all().first()
    # last = Friend.objects.all().last()
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
        # 'form': HelloForm(),
        # 'data': [],
    }
    # if (request.method == 'POST'):
    #     num = request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data'] = [item]
    #     params['form'] = HelloForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)

# create model


def create(request):
    if (request.method == 'POST'):
        # name = request.POST['name']
        # mail = request.POST['mail']
        # gender = 'gender' in request.POST
        # age = int(request.POST['age'])
        # birth = request.POST['birthday']
        # friend = Friend(name=name, mail=mail, gender=gender,
        #                 age=age, birthday=birth)
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)


def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    prams = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', prams)


def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)


class FriendList(ListView):
    model = Friend


class FriendDetail(DetailView):
    model = Friend
