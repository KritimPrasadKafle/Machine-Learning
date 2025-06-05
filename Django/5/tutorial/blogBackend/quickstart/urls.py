from django.urls import path, include
from .views import UserAPI, ProfileAPI, UserWithProfile, PostAPI, GroupAPI, TriggerNotification, TriggerTask
urlpatterns = [
    path('', UserAPI.as_view(), name = 'user-api'),
    path('profile/', ProfileAPI.as_view(), name = 'profile-api'),
    path('all/profile/<int:id>/', UserWithProfile.as_view(), name ='user-profile'),
    path('posts/', PostAPI.as_view(), name='posts'),
    path('groups/', GroupAPI.as_view(), name='posts'),
    path('notify/', TriggerNotification.as_view()),
    path('trigger-task/', TriggerTask.as_view(), name='trigger-task'),

]