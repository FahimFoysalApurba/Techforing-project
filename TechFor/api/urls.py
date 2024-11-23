from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterView, ProjectViewSet, TaskViewSet, CommentViewSet

urlpatterns = [
    # Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Endpoints
    path('users/register/', UserRegisterView.as_view(), name='user_register'),
    path('projects/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='projects'),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project_detail'),
    path('tasks/<int:project_id>/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task_detail'),
    path('comments/<int:task_id>/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment_detail'),
]
