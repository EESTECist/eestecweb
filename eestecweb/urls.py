from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('',jobs.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('user/', include('user.urls', namespace='user')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
