from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'add$', views.add),
  url(r'success$', views.success),
  url(r'(?P<idx>\d+)/delete$', views.delete),
  url(r'login$', views.login),
  url(r'wish_items/create$', views.create),
  url(r'wish_items/add_item$', views.add_item),
  url(r'(?P<idx>\d+)/take_wish$', views.take_wish),
  url(r'(?P<idx>\d+)/remove_wish$', views.remove_wish),
  url(r'(?P<idx>\d+)/check$', views.check),
  url(r'logout$', views.logout)
 ]