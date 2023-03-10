# Generated by Django 4.1.5 on 2023-01-09 07:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0004_auto_20230109_1507"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snippet",
            name="new_id",
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="snippet",
            name="persistence_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name="snippet",
            name="id",
        ),
        migrations.AlterField(
            model_name="snippet",
            name="persistence_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.RenameField(model_name="snippet", old_name="new_id", new_name="id"),
    ]
