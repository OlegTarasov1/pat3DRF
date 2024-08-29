from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Course(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'courses_created')
    course_title = models.CharField(max_length = 100)
    course_intro = models.CharField(max_length = 500, blank = True)
    course_slug = models.SlugField(unique = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    subscribers = models.ManyToManyField(get_user_model(), related_name = 'subscribed_courses')
    comment = models.ForeignKey('Comments', on_delete = models.DO_NOTHING, related_name = 'course', null = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.course_slug:
            self.course_slug = slugify(self.course_title)
        super().save(*args, **kwargs)


class Lessons(models.Model):
    courses = models.ForeignKey('Course', on_delete = models.CASCADE, related_name = 'lessons')
    lesson_title = models.CharField(max_length = 100)
    lesson_intro = models.CharField(max_length = 500, blank = True)
    lesson_text = models.TextField(blank = True)
    files = models.FileField(upload_to = 'uploads/', blank = True)
    viewed_by = models.ManyToManyField(get_user_model(), related_name = 'lessons', blank = True)


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
