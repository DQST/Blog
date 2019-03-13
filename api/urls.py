from django.urls import path, include
from api.views import UserListView


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('users/', UserListView.as_view()),
    path('user/', include('post.urls')),
]
