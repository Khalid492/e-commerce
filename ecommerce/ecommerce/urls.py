from django.conf import settings
from  django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('cart/',include('cart.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)