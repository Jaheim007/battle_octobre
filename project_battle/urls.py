from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from front.views import ContactView, HomeView, SingleView , SignUp , Login , Logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('single/',SingleView.as_view(), name='single'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
