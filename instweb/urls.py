from django.contrib import admin
from django.urls import path, re_path, include
from instant import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from instant.models import Image, Comment


from django.contrib.auth.models import User

from instant.views import RegisterUser, LoginUser

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('success', views.success, name = 'success'),
    re_path(r'^image_upload/$', views.image_view, name='image_upload'),
    #path('hotel_images', views.authors, name = 'hotel_images'),
    re_path(r'^images/$', views.display_images, name='images'),
    re_path(r'^images2/$', views.display_images2, name='images2'),
    re_path(r'^imagesPost/$', views.PostList.as_view(), name='imagesPost'),
    re_path(r'^image/(?P<pk>\d+)$', views.ImageDetailView.as_view(), name='image_detail'),
    re_path(r'^image/imagess/(\d+)$', views.authors, name='author'),
    re_path(r'^image/imagess/(\d+)$', views.usr, name='usr'),
    re_path(r'^followers', views.followers, name='followers'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('create/', views.create, name='create'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
    re_path("image/imagess/post", views.followed, name="followed"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
