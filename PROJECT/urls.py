from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_page),
    path('profile/', views.profile_page),
    path('contacts/', views.contacts_page),
    path('my-notes/', views.my_notes),
    path('my-notes/<int:note_id>/', views.my_note),

    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('register/', views.register_user),

    path('profile-update/', views.profile_update),

    path('new-note/', views.new_note),
    path('create-note/', views.create_note),
    path('delete-note/<int:note_id>/', views.delete_note),
]
