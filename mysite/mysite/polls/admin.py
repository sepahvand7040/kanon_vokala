from django.contrib import admin
from .models import *
from .models import Post

from django_jalali.admin.filters import JDateFieldListFilter
from django_summernote.admin import SummernoteModelAdmin

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )


admin.site.register(Bar, BarAdmin)


class BarTimeAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )


admin.site.register(BarTime, BarTimeAdmin)

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  pass
  
admin.site.register(Member, MemberAdmin)
admin.site.register(T_input_paper, MemberAdmin)
admin.site.register(T_type_paper, MemberAdmin)
admin.site.register(T_user_pople, MemberAdmin)
admin.site.register(T_user_permination, MemberAdmin)
admin.site.register(T_user_erja, MemberAdmin)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)

