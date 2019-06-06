from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user.views import testing_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testing_index, name='test-page'),

    path('products/', include('product.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart11.urls')),
    path('order/', include('payment.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
