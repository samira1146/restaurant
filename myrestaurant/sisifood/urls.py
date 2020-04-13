from django.urls import path,re_path
from .import views

urlpatterns=[
    path('' , views.index , name='index'),
    path('pizza/' , views.pizza , name='pizza'),
    #path('topping/' , views.topping , name='sideDish'),
    re_path('pizza/(?P<id>[0-9]+)/$',views.pizza_page,name='pizza_pagesPages'),
    ##re_path('pizza/(?P<name>[\w-]+)/$',views.topping,name='pizza_topping'),
    path('dink/' , views.drink , name='dink'),
    path('signUp/' , views.user_sign_up, name='signUp'),
    path('logout/', views.user_logout, name='logout'),
    path('login/' , views.user_login, name='login'),

]