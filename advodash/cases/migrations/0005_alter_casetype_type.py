# Generated by Django 4.2.5 on 2023-09-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cases", "0004_alter_casestage_stage_alter_casetype_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casetype",
            name="type",
            field=models.CharField(max_length=100),
        ),
    ]