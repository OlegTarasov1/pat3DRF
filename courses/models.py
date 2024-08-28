from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Course(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'courses_created')
    course_title = models.CharField(max_length = 100)
    course_intro = models.CharField(max_length = 500)
    course_slug = models.SlugField(unique = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    subscribers = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING, related_name = 'subscribed_courses')
    comment = models.ForeignKey('Comments', on_delete = models.DO_NOTHING, related_name = 'course')

    def save(self, *args, **kwargs):
        if not self.course_slug:
            self.course_slug = slugify(self.course_title)
        super().save(*args, **kwargs)


class Lessons(models.Model):
    courses = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'lessons')
    lesson_title = models.CharField(max_length = 100)
    lesson_intro = models.CharField(max_length = 500)
    lesson_text = models.TextField()
    files = models.FileField(upload_to = 'uploads/')
    viewed_by = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, null = True, related_name = 'lessons')


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING, related_name = 'feedback')
    comment = models.TextField()


class Score(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING, related_name = 'score')
    course = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'score')
    
    class Rating(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,
    
    score = models.IntegerField(choices = Rating.choices)

    class Meta:
        unique_together = ['user', 'course']
