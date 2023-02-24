from . import views
from django.urls import path

urlpatterns = [
    path('',views.about,name='about'),
    # path('about/',views.about,name='about'),
    # path('add/',views.addition,name='addition'),
    # path('mul/',views.addition,name='multiplication'),
    # path('sub/',views.addition,name='substraction'),
    # path('div/',views.addition,name='division'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')
]
