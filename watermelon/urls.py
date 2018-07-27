from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from rest_framework.schemas import get_schema_view



from songs import rest as SongRest
from artists import rest as ArtistRest

apiRouter = routers.DefaultRouter()
apiRouter.register(r'songs', SongRest.SongViewSet)
apiRouter.register(r'songstatus', SongRest.SongStatusViewSet)
apiRouter.register(r'platforms', SongRest.PlatformViewSet)
apiRouter.register(r'users', SongRest.UserViewSet)
apiRouter.register(r'artists', ArtistRest.ArtistViewSet)

schema_view = get_schema_view(title='Watermelon API')

urlpatterns = [
    url(r'^artists/', include('artists.urls')),
    url(r'^streams/', include('streams.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(apiRouter.urls)),
    url(r'^docs/', include_docs_urls(title='Watermelon API')),
    url(r'^schema/$', schema_view),
]
