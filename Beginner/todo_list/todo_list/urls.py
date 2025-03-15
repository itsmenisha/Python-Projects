from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),  # Fixed empty string for root
    path("calander/", include("mycalendar.urls")),  
    path("calendar/", include("mycalendar.urls")),  

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
