"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from config import views
from django.conf import settings

urlpatterns = [
    # http://localhost/admin
    path("admin/", admin.site.urls),

    #  시작페이지 : http://localhost
    # path(request, response, name)
    path("", views.home),
    # http://localhost/address
    path("address/", include("address.urls")),
    #http://localhost/memo
    path("memo/", include('memo.urls')),
    #httpL//localhost/survey
    path("survey/", include('survey.urls')),
    #http://localhost/guestbook
    path("guestbook/", include('guestbook.urls')),
    path("member/", include('member.urls')),
    path("shop/", include('shop.urls')),
]

# settings.py 파일에 INSTALLED_APPS에 debug_toolbar가 존재한다면
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
