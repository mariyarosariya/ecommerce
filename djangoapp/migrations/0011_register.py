# Generated by Django 4.2.4 on 2023-09-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0010_regmodel1_delete_file_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]