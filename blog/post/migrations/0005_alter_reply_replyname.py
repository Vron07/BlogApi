# Generated by Django 4.1 on 2022-09-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_post_comment_commentname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='replyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='post.comment'),
        ),
    ]
