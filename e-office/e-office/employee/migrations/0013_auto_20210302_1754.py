# Generated by Django 3.1.3 on 2021-03-02 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0007_opening_job_location'),
        ('employee', '0012_job_opening_model_job_posting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.opening'),
        ),
        migrations.DeleteModel(
            name='job_opening_model',
        ),
    ]