# Generated by Django 4.2.4 on 2023-09-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0009_file_upload_delete_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('kerala', 'kerala'), ('karnataka', 'karnataka'), ('goa', 'goa')], max_length=30)),
                ('english', models.BooleanField(default=False)),
                ('malayalam', models.BooleanField(default=False)),
                ('hindi', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='file_upload',
        ),
    ]
