#
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def home(request):
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', home),  # ルートURLに対応するビューを追加
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
