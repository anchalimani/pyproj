from django.urls import path
from .import views
urlpatterns = [
    path('H/',views.hello),
    path('home/', views.home),
    path('hello/', views.python),
    path('new/', views.anchu),
    path('details/', views.fun)
]