from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post',views.PostViewSet) # 2개의 url 만들기

urlpatterns = [
    path('public/', views.PublicPostListAPIView.as_view()),
    path('',include(router.urls))
]
