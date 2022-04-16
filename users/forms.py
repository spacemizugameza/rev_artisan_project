from django import forms
from django.forms import TextInput,EmailInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
       
        # def __init__(self, *args , **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['username'].widget.attrs.update({
        #         'type':'text',
        #         'required':'',
        #         'help_text':'insert char',
        #         'name':'firstname',
        #         'placeholder':'User Name',
        #         'id':"input-firstname",
        #         'class':'form-control'
        #     })
        #     self.fields['email'].widget.attrs.update({
        #         'type':'email',
        #         'required':'',
        #         'name':'email',
        #         'placeholder':'E-mail',
        #         'id':"input-email",
        #         'class':'form-control'
        #     })
        #     self.fields['password1'].widget.attrs.update({
        #         'type':'password',
        #         'required':'',
        #         'name':'password',
        #         'placeholder':'Password',
        #         'id':"input-password",
        #         'class':'form-control'
        #     })
        #     self.fields['password2'].widget.attrs.update({
        #         'type':'password',
        #         'required':'',
        #         'name':'confirm',
        #         'placeholder':'Password Confirm',
        #         'id':"input-confirm",
        #         'class':'form-control'
        #     })


        class Meta:
            model = User
            fields = ['first_name','last_name','username','email','password1','password2']
            widgets = {
            'first_name': TextInput(attrs={'placeholder':'First Name',
            'type':'text',
            'required':'',
            'name':'firstname',
            'placeholder':'First Name',
            'id':"input-firstname",
            'class':'form-control'}),

            'last_name': TextInput(attrs={'placeholder':'Last Name',
            'type':'text',
            'required':'',
            'name':'lastname',
            'placeholder':'Last Name',
            'id':"input-lastname",
            'class':'form-control'}),

            'username': TextInput(attrs={'placeholder':'Username',
            'type':'text',
            'required':'',
            'name':'username',
            'placeholder':'User Name',
            'id':"input-username",
            'class':'form-control'
            }),
            'email': EmailInput(attrs={'placeholder':'Email',
            'type':'email',
            'required':'',
            'name':'email',
            'placeholder':'E-mail',
            'id':"input-email",
            'class':'form-control'
            })
            # 'password1': PasswordInput(attrs={'placeholder':'Password',
            # 'type':'password',
            # 'required':'',
            # 'name':'password',
            # 'placeholder':'password',
            # 'id':"input-password",
            # 'class':'form-control'
            # }),
            # 'password2': PasswordInput(attrs={'placeholder':'Confirm Password',
            # 'type':'password',
            # 'required':'',
            # 'name':'confirm',
            # 'placeholder':'Confirm Password',
            # 'id':"input-confirm",
            # 'class':'form-control'
            # })
        }
        def __init__(self, *args, **kwargs):
          super(UserCreationForm, self).__init__(*args, **kwargs)
          self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password',
          'type':'password',
          'required':'',
          'name':'password',
          'placeholder':'password',
          'id':"input-password",
          'class':'form-control'})
          self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password',
           'type':'password',
           'required':'',
           'name':'confirm',
           'placeholder':'Confirm Password',
           'id':"input-confirm",
           'class':'form-control'
             })


from django.contrib.auth.forms import AuthenticationForm, UsernameField
class LoginForm(AuthenticationForm):
  class Meta:
    model=User
    fields = ['username','password']

    # username = UsernameField(
    #   widget = forms.TextInput(
    #     attrs={'class': 'form-control', 'id': 'input-username', 'placeholder': 'Username'}
    #   )
    # )
    # widgets = {
    #       'username': TextInput(attrs={'placeholder':'First Name',
    #       'type':'text',
    #       'required':'',
    #       'name':'username',
    #       'placeholder':'User Name',
    #       'id':"input-username",
    #       'class':'form-control'}),

    #       'password': PasswordInput(attrs={'placeholder':'Password',
    #       'type':'password',
    #       'required':'',
    #       'name':'passwprd',
    #       'placeholder':'Password',
    #       'id':"input-passwprd",
    #       'class':'form-control'}),    

    # }
  def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.fields['username'].widget = forms.widgets.TextInput(attrs={
              'class': 'form-control',
              'type':'text',
              'required':'',
              'name':'username',
              'placeholder':'User Name',
              'id':"input-username",
          })
     self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
              'class': 'form-control',
              'type':'password',
              'required':'',
              'name':'password',
              'placeholder':'Password',
              'id':"input-password",
          })