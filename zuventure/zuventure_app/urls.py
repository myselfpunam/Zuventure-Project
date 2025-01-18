from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "index"),
    path('<str:category_name>/', views.get_categories, name="get_categories"),
    path('<str:category_name>/<int:id>', views.get_products, name="get_products"),
    path('about', views.about, name="about"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('drop-cv', views.drop_cv, name='drop_cv'),

]
