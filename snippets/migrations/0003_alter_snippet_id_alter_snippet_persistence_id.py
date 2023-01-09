# Generated by Django 4.1.5 on 2023-01-09 06:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0002_snippet_persistence_id_alter_snippet_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippet",
            name="new_id",
            field=models.UUIDField(
                default=uuid.uuid4, null=True, verbose_name="ID"
            ),
        ),
        migrations.AddField(
            model_name="snippet",
            name="persistence_id",
            field=models.BigIntegerField(null=True, serialize=False),
        ),
    ]
