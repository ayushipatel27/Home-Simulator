
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
	
	#path('api_build/', include('api_build.urls')),

    path('admin/', admin.site.urls),

    path('api/',  include(('api_build.api.urls', 'api_build'), namespace='api_calls')),
]
