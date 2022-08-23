from os import stat
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="Home"),
    path('show/<str:pk>', views.show, name="Show")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
