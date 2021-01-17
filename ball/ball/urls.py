from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #jwt urls ====================
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
    # all urls =================
    path('admin/', admin.site.urls),
    path('api/transports/', include('transports.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns +=[re_path(r'^.*', TemplateView.as_view(template_name='index.js'))]
