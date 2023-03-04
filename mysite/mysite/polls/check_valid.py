from django.contrib.auth.models import User
from .models import *
class ckeck_valid():
   def check_erj(request,id_user,id_paper):
      check=None
      
      if (T_user_erja.objects.filter(user_deliver_erja=id_user , user_send_id=request.user.id , paper_erja=id_paper)):
         return False
      else :
         return True