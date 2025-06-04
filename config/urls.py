from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, category_detail


from django.contrib import admin

from accounts.views import (

    register_view,
    login_view,
    logout_view,
    profile_view,
    cart_view,
    add_to_cart
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

   path('', include('app.urls')),
   path('accounts/', include('accounts.urls')),

    path('category/<int:category_id>/', category_detail, name='category_detail'),



    # Авторизация
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

