# Generated by Django 5.1 on 2024-08-29 14:53

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_pub_date_comment_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[blog.validators.validate_content], verbose_name='포스트 내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postTitle',
            field=models.CharField(max_length=50, validators=[blog.validators.validate_title], verbose_name='포스트 제목'),
        ),
    ]
