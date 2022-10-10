# Generated by Django 4.1.2 on 2022-10-10 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0009_alter_item_buys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='purch',
        ),
        migrations.RemoveField(
            model_name='purchased',
            name='user',
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchased',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='main_app.budget'),
        ),
    ]
