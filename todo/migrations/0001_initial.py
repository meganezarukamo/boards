# Generated by Django 5.1.5 on 2025-01-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='user name')),
                ('micropost', models.CharField(blank=True, max_length=140, verbose_name='tweet')),
            ],
        ),
    ]
