# Generated by Django 4.2.1 on 2023-05-29 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0004_alter_shift_id_alter_shift_punch_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='corrected_break_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='corrected_break_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='corrected_punch_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='corrected_punch_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CorrectedShift',
        ),
    ]
