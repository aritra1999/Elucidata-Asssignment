# Generated by Django 3.1.3 on 2020-11-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20201113_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_file', models.CharField(blank=True, max_length=120, null=True)),
                ('file_created', models.IntegerField(blank=True, null=True)),
                ('verdict', models.BooleanField(default=True)),
                ('task', models.IntegerField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]