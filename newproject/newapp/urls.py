from django.contrib import admin
from django.urls import path,include
from newapp import views

urlpatterns = [
    path('dep_add',views.dep_add,name='dep_add'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('logins',views.logins,name='logins'),
    path('teachhome',views.teachhome,name='teachhome'),
    path('studhome',views.studhome,name='studhome'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updatetr',views.updatetr,name='updatetr'),
    path('updateteacher/<int:aid>',views.updateteacher,name='updateteacher'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('lgout',views.lgout,name='lgout'),
    path('deletest/<int:id>',views.deletest,name='deletest'),
    path('deletetr/<int:id>',views.deletetr,name='deletetr'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
    path('depbyteacher',views.depbyteacher,name='depbyteacher'),
    path('',views.index,name='index'),






]