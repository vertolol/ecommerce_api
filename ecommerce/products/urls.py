from .views import ProductView
from rest_framework import routers


app_name = 'product'

router = routers.DefaultRouter()
router.register(r'', ProductView, basename='product')

urlpatterns = router.urls