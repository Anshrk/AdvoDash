# Generated by Django 4.2.5 on 2023-09-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cases", "0002_casestage_stage_casetype_type_court_court"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cases",
            name="appearing_lawyer",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="cases",
            name="title",
            field=models.CharField(max_length=250),
        ),
    ]
