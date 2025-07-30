from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from workspaces.models import Workspace
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
    