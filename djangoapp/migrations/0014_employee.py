# Generated by Django 4.2.4 on 2023-09-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0013_file1_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=20)),
                ('desig', models.CharField(max_length=20)),
            ],
        ),
    ]