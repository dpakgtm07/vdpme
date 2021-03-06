from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from mande import views
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout,name='logout'),
]
new_patterns = i18n_patterns(url(r'^', include('mande.urls')))
urlpatterns = urlpatterns+new_patterns
if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
