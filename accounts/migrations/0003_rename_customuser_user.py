# Generated by Django 4.2.5 on 2023-09-22 18:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0002_rename_user_customuser"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CustomUser",
            new_name="User",
        ),
    ]
