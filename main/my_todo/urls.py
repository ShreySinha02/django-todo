from django.urls import re_path
from my_todo import views
urlpatterns = [
    re_path(r"login/$",views.LoginPage,name="login"),
    re_path(r"$",views.SignupPage,name="signup"),
    re_path(r"home/$",views.Home,name='home'),
    re_path(r"add",views.Add_notes,name='add'),
    re_path(r"done/(?P<pk>\d+)/$",views.Delete_note,name='done'),
    re_path(r"logout/",views.logout_view,name='logout')
]