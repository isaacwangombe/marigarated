# Generated by Django 4.0.2 on 2022-06-15 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0011_remove_review_avg_design'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='profile',
        ),
    ]