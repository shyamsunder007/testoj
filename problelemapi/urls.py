from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^problems/add/$', views.add_problem),
    url(r'^problems/$', views.Problem_list),

]