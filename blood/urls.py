from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

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
    path('add-donor/', views.add_donor, name='add_donor'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)