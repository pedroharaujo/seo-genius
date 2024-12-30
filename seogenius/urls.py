from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main_pages.urls', 'main_pages'), namespace='main_pages')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('accounts/', include('allauth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
