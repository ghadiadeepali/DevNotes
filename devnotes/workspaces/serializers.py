from rest_framework import serializers
from workspaces.models import Workspace

class ListWorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = "__all__"
        
        
class CreateWorkspaceSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Workspace
        fields = ["name", "description"]