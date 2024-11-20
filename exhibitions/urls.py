from django.urls import path
from exhibitions.views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('about-us/', AboutUsPage.as_view(), name='aboutus_page'),
    path('gallery/', GalleryPage.as_view(), name='gallery_page'),
    path('contact/', ContactPage.as_view(), name='contact_page'),
]