from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/', views.show_post,name='post'), 
    path('about/', views.about,name='about'), 
    path('contact/', views.contact,name='contact'),
    path('post/', views.show_post,name='post'), 
    path('add_post/', views.add_post,name='add_post'),    
    path('user_profile/', views.user_profile,name='user_profile'), 
    path('like/<int:pk>' ,views.like,name= 'like_post_btn'),  
    path('post_detail/<int:pk>' ,views.post_detail,name= 'post_detail'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
