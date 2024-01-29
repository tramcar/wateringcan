# Generated by Django 4.2 on 2024-01-28 19:50

from django.db import migrations, models

import markdown


def set_default_value(apps, schema_editor):
    Page = apps.get_model('wateringcan', 'Page')

    # Perform custom operations using model fields
    for page in Page.objects.all():
        page.content_html = markdown.markdown(page.content)
        page.save()


def reverse_set_default_value(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('wateringcan', '0003_alter_page_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='page',
            name='content_html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.RunPython(code=set_default_value, reverse_code=reverse_set_default_value),
    ]