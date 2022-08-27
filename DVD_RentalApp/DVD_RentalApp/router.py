from api.viewsets import MovieViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movie', MovieViewset)