# Generated by Django 3.0.6 on 2021-04-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("introduction", "0006_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="comment",
            field=models.CharField(max_length=600),
        ),
    ]
