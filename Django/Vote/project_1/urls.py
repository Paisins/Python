from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vote/', include('vote.urls')),
    path('admin/', admin.site.urls),
]
