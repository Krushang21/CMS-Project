# Generated by Django 4.1 on 2023-04-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
