# Generated by Django 2.2.17 on 2020-12-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("enhydris", "0103_verbose_names"),
    ]

    operations = [
        migrations.RemoveField(model_name="station", name="copyright_holder"),
        migrations.RemoveField(model_name="station", name="copyright_years"),
    ]
