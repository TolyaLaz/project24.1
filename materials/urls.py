from config.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView

app_name = MaterialsConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
                  path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lessons_update'),
                  path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
              ] + router.urls
