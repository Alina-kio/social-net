"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import swagger
from django.conf import settings
from django.conf.urls.static import static
from socialmedia import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', views.UserAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/users/<int:pk>/', views.ProfileAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/authorization/', views.AuthorizationAPIView.as_view()),
    path('api/v1/registration/', views.RegistrationAPIView.as_view()),
    path('api/v1/posts/', views.PostAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/posts/<int:pk>/', views.PostAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/search/', views.Search1.as_view()),
]





# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/users/', views.user_list_view),
#     path('api/v1/users/<int:id>/', views.user_profile_item_view),
#     path('api/v1/authorization/', views.authorization),
#     path('api/v1/registration/', views.registration),
#     path('api/v1/posts/', views.posts_view),
#     path('api/v1/posts/<int:id>/', views.post_item_view),
#     path('api/v1/search/', views.Search1.as_view()),
# ]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += swagger.urlpatterns

