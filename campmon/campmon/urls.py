
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from my_campaign_monitor import views


router=routers.DefaultRouter()
router.register (r'subscribers',views.SubscriberView,'subscriber')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
