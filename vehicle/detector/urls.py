from django.urls import path
from .import views
from django.urls import path, include

urlpatterns = [
   path('',views.login),
   path('reg',views.reg),
   path('show',views.Showdata),
   path('ins',views.ins),
   path('forgot',views.forgot),
   path('reset',views.reset),

   
]
