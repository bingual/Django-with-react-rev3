from django.urls import path, include
from rest_framework.routers import DefaultRouter
from instagram import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 만들어줍니다.
router.urls

urlpatterns = [
    # path('public/', views.public_post_list),
    path('', include(router.urls)),
    path('mypost/<int:pk>/', views.post_detail)
]