from rest_framework import serializers
from projects.models import Project, Tag
from users.models import Profile


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
