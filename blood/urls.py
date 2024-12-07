from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


#urls for apges
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('team', views.team_page, name='team_page'),
    path('gallery', views.gallery_page, name='gallery_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('donate', views.donate_page, name='donate_page'),
    path('show_donations/', views.retrieve_donations, name='show_donations'),
    path('delete/<int:id>/', views.delete_donations, name='delete_donation'),
    path('update/<int:donation_id>/', views.update_donation, name='update_donation'),
    path('upload/', views.upload_image, name='upload_image'),
    path('search-blood-donations/', views.search_blood_donations, name='search_blood_donations'),
    path('search-blood-donation/', views.search_blood_donation, name='search_blood_donation'),
    path('book_donor/<int:donor_id>/', views.book_donor, name='book_donor'),
    path('add-donor/', views.add_donor, name='add_donor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('requests/', views.requests, name='requests'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordResetDoneView.as_view(), name='password_change_done'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
