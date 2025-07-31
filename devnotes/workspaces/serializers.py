from rest_framework import serializers
from workspaces.models import Workspace
from users.models import CustomUser

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "email"]
        

class ListWorkspacesSerializer(serializers.ModelSerializer):
    collaborators = CollaboratorSerializer(read_only=True, many=True)
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'created_at', 'collaborators']
        
        
class CreateWorkspaceSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=False)
    class Meta:
        model = Workspace
        fields = ["name", "description"]