# django_rest_ec/urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def home(request):
    return HttpResponse("Hello, world!")


urlpatterns = [
    path('', home),  # ルートURLに対応するビューを追加
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/', include('api.urls')),                      # api アプリへのルートを追加
    path('accounts/', include('accounts.urls')),            # accounts アプリへのルートを追加
    path('ec_app/', include('ec_app.urls')),                # ec_app アプリへのルートを追加
]
