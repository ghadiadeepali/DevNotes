from users import models
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {"input_type":"password"}, write_only=True)
    # needs to be write_only so that user can write it but cannot read it
    # This is commonly used in signup (registration) serializers to confirm the user typed the same password twice.
    class Meta:
        model = models.CustomUser
        fields = ["name", "email", "password" , "password2"]
        extra_kwargs = {'password':{'write_only':True}}
        