from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.details, name='testing'),    
	path('members/delete/<int:id>', views.delete, name='delete'),
	path('members/update/<int:id>', views.update, name='update'),
	path('members/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
	path('members/add/', views.add, name='add'),
	path('members/add/addrecord/', views.addrecord, name='addrecord'),
	path('members/add/search/', views.search, name='search'),
	path('members/paperindex/', views.paperindex, name='paperindex'),
	path('members/paperindex/addrecord_input_paper/', views.addrecord_input_paper, name='addrecord_input_paper'),
	path('members/input_user_pople/', views.input_user_pople, name='input_user_pople'),
	path('members/input_user_pople/addrecord_input_user_pople/', views.addrecord_input_user_pople, name='addrecord_input_user_pople'),
	path('members/datagrade_cartabl/<int:id>/<int:see>/', views.datagrade_cartabl, name='datagrade_cartabl'),
	path('members/show_paper/<int:id>', views.show_paper, name='show_paper'),
	path('members/erja_user/<int:paper_id>/<int:user_id>', views.erja_user, name='erja_user'),
	path('members/summernote/', include('django_summernote.urls')),
	path('members/paper_send/', views.paper_send, name='paper_send'),
	path('members/paper_send/addrecord_paper_send/', views.addrecord_paper_send, name='addrecord_paper_send'),
	path('members/enter_paper/', views.enter_paper, name='enter_paper'),
	path('members/enter_paper/addrecord_enter_paper/', views.addrecord_enter_paper, name='addrecord_enter_paper'),
	path('members/sign_digital/', views.sign_digital, name='sign_digital'),
	path('members/sign_digital/addrecord_sign_digital/', views.addrecord_sign_digital, name='addrecord_sign_digital'),
	path('accounts/', include('django.contrib.auth.urls')),

	
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
