# Generated by Django 4.1 on 2022-09-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='post.comment'),
        ),
    ]