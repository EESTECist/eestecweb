from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views

urlpatterns = [
#    path('',home.views.home, name='home'),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
