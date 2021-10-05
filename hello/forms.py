from django import forms
from.models import Friend


class FriendForm(forms.ModelForm):
    # name = forms.CharField(label='name',
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mail = forms.CharField(label='mail',
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # age = forms.IntegerField(label='age',
    #                          widget=forms.NumberInput(attrs={'class': 'form-control'}))

    # required True:チェックしないと送信できない
    # check = forms.BooleanField(label='check', required=False)

    # check = forms.NullBooleanField(label='Check')

    # data = [
    #     ('one', 'item 1'),
    #     ('two', 'item 2'),
    #     ('three', 'item 3'),
    #     ('four', 'item 4'),
    #     ('five', 'item 5')
    # ]
    # choice = forms.ChoiceField(label='Choice', choices=data)

    # choice = forms.ChoiceField(label='radio', \
    #     choices=data, widget=forms.RadioSelect())

    # choice = forms.ChoiceField(label='radio', \
    #     choices=data, widget=forms.Select(attrs={'size': 5}))

    # choice = forms.MultipleChoiceField(
    #     label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))

    # id = forms.IntegerField(label='ID')

    # name = forms.CharField(label='Name',
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mail = forms.EmailField(label='Email',
    #                         widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # gender = forms.BooleanField(label='Gender', required=False,
    #                             widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # age = forms.IntegerField(label='Age',
    #                          widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # birthday = forms.DateField(label='Birth',
    #                            widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
