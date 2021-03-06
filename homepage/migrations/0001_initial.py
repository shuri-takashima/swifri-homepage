# Generated by Django 3.2.5 on 2021-12-07 01:00

from django.db import migrations, models
import homepage.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('image', models.ImageField(upload_to=homepage.models.image_directory_path, verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'Art',
            },
        ),
    ]
