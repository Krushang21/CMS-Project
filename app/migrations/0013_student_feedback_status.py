# Generated by Django 4.2 on 2023-04-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_student_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_feedback",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]
