from rest_framework import routers

from products.views import ProductViewSet, CategoryViewSet, SizeViewSet, GenderViewSet

router = routers.DefaultRouter()


router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'size', SizeViewSet)
router.register(r'gender', GenderViewSet)

urlpatterns = [
    *router.urls
]