from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'togglier.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^zuke/', include('zuke.urls')),
                       (r'^accounts/', include('registration.backends.simple.urls'))
                       )
