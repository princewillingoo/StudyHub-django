# Generated by Django 4.2 on 2023-05-05 00:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_topic_room_host_messaage_room_topic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messaage',
            new_name='Message',
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]