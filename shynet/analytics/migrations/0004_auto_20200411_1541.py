# Generated by Django 3.0.5 on 2020-04-11 19:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0003_auto_20200410_1325"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hit", old_name="start", new_name="start_time",
        ),
        migrations.RenameField(
            model_name="session", old_name="first_seen", new_name="start_time",
        ),
        migrations.RemoveField(model_name="hit", name="duration",),
        migrations.AddField(
            model_name="hit",
            name="last_seen",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
