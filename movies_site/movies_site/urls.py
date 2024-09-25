from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from movies import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),  # Routes all requests starting with movies/ to the movies app
    path('accounts/', include('accounts.urls')),  # Routes all account-related URLs
    path('', movie_views.movie_list, name="home"),  # Root URL shows the movie list as the homepage
]

urlpatterns += staticfiles_urlpatterns()  # Serves static files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serves media files during development
