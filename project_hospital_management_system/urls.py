from django.contrib import admin
from django.urls import path
from hospital.views import home , main , patient_dashboard , doctor_dashboard , usignup , ulogin , ulogout , ucp , remp
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name = 'home'),
    path('main' , main , name = 'main'),
    path('patient_dashboard', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard', doctor_dashboard, name='doctor_dashboard'),
    path('usignup' , usignup , name = 'usignup'),
    path('ulogin' , ulogin , name = 'ulogin'),
    path('ulogout' , ulogout , name = "ulogout"),
    path('ucp' , ucp , name = 'ucp'),
    path('remp/<int:id>',remp,name='remp'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

