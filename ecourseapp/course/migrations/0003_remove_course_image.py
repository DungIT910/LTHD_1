# Generated by Django 5.0.3 on 2024-03-26 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
    ]
