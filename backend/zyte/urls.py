
from rest_framework import routers
from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register("spiders", views.SpiderViewSet)
router.register("job-data", views.JobDataViewSet)
urlpatterns = router.urls