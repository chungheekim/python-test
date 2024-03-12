from rest_framework import routers

from account.views import AccountsViewSet, SignupViewSet
from bike.views import BikeViewSet

router = routers.DefaultRouter()
router.register(r'bikes', BikeViewSet)
router.register(r'accounts', AccountsViewSet)
router.register(r'signup', SignupViewSet, basename='signup')

