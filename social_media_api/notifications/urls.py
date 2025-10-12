from django.urls import include, path

urlpatterns = [
    path('/notifications/', include('notifications.urls')),
]