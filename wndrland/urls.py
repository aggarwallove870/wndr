from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from wndrland_app.sitemap import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticViewSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wndrland_app.urls')),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
     path('robots.txt', TemplateView.as_view(template_name="robots.txt" , content_type="text/plain")),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
