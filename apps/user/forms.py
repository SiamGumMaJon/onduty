from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Users



from django.forms.widgets import DateInput
class UsersForm(forms.ModelForm):
       class Meta:
              model = Users
              # fields = ["date", "name", "withdraw","approver"]
              fields = "__all__"
              widgets = {'date': DateInput(attrs={'type': 'date'}),}

              
              

class MyAuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(MyAuthForm,self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            # attrs = { 'autofocus': True,
            #         'class' : 'form-control',
            #         'id' : 'username',
            #         'placeholder' : 'email ทอ. ไม่ต้องมี @rtaf',
            #         'size' : 20}))
            attrs = { 
                    'autofocus': True,
                    # 'type' :"email",
                    'class' : 'form-control',
                    'id' : 'username',
                    'placeholder' : 'email ทอ. ไม่ต้องมี @rtaf',
                    'class': 'form-control form-control-user',
                    # 'id' : 'exampleInputEmail', 
                    'aria-describedby' : 'emailHelp'
                    }))


    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                    'autocomplete': 'current-password',
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'id' : 'password',
                    'class' : 'form-control form-control-user',
                    # 'id' : 'exampleInputPassword',                                    
                    })
    )
