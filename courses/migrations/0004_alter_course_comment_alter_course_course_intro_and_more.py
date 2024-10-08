# Generated by Django 5.1 on 2024-08-28 18:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_cours_intro_course_course_intro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='course', to='courses.comments'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_intro',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='course',
            name='subscribers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscribed_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='files',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_intro',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='viewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]
