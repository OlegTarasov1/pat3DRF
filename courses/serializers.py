from .models import Course, Lessons
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default = serializers.CurrentUserDefault())
    amnt_of_lessons = serializers.SerializerMethodField(read_only = True)
    course_slug = serializers.SlugField(required = False)
    comment = serializers.CharField(read_only = True)
    creator_username = serializers.SerializerMethodField()

    def get_creator_username(self, obj): 
        return obj.creator.username


    def get_amnt_of_lessons(self, obj):
        return obj.lessons.count()


    class Meta:
        model = Course
        fields = ('creator', 'creator_username', 'course_title', 'course_intro', 'course_slug', 'price', 'comment', 'amnt_of_lessons')


class LessonsSerializer(serializers.ModelSerializer):
    viewed_by = serializers.SerializerMethodField(read_only = True)

    def get_viewed_by(self, obj):
        return obj.viewed_by.count()

    class Meta:
        model = Lessons
        fields = ('__all__')


class LessonsSerializerShort(serializers.ModelSerializer):
    amnt_of_views = serializers.SerializerMethodField(read_only = True)

    def get_amnt_of_views(self, obj):
        return obj.viewed_by.count()

    class Meta:
        model = Lessons
        fields = ('courses', 'lesson_title', 'lesson_intro', 'amnt_of_views')