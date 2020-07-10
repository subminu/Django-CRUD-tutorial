from django.contrib import admin
from django.urls import path, include
import funcrud.urls
import funcrud.views
# import classcrud.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', funcrud.views.welcome, name='index'),
    path('funcrud/', include(funcrud.urls)),
    # path('classcrud/', include(classcrud.urls)),
]
