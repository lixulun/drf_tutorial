# Generated by Django 4.1.5 on 2023-01-09 07:07

import uuid
from django.db import migrations


def generate_uuid_and_set_persistence_id(apps, schema_editor):
    Snippet = apps.get_model("snippets", "Snippet")
    for row in Snippet.objects.all():
        row.new_id = uuid.uuid4()
        row.persistence_id = row.id
        row.save(update_fields=['new_id', 'persistence_id'])


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0003_alter_snippet_id_alter_snippet_persistence_id"),
    ]

    operations = [
        migrations.RunPython(
            generate_uuid_and_set_persistence_id, reverse_code=migrations.RunPython.noop
        )
    ]
