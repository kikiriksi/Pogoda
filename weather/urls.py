from django.urls import path
from . import views

urlpatterns = [
    path('', views.Info.as_view()),
    path('del/<str:city>', views.delit, name='delit'),
]
