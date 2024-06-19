# Generated by Django 3.2.25 on 2024-06-14 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_childtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.FileField(upload_to='uploads/')),
                ('file_description', models.TextField()),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.childtitle')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]