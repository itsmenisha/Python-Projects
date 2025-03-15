from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),  # Fixed empty string for root
    path("calander/", include("mycalendar.urls")),  # Removed leading slash
    path("calendar/", include("mycalendar.urls")),  # Removed leading slash

]

# Debug Toolbar URL Configuration
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
