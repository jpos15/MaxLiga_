# Generated by Django 2.1.12 on 2019-10-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_maxliga', '0003_auto_20191028_1009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LancamentoPontuacao',
            new_name='LancamentoAvaliacao',
        ),
    ]
