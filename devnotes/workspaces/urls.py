from django.urls import path
from workspaces import views
urlpatterns = [
    path("",views.list_workspaces),
    path("create/", views.create_workspace),
    path("<int:pk>", views.get_workspace_details),
    path("update/<int:pk>", views.update_a_workspace),
    path("delete/<int:pk>", views.delete_a_workspace),
    path("add-collaborator/<int:workspace_id>/<int:user_id>", views.add_collaborator_to_a_workspace),
    path("remove-collaborator/<int:workspace_id>/<int:user_id>", views.remove_collaborator_from_a_workspace)
    
]