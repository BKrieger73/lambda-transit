from django.conf.urls import url

from stations import views

urlpatterns = [
    url(r'^$', views.StationList.as_view()),
]
