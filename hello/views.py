from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm


class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            # 'message': 'your data:',
            'form': HelloForm(),
            'result': None
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
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
        ch = request.POST.getlist('choice')
        result = '<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result += '<li class="list-group-item">' + item + '</li>'
        result += '</ol>'
        self.params['result'] = result

        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
