from django.contrib import admin
from .views import login_redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),),
    path('tips/', include('Predictions.urls', namespace='tips')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sub/', include('subscriptions.urls', namespace='subs')),
    path('payments/', include('Predictions.mpesa.api.urls',namespace='mpesa')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # url(r'^.*/', TemplateView.as_view(template_name="index.html"),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
