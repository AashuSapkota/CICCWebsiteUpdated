# Generated by Django 3.1.8 on 2021-04-21 04:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0010_auto_20210421_1002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicesList',
            new_name='Services',
        ),
    ]
