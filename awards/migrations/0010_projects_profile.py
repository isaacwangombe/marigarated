# Generated by Django 4.0.2 on 2022-06-15 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0009_alter_review_content_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.profile'),
        ),
    ]
