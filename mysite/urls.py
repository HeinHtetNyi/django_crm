from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register', views.register_user, name="register"),
    path('record/<int:pk>', views.record_detail, name="record-detail"),
    path('delete_record/<int:pk>', views.delete_record, name="delete-record"),
    path('add_record', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update-record'),
]
