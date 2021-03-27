from django.conf.urls import url,include
from sub import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^enter/$',views.enter,name="enter"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)