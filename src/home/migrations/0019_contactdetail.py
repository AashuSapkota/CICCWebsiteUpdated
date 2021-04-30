# Generated by Django 3.1.8 on 2021-04-21 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0018_delete_contactdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('contact_number1', models.CharField(max_length=15)),
                ('contact_number2', models.CharField(max_length=15)),
                ('contact_number3', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('mail_address', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
