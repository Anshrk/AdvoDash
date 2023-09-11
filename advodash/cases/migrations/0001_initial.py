# Generated by Django 4.2.5 on 2023-09-11 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CaseStage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="CaseType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Court",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Case",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("number", models.BigIntegerField()),
                ("tags", models.CharField(blank=True, max_length=100)),
                ("filling_date", models.DateField()),
                ("appearing_lawyer", models.CharField(max_length=255)),
                ("remarks", models.TextField()),
                ("party_name", models.CharField(max_length=30)),
                ("party_contact_no", models.CharField(max_length=15)),
                (
                    "party_email",
                    models.CharField(blank=True, default="", max_length=40),
                ),
                (
                    "party_alternative_contact_no",
                    models.CharField(blank=True, default="", max_length=14),
                ),
                ("party_adress", models.TextField(blank=True, default="")),
                ("prev_date", models.DateField()),
                ("next_date", models.DateField(null=True)),
                ("case_history", models.TextField()),
                (
                    "court",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cases.court"
                    ),
                ),
                (
                    "stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cases.casestage",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cases.casetype"
                    ),
                ),
            ],
        ),
    ]
