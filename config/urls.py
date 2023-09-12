from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static  import static
from api.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-detail'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
