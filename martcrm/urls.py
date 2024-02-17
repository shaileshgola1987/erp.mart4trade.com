from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('add_category',views.add_category,name='add_category'),
    path('error',views.error,name='error'),
    path('success',views.success,name='success'),
    path('category_list',views.category_list,name='category_list'),
    path('create_company', views.create_company, name='create_company'),
    path('select_state',views.select_state,name='select_state'),
    path('select_city',views.select_city,name='select_city'),
    path('upload_bulk_profiles',views.upload_bulk_profiles,name='upload_bulk_profiles'),
    path('check_email',views.check_email,name='check_email'),
    path('select_categories',views.select_categories,name='select_categories'),
    path('profile_list',views.profile_list,name='profile_list'),
    path('view_profile/<int:profile_id>',views.view_profile,name='view_profile'),
    ]