# Generated by Django 2.2 on 2019-05-20 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("user", "0009_auto_20190520_1848")]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="tags",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="user.Tags",
                verbose_name="标签",
            ),
        )
    ]
