from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# keyingi holatlar uchun
from . import views
urlpatterns = [
	path('',HomePageView.as_view(),name='index'),
	
	# path('menu/',MenuPageView,name='menu'), # avvalgi holat
	path('menu/',views.menuPageView,name='menu'), # keyingi holat
	# updateItem uchun
	path('update_item/',views.updateItem),
	# cart funsiyasi uchun 
	path('cart/', views.cart, name="cart"),

	path('book/',BookPageView,name='book'),
	path('about/',AboutPageView.as_view(),name='about'),
	path('product_create/',ProductCreateView.as_view(),name='product_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 4- bosqichda menu html fayliga Add Cart bo'limini yozishimiz kerak
