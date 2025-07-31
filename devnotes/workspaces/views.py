from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from workspaces.models import Workspace
from users.models import CustomUser
from workspaces.serializers import ListWorkspacesSerializer, CreateWorkspaceSerializer


# Create your views here.
@api_view(["GET"])
def list_workspaces(request):
    workspaces = Workspace.objects.all()
    serializer = ListWorkspacesSerializer(workspaces, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_workspace(request):
    serializer = CreateWorkspaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(["GET"])
def get_workspace_details(request, pk):
    workspace = get_object_or_404(Workspace, pk=pk)
    serializer = ListWorkspacesSerializer(workspace)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_a_workspace(request, pk):
    workspace = get_object_or_404(Workspace,pk=pk)
    serializer = CreateWorkspaceSerializer(instance=workspace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors)
    
    
@api_view(["DELETE"])
def delete_a_workspace(request, pk):
    workspace = get_object_or_404(Workspace, pk=pk)
    workspace.delete()
    return Response({"msg": "Workspace deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def add_collaborator_to_a_workspace(request, workspace_id, user_id):
    workspace = Workspace.objects.get(pk=workspace_id)
    if not CustomUser.objects.filter(id=user_id).exists():
        return Response({"error": "User not found"}, status=404)
    workspace.collaborators.add(user_id)
    return Response({"msg":"Collaborator added successfully"})

    
@api_view(["DELETE"])
def remove_collaborator_from_a_workspace(request, workspace_id, user_id):
    workspace = Workspace.objects.get(pk=workspace_id)
    workspace.collaborators.remove(user_id)
    return Response({"msg":"Collaborator removed successfully"})