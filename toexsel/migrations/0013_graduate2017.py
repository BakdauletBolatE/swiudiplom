# Generated by Django 3.1.4 on 2021-01-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toexsel', '0012_auto_20210114_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graduate2017',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diplom_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Дипломның нөмірі, сериясы')),
                ('tirkeu_katar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тіркеу қатар саны')),
                ('mak', models.CharField(blank=True, max_length=150, null=True, verbose_name='МАК')),
                ('diplombk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Диплом беру туралы бұйрық № ')),
                ('mamangikship', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мамандық шифрі')),
                ('formedu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Форма обучения (очн., заочн.)')),
                ('fio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тегі-аты әкесінің аты')),
            ],
            options={
                'verbose_name': 'Выпуснкик 2017 года',
                'verbose_name_plural': 'Выпуснкики 2017 года',
            },
        ),
    ]
