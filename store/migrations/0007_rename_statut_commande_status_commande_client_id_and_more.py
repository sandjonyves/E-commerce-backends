# Generated by Django 5.0.4 on 2024-05-17 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('store', '0006_pieceimage_image_url_alter_pieceimage_piece_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='Statut',
            new_name='status',
        ),
        migrations.AddField(
            model_name='commande',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client_id', to='account.client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='piece',
            name='city',
            field=models.CharField(blank=True, default='yaounde', max_length=255),
        ),
    ]