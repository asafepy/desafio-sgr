from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from apps.radio import views
from apps.core.views import LoginAuthToken, ObtainAuthToken, UserCreateViewSet



router = routers.DefaultRouter()
router.register(r'radio', views.RadioViewSet)
router.register(r'programa', views.ProgramaViewSet)
router.register(r'programacao', views.ProgramacaoViewSet)



helper_patterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', UserCreateViewSet.as_view(), name='user'),
	path('api-token-auth/', ObtainAuthToken.as_view()),
    path('authenticate/', LoginAuthToken.as_view(), name='authenticate'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns = helper_patterns
urlpatterns.extend(router.urls)