from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import *
from .login_kanon import *
from .check_valid import *
from django.db.models import Q
from .forms import *
from django.contrib.auth import authenticate,login
from django.db.models.expressions import RawSQL
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from jalali_date import datetime2jalali, date2jalali
str_result=''
def members(request):
  user=User.objects.first()
  step_ok=user.has_perm('polls.show_step')
  mymembers = Member.objects.all().values()
  mypapers = T_type_paper.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
	'step_ok':step_ok,
    'mymembers': mymembers,
	'mydata': mypapers,
	
  }
  return HttpResponse(template.render(context, request))
  
#--------------------------------------------
@permission_required('polls.show_base_seting')
@permission_required('polls.show_step', raise_exception=True)

def add(request):
  
  user=User.objects.first()
  step_ok=user.has_perm('polls.show_step')
  
  datauser=login_kanon.login_kanon_def()
  mypapers = T_type_paper.objects.all().values()
  context = {
	
    'step_ok':step_ok,
	'mydata': mypapers,
	'datauser': datauser,
	'activeadd':'active',
  }
  template = loader.get_template('inputformpaper.html')
  return HttpResponse(template.render(context, request))
#--------------------------------------------
  
# Create your views here.


def addrecord(request):
  type_paper = request.POST['type_paper']
  code_paper = request.POST['code_paper']
  sharh_paper = request.POST['sharh_paper']
  pp_paper = request.POST['pp_paper']
  t_type_paper = T_type_paper(type_paper=type_paper, code_paper=code_paper,sharh_paper=sharh_paper,pp_paper=pp_paper)
  t_type_paper.save()
  return HttpResponseRedirect(reverse('add'))
  
def delete(request, id):

  member = T_type_paper.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('add'))
  
def update(request, id):
  mymember = T_type_paper.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mydata': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, id):
  type_paper = request.POST['type_paper']
  code_paper = request.POST['code_paper']
  sharh_paper = request.POST['sharh_paper']
  pp_paper = request.POST['pp_paper']
  member = T_type_paper.objects.get(id=id)
  member.type_paper = type_paper
  member.code_paper = code_paper
  member.sharh_paper = sharh_paper
  member.pp_paper = pp_paper
  member.save()
  return HttpResponseRedirect(reverse('add'))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  step_ok=request.user.has_perm('polls.show_step')
  context = {
    'step_ok': step_ok,
  }
  template = loader.get_template('main.html')
  
  return HttpResponse(template.render(context, request))
  


def search(request):
  mydata=None
  type_paper = request.POST['type_paper']
  code_paper = request.POST['code_paper']
  sharh_paper = request.POST['sharh_paper']
  pp_paper = request.POST['pp_paper']
  mymembers = T_type_paper.objects.all().values()
  mydata = T_type_paper.objects.filter(Q(type_paper=type_paper) | Q(code_paper=code_paper) | Q(sharh_paper=sharh_paper) | Q(pp_paper=pp_paper)).values()
  if mydata == None :
    mydata = T_type_paper.objects.all().values()
  template = loader.get_template('inputformpaper.html')
  context = {
    'mymembers': mymembers,
	'mydatasearch':mydata,
	'activesearch':'active',
	
  }
  return HttpResponse(template.render(context, request))
 
def paperindex(request):
  jalali_join = date2jalali(timezone.now()).strftime( '%Y-%m-%d')
  mypapers = T_type_paper.objects.all().values()
  mydatapaper = T_input_paper.objects.all().values()
  mydatapople = T_user_pople.objects.all().values()
  mydatauser=User.objects.all().values()
  context = {
    'mydatauser': mydatauser,
	'mydata': mypapers,
	'mydatapople': mydatapople,
	'activepaper':'active',
	'mydatapaper': mydatapaper,
	'jalali_join': jalali_join,
	
  }
  template = loader.get_template('paperindex.html')
  
  return HttpResponse(template.render(context, request))
  
def addrecord_input_paper(request):
  t_input_paper = T_input_paper(
	user_send_id = request.POST['user_send_id'],
	date_deliver = request.POST['date_deliver'],
	no_andikator = request.POST['no_andikator'],
	type_paper_id = request.POST['type_paper_id'],
	date_paper = request.POST['date_paper'],
	date_andikator = request.POST['date_andikator'],
	user_deliver_id = request.POST['user_deliver_id'],
	no_paper_deliver = request.POST['no_paper_deliver'],
	permination = request.POST['permination'],
	mozo = request.POST['mozo'],
	tozihat = request.POST['tozihat'],
	content_paper = '',
	photo_file = request.FILES['photo_paper'],
	peyvast = request.POST['user_send_id'],
	peyvast_file = request.FILES['peyvast_file'],)
  t_input_paper.save()
  return HttpResponseRedirect(reverse('paperindex'))
  
