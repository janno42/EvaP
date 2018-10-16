# Generated by Django 2.0.9 on 2018-10-15 19:08

from django.db import migrations, models
import django.utils.timezone


def create_cronjob_user(apps, _schema_editor):
    UserProfile = apps.get_model('evaluation', 'UserProfile')

    UserProfile.objects.create(username="cronjob")


def delete_cronjob_user(apps, _schema_editor):
    UserProfile = apps.get_model('evaluation', 'UserProfile')

    try:
        UserProfile.objects.get(username="cronjob").delete()
    except UserProfile.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0084_rename_course_comments_to_general_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_modified_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RunPython(delete_cronjob_user, reverse_code=create_cronjob_user),
    ]
