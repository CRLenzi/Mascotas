# Generated by Django 3.1 on 2021-03-15 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación', verbose_name='creado')),
                ('mensaje', models.CharField(blank=True, max_length=250, null=True)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL)),
                ('id_mascotas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopcion.mascotasadopcion')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Mensajes',
            },
        ),
    ]
