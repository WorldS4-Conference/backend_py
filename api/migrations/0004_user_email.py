# Generated by Django 4.1.7 on 2023-04-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='no-email@example.com', max_length=255),
        ),
    ]
