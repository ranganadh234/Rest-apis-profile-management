"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView,HelloViewSet,UserProfileViewSet,LoginViewSet,UserProfileFeedViewSet

router=DefaultRouter()
router.register('hello-viewset',HelloViewSet,base_name='hello-viewset')
router.register('profile',UserProfileViewSet,base_name='profile')
router.register('login',LoginViewSet,base_name='login')
router.register('feed',UserProfileFeedViewSet,base_name='feed')
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-view/',HelloApiView.as_view(),name='hello'),
    path('',include(router.urls)),
    #path('feed',UserProfileFeedViewSet.as_view(),name='feed')
]
