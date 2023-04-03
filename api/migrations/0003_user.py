# Generated by Django 4.1.7 on 2023-04-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_uploadedfile_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
