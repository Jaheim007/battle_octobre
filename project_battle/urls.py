from django.contrib import admin
from django.urls import path

from front.views import ContactView, HomeView, SingleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('single/',SingleView.as_view(), name='single'),
    path('contact/', ContactView.as_view(), name='contact'),
]
