from django.db import models

# Create your models here.

class Graguate2004(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    btrgen_uakyt = models.CharField('бітірген уақыты',max_length=50,blank=True,null=True)
    berilgen_kun = models.CharField('бітірген уақыты',max_length=50,blank=True,null=True)
    mamangik = models.CharField('мамандық',max_length=10,blank=True,null=True)
    pos = models.CharField('безимянный',max_length=30,blank=True,null=True)

class Graduate2005(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    berilu_merzim = models.CharField('берілу мерзімі',max_length=100, blank=True,null=True)
    mkk = models.CharField('МКК протоколының нөмірі, мерзімі',max_length=100,blank=True,null=True)
    mamangik = models.CharField('мамандық',max_length=10,blank=True,null=True)
    berilgen_kva = models.CharField('берілген квалификациясы',max_length=255,blank=True,null=True)
    pos = models.CharField('безимянный',max_length=30,blank=True,null=True)

class Graduate2006(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    duplicate = models.CharField('Дупликат',max_length=20,blank=True,null=True)
    year = models.CharField('Жылдар',max_length=20,blank=True,null=True)

class Graduate2007(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    akt = models.CharField('Акт',max_length=30,blank=True,null=True)
    uzd = models.CharField('Узд',max_length=20,blank=True,null=True)
    duplicate = models.CharField('Дупликат',max_length=20,blank=True,null=True)
    year = models.CharField('Жылдар',max_length=20,blank=True,null=True)
    ajb = models.CharField('АЖБ',max_length=30,blank=True,null=True)

class Graduate2008(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    eskertu = models.CharField('Ескерту',max_length=100,blank=True,null=True)
    address = models.CharField('мекен-жайы',max_length=255,blank=True,null=True)
    workplace = models.CharField('жұмыс орны',max_length=255,blank=True,null=True)
    fio2 = models.CharField('fio2',max_length=100,blank=True,null=True)
    naima = models.CharField('naima',max_length=100,blank=True,null=True)

class Graduate2009(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    eskertu = models.CharField('Ескерту',max_length=100,blank=True,null=True)
    address = models.CharField('Мекен-жайы',max_length=255,blank=True,null=True)
    workplace = models.CharField('Жұмыс орны',max_length=255,blank=True,null=True)
    fio2 = models.CharField('Fio2',max_length=255,blank=True,null=True)

class Graduate2010(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    eskertu = models.CharField('Ескерту',max_length=100,blank=True,null=True)
    reddiplom = models.CharField('Красный Дипломдар',max_length=255,blank=True,null=True)


    




