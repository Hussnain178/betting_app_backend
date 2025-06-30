from django.urls import path

from .views import *

urlpatterns = [
    path('create_user/', create_user_view, name='create_user'),
    path('update_age', update_age_view, name='update_age'),
    path('delete_user/', delete_user_view, name='delete_user'),
    path('get_age/', get_age_view, name='get_age'),
    path('test_view/', test_view, name='test_view')
]
