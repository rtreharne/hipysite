from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import hello.views
import idea.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^resources/', include('resources.urls')),
    url(r'^idea/$', idea.views.idea, name='idea'),
    url(r'^register/(?P<hive_id>\d+)$', hello.views.register, name='register'),
    url(r'^hive/(?P<hive_id>\d+)$', hello.views.hive, name='hive'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'promo/$', hello.views.promo, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

