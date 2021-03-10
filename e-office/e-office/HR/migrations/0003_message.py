# Generated by Django 3.1.3 on 2021-02-25 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_auto_20210215_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message_body', models.TextField(max_length=300)),
                ('sent_date', models.DateTimeField(auto_now=True)),
                ('receipent_id', models.IntegerField()),
                ('hr_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.hrp')),
            ],
        ),
    ]