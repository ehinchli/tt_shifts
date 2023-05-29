# Generated by Django 4.2.1 on 2023-05-29 01:33

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
            name='TimePunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField(blank=True, null=True)),
                ('break_start', models.DateTimeField(blank=True, null=True)),
                ('break_end', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimePunchCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_time_in', models.DateTimeField()),
                ('old_time_out', models.DateTimeField(blank=True, null=True)),
                ('old_break_start', models.DateTimeField(blank=True, null=True)),
                ('old_break_end', models.DateTimeField(blank=True, null=True)),
                ('correction_note', models.TextField()),
                ('corrected_at', models.DateTimeField(auto_now_add=True)),
                ('time_punch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clock.timepunch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]