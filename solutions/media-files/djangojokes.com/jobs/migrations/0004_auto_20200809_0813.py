# Generated by Django 3.1 on 2020-08-09 12:13

from django.db import migrations, models
import djangojokes.storage_backends
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200809_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', storage=djangojokes.storage_backends.PrivateMediaStorage(), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]