def input_user_pople(request):
  mydata = T_user_pople.objects.all().values()
  context = {
    
	'mydata': mydata,
	'activpople':'active',
	
	
  }
  template = loader.get_template('input_user_pople.html')
  
  return HttpResponse(template.render(context, request))
  
  
def addrecord_input_user_pople(request):
  t_user_pople = T_user_pople(
	name = request.POST['name'],
	last_name = request.POST['last_name'],
	organ = request.POST['organ'],
	linker = request.POST['linker'],
	tozih = request.POST['tozih'],)
  
  t_user_pople.save()
  return HttpResponseRedirect(reverse('input_user_pople'))
  
def datagrade_cartabl(request,id,see):
  #mydata = T_input_paper.objects.all().values()
  #user=User.objects.first()
  str_sql='select * from polls_t_input_paper,polls_t_user_erja where (polls_t_user_erja.user_deliver_erja='+str(id)	+' and polls_t_input_paper.id=polls_t_user_erja.paper_erja)'
  mydata1 = T_input_paper.objects.raw(str_sql)
  see_is=T_input_paper.objects.filter(user_deliver_id=id,date_paper_see__isnull=True).values()
  see_not=T_input_paper.objects.filter(user_deliver_id=id,date_paper_see__isnull=False).values()
  see_erja=T_input_paper.objects.raw(str_sql)
  if(see==1):
	  mydata = see_not
  elif(see==0):
	  mydata = see_is
  elif(see==3):
	  mydata = see_erja
  #QuerySet.annotate(val=RawSQL('select * from T_input_paper ', (param,)))
  context = {
    'see_is':see_is,
	'see_not':see_not,
	'see_erja':see_erja,
    'sqls':str_sql,
    'mydata1': mydata1,
	'mydata': mydata,
	'activpople':'active',
	
	
  }
  template = loader.get_template('datagrade_cartabl.html')
  
  return HttpResponse(template.render(context, request))
  
def show_paper(request, id,):
  str_sql="select *,(SELECT auth_user.last_name from auth_user where auth_user.id=polls_t_user_erja.user_send_id) as lastname,(SELECT auth_user.first_name from auth_user where auth_user.id=polls_t_user_erja.user_send_id) as firstname,(SELECT auth_user.first_name from auth_user where auth_user.id=polls_t_user_erja.user_deliver_erja) as dfirstname,(SELECT auth_user.last_name from auth_user where auth_user.id=polls_t_user_erja.user_deliver_erja) as dlastname from auth_user,polls_t_user_erja where  polls_t_user_erja.paper_erja="+str(id)+" and polls_t_user_erja.user_deliver_erja=auth_user.id"
  str_sql2="SELECT *,(SELECT auth_user.last_name from auth_user where auth_user.id=polls_t_input_paper.user_send_id) as lastname, (SELECT auth_user.first_name from auth_user where auth_user.id=polls_t_input_paper.user_send_id) as firstname, (SELECT auth_user.first_name from auth_user where auth_user.id=polls_t_input_paper.user_deliver_id) as dfirstname, (SELECT auth_user.last_name from auth_user where auth_user.id=polls_t_input_paper.user_deliver_id) as dlastname FROM polls_t_input_paper where id= "+str(id)
  #mydata = T_input_paper.objects.filter(id=id).values()
  mydata = T_user_erja.objects.raw(str_sql2)
  user_show=User.objects.all()
  #temp_show_paper=T_user_erja.objects.filter(paper_erja=id).values()
  temp_show_paper = T_user_erja.objects.raw(str_sql)
  show_user_erja = T_user_erja.objects.filter(user_deliver_erja=request.user.id , paper_erja=id)
  date_update = T_input_paper.objects.get(id=id)
  date_update.date_paper_see=date2jalali(timezone.now()).strftime( '%Y-%m-%d')
  date_update.save()
  context = {
    'show_user_erja':show_user_erja,
    'temp_show_paper':temp_show_paper,
    'str_result':str_result,
	'user_show':user_show,
    'mydatashowpaper': mydata,
	'mydataerja': mydata,
	'activpople':'active',
	
	
	
  }
  template = loader.get_template('show_paper.html')
  return HttpResponse(template.render(context, request))
  #return render(request,context, 'show_paper.html', {'form': form})
  
