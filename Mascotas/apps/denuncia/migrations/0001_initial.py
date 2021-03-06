# Generated by Django 3.1 on 2021-03-15 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('denunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denunciado', to=settings.AUTH_USER_MODEL)),
                ('denunciante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denunciante', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'denuncias',
            },
        ),
    ]
