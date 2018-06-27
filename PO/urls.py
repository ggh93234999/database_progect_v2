"""PO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from databases import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'user_profile',views.User_profilesViewSet)
router.register(r'event',views.EventsViewSet)
router.register(r'team',views.TeamsViewSet)
router.register(r'teammember',views.TeammembersViewSet)
router.register(r'announcement',views.AnnouncementsViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api-token-auth/',obtain_jwt_token),
    path('signup/',views.Signup),


]
