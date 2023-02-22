
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("chat/", include("chat.urls")),
    path('api-auth/', include('rest_framework.urls')),
    # re_path(r'api/v1/rest-auth/', include('rest_auth.urls')),

]
