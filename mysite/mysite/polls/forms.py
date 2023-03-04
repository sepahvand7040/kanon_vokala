from django import forms

from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_jalali.admin.filters import JDateFieldListFilter
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
# Apply summernote to specific fields.
class SummerForm(forms.Form):
    summer = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
	
# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())

class NameForm(forms.Form):
		firstname = forms.CharField(label='Your name', max_length=100)
		lastname = forms.CharField(label='Your name', max_length=100)
class PostForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())

class DateForm(forms.Form):
   date_paper 	=forms.DateField(widget=AdminJalaliDateWidget )
   date_andikator= forms.DateField(widget=AdminJalaliDateWidget )
   datetimejalali=SplitJalaliDateTimeField(widget=AdminSplitJalaliDateTime )