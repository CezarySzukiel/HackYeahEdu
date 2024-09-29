from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, ClassGroupViewSet, HomeworkOpenAIView

router = DefaultRouter()
router.register(r'homework', HomeworkViewSet)
router.register(r'classgroup', ClassGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('homework/<int:pk>/openai/', HomeworkOpenAIView.as_view(), name='homework-openai'),
]
