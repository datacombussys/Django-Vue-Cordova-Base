from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
# from users.views import TeamSet
from blog.views import BlogSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
# router.register(r'teams', TeamSet)
router.register(r'blog', BlogSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^api/swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^api/redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url(r'^api/', include((router.urls, 'app_name'),
                          namespace='instance_name')),
    url(r'^api/accounts/', include('rest_registration.api.urls')),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
