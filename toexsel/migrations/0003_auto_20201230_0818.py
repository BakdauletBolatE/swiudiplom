# Generated by Django 3.1.4 on 2020-12-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toexsel', '0002_auto_20201230_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graguate',
            name='berilgen_kun',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='бітірген уақыты'),
        ),
        migrations.AlterField(
            model_name='graguate',
            name='btrgen_uakyt',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='бітірген уақыты'),
        ),
        migrations.AlterField(
            model_name='graguate',
            name='diplom_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дипломның нөмірі, сериясы'),
        ),
        migrations.AlterField(
            model_name='graguate',
            name='fio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тегі-аты әкесінің аты'),
        ),
        migrations.AlterField(
            model_name='graguate',
            name='mamangik',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='мамандық'),
        ),
        migrations.AlterField(
            model_name='graguate',
            name='tirkeu_katar',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Тіркеу қатар саны'),
        ),
    ]
