from rest_framework import serializers

from users.serializers import CustomUserDetailSerializer
from .models import Homework, ClassGroup, HomeworkAssignment


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework

        fields = ('pk', 'title', 'description', 'assigned_to')


class ClassGroupSerializer(serializers.ModelSerializer):
    homeroom_teacher = CustomUserDetailSerializer()
    related_users = serializers.SerializerMethodField()

    class Meta:
        model = ClassGroup
        fields = ('pk', 'name', 'homeroom_teacher', 'related_users')

    def get_related_users(self, obj):
        assignments = HomeworkAssignment.objects.filter(homework__assigned_to__class_group=obj)
        users = {assignment.user for assignment in assignments}
        return CustomUserDetailSerializer(users, many=True).data
