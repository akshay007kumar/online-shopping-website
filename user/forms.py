from django import forms
from . models import Customer, UserProfile


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'mobile', 'email']

    username = forms.CharField(max_length=40,
                               label="",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Username',

                                   }))
    password = forms.CharField(max_length=40,
                               label="",
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'password'
                                   }))

    mobile = forms.CharField(max_length=15,
                             label="",
                             widget=forms.NumberInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Mobile'
                                 }))

    email = forms.CharField(max_length=50,
                            label="",
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Email'
                                }))


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'permanent_address',
                  'shipping_address', 'profile_image', 'dob']

    first_name = forms.CharField(max_length=40,
                                 label="First Name",
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Firstname'
                                     }))

    last_name = forms.CharField(max_length=40,
                                label="Last Name",
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Lastname'
                                    }))

    permanent_address = forms.CharField(max_length=100,
                                        label="Permanent Address",
                                        widget=forms.Textarea(
                                            attrs={
                                                'rows': 3,
                                                'class': 'form-control',
                                                'placeholder': 'Permanent address'
                                            }))

    shipping_address = forms.CharField(max_length=100,
                                       label="Shipping Address",
                                       widget=forms.Textarea(
                                           attrs={
                                               'rows': 3,
                                               'class': 'form-control',
                                               'placeholder': 'Shipping address'
                                           }))


    dob = forms.DateField(label="Date of Birth",
                          widget=forms.DateInput(
                              attrs={
                                  'placeholder': "date of birth",
                                  'class': 'form-control',
                                  'type': 'date',
                              }))


class LoginForm(forms.Form):

    username = forms.CharField(max_length=40,
                               label="",
                               widget=forms.TextInput(
                                   attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Username'
                                   }))

    password = forms.CharField(max_length=40,
                               label="",
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter Password'
                                   }))


class ChangePassword(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['password']

    password = forms.CharField(max_length=40,
                               label="",
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Old Password'
                                   }))
    newPassword = forms.CharField(max_length=40,
                                  label="",
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'New Password'
                                      }))
    repeatPassword = forms.CharField(max_length=40,
                                     label="",
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Repeat Password'
                                         }))
