# from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView
# from .forms import HelloForm
from .models import Friend
from django.db.models import QuerySet


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

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result


QuerySet.__str__ = __new_str__


def index(request):
    # num = Friend.objects.all().count()
    # first = Friend.objects.all().first()
    # last = Friend.objects.all().last()
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        'message': 'all friends.',
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