def erja_user(request,paper_id,user_id):
  user_deliver_erja=request.POST['user_erja']
  jalali_date = date2jalali(timezone.now()).strftime( '%Y-%m-%d')
  t_user_erja = T_user_erja(
	user_send_id =request.user.id,
	date_send = jalali_date,
	date_see = jalali_date,
	paper_erja = paper_id,
	user_deliver_erja = user_deliver_erja,
	tozih=request.POST['tozih']
	)
  if(ckeck_valid.check_erj(request,user_deliver_erja,paper_id,)):
    t_user_erja.save()
    str_result='ok'
    return HttpResponseRedirect(reverse('show_paper',args=(paper_id,)))
  else:
    str_result='not'
    return HttpResponseRedirect(reverse('show_paper',args=(paper_id,)))
  
  
def paper_send(request):
  jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
  jalali_join = date2jalali(timezone.now()).strftime( '%Y-%m-%d')
  #step_ok=request.user.has_perm('polls.show_step')

  form = SummerForm()
  formdate = DateForm()
  mypapers = T_type_paper.objects.all().values()
  mydatapaper = T_input_paper.objects.all().values()
  mydatapople = T_user_pople.objects.all().values()
  mydatauser=User.objects.all().values()
  context = {
	
    'mydatauser': mydatauser,
	'mydata': mypapers,
	'mydatapople': mydatapople,
	'activepaper':'active',
	'mydatapaper': mydatapaper,
	'form': form,
	'formdate': formdate,
	'jalali_join':jalali_join,
	
  }
  template = loader.get_template('paper_send.html')
  
  return HttpResponse(template.render(context, request))
def addrecord_paper_send(request):
  formdate = DateForm(request.POST)
  form = SummerForm(request.POST)
  t_input_paper = T_input_paper(
	user_send_id = request.POST['user_send_id'],
	no_andikator = request.POST['no_andikator'],
	type_paper_id = request.POST['type_paper_id'],
	date_paper =request.POST['date_paper'],
	date_andikator =  request.POST['date_andikator'],
	user_deliver_id = request.POST['user_deliver_id'],
	no_paper_deliver = '',
	permination = request.POST['permination'],
	mozo = request.POST['mozo'],
	tozihat = request.POST['tozihat'],
	content_paper = request.POST['summer'],
	photo_file = request.FILES['photo_paper'],
	peyvast = request.POST['tozihat'],
	peyvast_file = request.FILES['peyvast'],)
  t_input_paper.save()
  return HttpResponseRedirect(reverse('paper_send'))
 
def sign_digital(request):
  mydatauser = User.objects.all().values()
  mydatasign = T_sign_digital.objects.all().values()
  context = {
    
	'mydatasign': mydatasign,
	'mydata': mydatauser,
	'activpople':'active',
	
	
  }
  template = loader.get_template('sign_digital.html')
  
  return HttpResponse(template.render(context, request))
  
def addrecord_sign_digital(request):
  t_sign_digital = T_sign_digital(
	user_sign_id = request.POST['user_sign_id'],
	photo_sign = request.FILES['photo_sign'],)
  
  t_sign_digital.save()
  return HttpResponseRedirect(reverse('sign_digital'))
def enter_paper(request):
  jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
  jalali_join = date2jalali(timezone.now()).strftime( '%Y-%m-%d')
  #step_ok=request.user.has_perm('polls.show_step')

  form = SummerForm()
  formdate = DateForm()
  mypapers = T_type_paper.objects.filter(type_paper='داخلی').values()
  mydatapaper = T_input_paper.objects.all().values()
  mydatapople = T_user_pople.objects.all().values()
  mydatauser=User.objects.all().values()
  context = {
	
    'mydatauser': mydatauser,
	'mydata': mypapers,
	'mydatapople': mydatapople,
	'activepaper':'active',
	'mydatapaper': mydatapaper,
	'form': form,
	'formdate': formdate,
	'jalali_join':jalali_join,
	
  }
  template = loader.get_template('enter_paper.html')
  
  return HttpResponse(template.render(context, request))
def addrecord_enter_paper(request):
  formdate = DateForm(request.POST)
  form = SummerForm(request.POST)
  t_input_paper = T_input_paper(
	user_send_id = request.user.id,
	no_andikator = request.POST['no_andikator'],
	type_paper_id = request.POST['type_paper_id'],
	date_paper =request.POST['date_paper'],
	date_andikator =  request.POST['date_andikator'],
	user_deliver_id = request.POST['user_deliver_id'],
	no_paper_deliver = '',
	permination = request.POST['permination'],
	mozo = request.POST['mozo'],
	tozihat = request.POST['tozihat'],
	content_paper = request.POST['summer'],
	photo_file = request.FILES['photo_paper'],
	peyvast = request.POST['tozihat'],
	peyvast_file = request.FILES['peyvast'],)
  t_input_paper.save()
  return HttpResponseRedirect(reverse('enter_paper'))