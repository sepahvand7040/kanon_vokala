from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
class T_type_paper(models.Model):
  type_paper = models.CharField(max_length=255)
  code_paper = models.CharField(max_length=255)
  sharh_paper = models.CharField(max_length=255)
  pp_paper = models.CharField(max_length=255)
class T_input_paper(models.Model):
  user_send_id = models.CharField(max_length=255)
  date_deliver = models.DateField(null=True)
  no_andikator = models.CharField(max_length=255)
  type_paper_id = models.CharField(max_length=255)
  date_paper= models.DateField()
  date_andikator= models.DateField()
  user_deliver_id= models.CharField(max_length=255)
  no_paper_deliver= models.CharField(null=True,max_length=255)
  permination= models.CharField(max_length=255)
  mozo= models.CharField(null=True,max_length=255)
  tozihat= models.CharField(null=True,max_length=500)
  content_paper=models.TextField(null=True)
  photo_file = models.FileField(null=True)
  peyvast=models.CharField(null=True,max_length=255)
  peyvast_file = models.FileField(  null=True)
  date_paper_see= models.DateField(null=True)
class T_user_pople(models.Model):
  name = models.CharField(null=True,max_length=255)
  last_name = models.CharField(null=True,max_length=255)
  organ = models.CharField(null=True, max_length=255)
  linker = models.CharField(null=True,max_length=255)
  tozih = models.CharField(null=True,max_length=255)
class T_user_erja(models.Model):

  user_deliver_erja = models.IntegerField(null=True)
  user_send_id 	  	= models.CharField(max_length=255)
  paper_erja		= models.IntegerField(null=True)
  date_send		  	= models.DateField()
  date_see		  	= models.DateField()
  tozih             = models.TextField(null=True)
class T_sign_digital(models.Model):
  photo_sign 	    = models.FileField(  )
  user_sign_id 	  	= models.CharField(max_length=255)
class T_user_permination(models.Model):
  perm_step = (
        ('1', 'عادی'),
        ('2', 'محرمانه'),
        ('3', 'فوق محرمانه'),
    )
  user_id 	    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perm_user')
  user_perm 	 = models.CharField(max_length=1, choices=perm_step)

class Kanon_perm(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        permissions = (
                       ("show_step", "namayesh step mahramenh"),
                       ("show_base_seting", "namayesh tanzimat avaliyeh"),
                      )
  

class Bar(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200)
    date = jmodels.jDateField()

    def __str__(self):
        return "%s, %s" % (self.name, self.date)


class BarTime(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200)
    datetime = jmodels.jDateTimeField()

    def __str__(self):
        return "%s, %s" % (self.name, self.datetime) 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField( default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
  
  

 # def __str__(self):
 #   return f"{self.firstname} {self.lastname}"