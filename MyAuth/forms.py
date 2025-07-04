from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    frist_name = forms.CharField(max_length=40, required=True)
    last_name = forms.Charfield(max_length=40, required=True)

    class Meta:
        model = User 
        fields = ('username','email','first_name','last_name','password1','password2')
        
        def save(self, commit = True):
            user = super().save(commit = False)
            user.email= self.cleaned_data['email']
            user.frist_name= self.celaned_data['first_name']
            user.last_name= self.cleaned_data['last_data']
            if commit:
                user.save()
            return user
        
class CustomAuthenticationForm(AuthenticationForm):
    pass
        