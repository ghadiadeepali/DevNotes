from django.urls import path
from workspaces import views
urlpatterns = [
    path("",views.list_workspaces),
    path("create/", views.create_workspace),
    path("<int:pk>", views.get_workspace_details)
]