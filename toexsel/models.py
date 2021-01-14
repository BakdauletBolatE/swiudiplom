from django.db import models

# Create your models here.

class Graguate1996(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)
    pos = models.CharField('безимянный',max_length=30,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 1996 года"
        verbose_name_plural = "Выпуснкики 1996 года"

class Graguate1997(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 1997 года"
        verbose_name_plural = "Выпуснкики 1997 года"

class Graguate1998(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 1998 года"
        verbose_name_plural = "Выпуснкики 1998 года"

class Graguate1999(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mak = models.CharField('МАК',max_length=30,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 1999 года"
        verbose_name_plural = "Выпуснкики 1999 года"

class Graguate2000(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    hattama = models.CharField('Хаттама',max_length=255,blank=True,null=True)
    berilgen_kun = models.CharField('Берілген күн',max_length=100,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2000 года"
        verbose_name_plural = "Выпуснкики 2000 года"

class Graguate2001(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    berilgen_kun = models.CharField('Берілген күн',max_length=100,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2001 года"
        verbose_name_plural = "Выпуснкики 2001 года"


class Graguate2002(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    hattama = models.CharField('Хаттама',max_length=255,blank=True,null=True)
    berilgen_kun = models.CharField('Берілген күн',max_length=100,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2002 года"
        verbose_name_plural = "Выпуснкики 2002 года"

class Graguate2003(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    btrgen_kun = models.CharField('Берілген күн',max_length=100,blank=True,null=True)
    berilgen_kun = models.CharField('Берілген күн',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    usp = models.CharField('Успеваемость',max_length=12,blank=True,null=True)
    srok = models.CharField('Хаттама',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2003 года"
        verbose_name_plural = "Выпуснкики 2003 года"

class Graguate2004(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    btrgen_uakyt = models.CharField('бітірген уақыты',max_length=50,blank=True,null=True)
    berilgen_kun = models.CharField('бітірген уақыты',max_length=50,blank=True,null=True)
    mamangik = models.CharField('мамандық',max_length=10,blank=True,null=True)
    pos = models.CharField('безимянный',max_length=30,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2004 года"
        verbose_name_plural = "Выпуснкики 2004 года"

    
class Graduate2005(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    berilu_merzim = models.CharField('берілу мерзімі',max_length=100, blank=True,null=True)
    mkk = models.CharField('МКК протоколының нөмірі, мерзімі',max_length=100,blank=True,null=True)
    mamangik = models.CharField('мамандық',max_length=100,blank=True,null=True)
    berilgen_kva = models.CharField('берілген квалификациясы',max_length=255,blank=True,null=True)
    pos = models.CharField('безимянный',max_length=30,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2005 года"
        verbose_name_plural = "Выпуснкики 2005 года"

class Graduate2006(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    duplicate = models.CharField('Дупликат',max_length=20,blank=True,null=True)
    year = models.CharField('Жылдар',max_length=20,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2006 года"
        verbose_name_plural = "Выпуснкики 2006 года"

class Graduate2007(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=255,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=255,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    akt = models.CharField('Акт',max_length=255,blank=True,null=True)
    uzd = models.CharField('Узд',max_length=255,blank=True,null=True)
    duplicate = models.CharField('Дупликат',max_length=255,blank=True,null=True)
    year = models.CharField('Жылдар',max_length=255,blank=True,null=True)
    ajb = models.CharField('АЖБ',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2007 года"
        verbose_name_plural = "Выпуснкики 2007 года"

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

    class Meta:
        verbose_name = "Выпуснкик 2008 года"
        verbose_name_plural = "Выпуснкики 2008 года"

class Graduate2009(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    eskertu = models.CharField('Ескерту',max_length=100,blank=True,null=True)
    address = models.CharField('Мекен-жайы',max_length=255,blank=True,null=True)
    workplace = models.CharField('Жұмыс орны',max_length=255,blank=True,null=True)
    fio2 = models.CharField('Fio2',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2009 года"
        verbose_name_plural = "Выпуснкики 2009 года"

class Graduate2010(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    eskertu = models.CharField('Ескерту',max_length=100,blank=True,null=True)
    reddiplom = models.CharField('Красный Дипломдар',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2010 года"
        verbose_name_plural = "Выпуснкики 2010 года"
    
class Graduate2011(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2011 года"
        verbose_name_plural = "Выпуснкики 2011 года"

class Graduate2012(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    group = models.CharField('Тобы',max_length=255,blank=True,null=True)
    birthday = models.CharField('туган күні',max_length=20,blank=True,null=True)
    birthyear1 = models.CharField('Туылган жылы1',max_length=255,blank=True,null=True)
    birthyear2 = models.CharField('Туылган жылы2',max_length=255,blank=True,null=True)
    jekekualik = models.CharField('жеке куәлік №',max_length=255,blank=True,null=True)
    jsn = models.CharField('ЖСН (ИИН)',max_length=255,blank=True,null=True)
    ctn = models.CharField('СТН (РНН)',max_length=255,blank=True,null=True)
    nation = models.CharField('улты',max_length=255,blank=True,null=True)
    azamattik = models.CharField('азаматтығы',max_length=255,blank=True,null=True)
    address = models.CharField('Мекен-жайы',max_length=255,blank=True,null=True)
    workplace = models.CharField('Жұмыс орны',max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2012 года"
        verbose_name_plural = "Выпуснкики 2012 года"


class Graduate2013(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
    birthday = models.CharField('туган күні',max_length=150,blank=True,null=True)
    pol = models.CharField('Пол',max_length=150,blank=True,null=True)
    nation = models.CharField('улты',max_length=150,blank=True,null=True)
    dateto = models.CharField('Дата выдачи',max_length=150,blank=True,null=True)
    numberpasport = models.CharField('жеке куәлік №',max_length=150,blank=True,null=True)
    whotake = models.CharField('Кем выдан',max_length=150,blank=True,null=True)
    datefor = models.CharField('Дата выдачи',max_length=150,blank=True,null=True)
    

    class Meta:
        verbose_name = "Выпуснкик 2013 года"
        verbose_name_plural = "Выпуснкики 2013 года"

class Graduate2014(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
  

    class Meta:
        verbose_name = "Выпуснкик 2014 года"
        verbose_name_plural = "Выпуснкики 2014 года"

class Graduate2015(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
  

    class Meta:
        verbose_name = "Выпуснкик 2015 года"
        verbose_name_plural = "Выпуснкики 2015 года"

class Graduate2016(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
  

    class Meta:
        verbose_name = "Выпуснкик 2016 года"
        verbose_name_plural = "Выпуснкики 2016 года"

class Graduate2017(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
  

    class Meta:
        verbose_name = "Выпуснкик 2017 года"
        verbose_name_plural = "Выпуснкики 2017 года"

class Graduate2018(models.Model):
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    tirkeu_katar = models.CharField('Тіркеу қатар саны',max_length=100,blank=True,null=True)
    mak = models.CharField('МАК',max_length=150,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    formedu = models.CharField('Форма обучения (очн., заочн.)',max_length=100,blank=True,null=True)
    fio = models.CharField('Тегі-аты әкесінің аты',max_length=255,blank=True,null=True)
  

    class Meta:
        verbose_name = "Выпуснкик 2018 года"
        verbose_name_plural = "Выпуснкики 2018 года"

class Graduate2019och(models.Model):
    surname = models.CharField('Фамилия',max_length=140,blank=True,null=True)
    name = models.CharField('Имя',max_length=140,blank=True,null=True)
    last_name = models.CharField('Отчество',max_length=140,blank=True,null=True)
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    untitled = models.CharField('Регистрационный номер',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2019 года очное"
        verbose_name_plural = "Выпуснкики 2019 года очное"

class Graduate2019zaoch(models.Model):
    surname = models.CharField('Фамилия',max_length=140,blank=True,null=True)
    name = models.CharField('Имя',max_length=140,blank=True,null=True)
    last_name = models.CharField('Отчество',max_length=140,blank=True,null=True)
    diplom_number = models.CharField('Дипломның нөмірі, сериясы',max_length=100,blank=True,null=True)
    untitled = models.CharField('Регистрационный номер',max_length=100,blank=True,null=True)
    mamangikship = models.CharField('Мамандық шифрі',max_length=255,blank=True,null=True)
    diplombk = models.CharField('Диплом беру туралы бұйрық № ',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = "Выпуснкик 2019 года заочное"
        verbose_name_plural = "Выпуснкики 2019 года заочное"


    




