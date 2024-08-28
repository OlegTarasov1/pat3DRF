from .models import Course, Lessons
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default = serializers.CurrentUserDefault())
    amnt_of_lessons = serializers.SerializerMethodField()

    def get_amnt_of_lessons(self, obj):
        return obj.lessons.count()


    class Meta:
        model = Course
        fields = ('creator', 'course_title', 'course_intro', 'course_slug', 'price', 'comment', 'amnt_of_lessons')


