from django.db import models

# Create your models here.

class SwiuDiplom2019(models.Model):

    nameUniversity = models.CharField('наименование вузаs (полностью)',max_length=255,null=True,blank=True)
    firstName = models.CharField('Фамилия',max_length=255,null=True,blank=True)
    name = models.CharField('Имя (полностью)',max_length=255,null=True,blank=True)
    lastName = models.CharField('Отчество (полностью)',max_length=255,null=True,blank=True)
    iin = models.CharField('ИИН',max_length=255,null=True,blank=True)
    pnn = models.CharField('РНН (в случае отсутствия ИИН)',max_length=255,null=True,blank=True)
    dateOfBirthDay = models.CharField('дата рождения  (обязательно)',max_length=255,null=True,blank=True)
    passNumber = models.CharField('номер уд. личности ',max_length=255,null=True,blank=True)
    companyName = models.CharField('Орган, выдавший документ, удостоверяющий личность',max_length=255,null=True,blank=True)
    dateEnter = models.CharField('Дата поступления (обязательно)',max_length=255,null=True,blank=True)
    numberOrder = models.CharField('Номер приказа о зачислении (обязательно)',max_length=255,null=True,blank=True)
    formEducation = models.CharField('Форма обучения (очное, заочное, вечернее) (обязательно)',max_length=255,null=True,blank=True)
    codeIn = models.CharField('код (обязательно)',max_length=255,null=True,blank=True)
    nameSpecialization = models.CharField('наименование специальности (обязательно)',max_length=255,null=True,blank=True)
    degreeAcademic = models.CharField('Академическая степень (бакалавр, магистр, доктор, резидент, интерн (обязательно)',max_length=255,null=True,blank=True)
    dateOut = models.CharField('Год выпуска (обязательно)',max_length=255,null=True,blank=True)
    numberOrderEnd = models.CharField('Номер приказа об окончании (обязательно)',max_length=255,null=True,blank=True)
    dateProtocol = models.CharField('Дата протокола (обязательно)',max_length=255,null=True,blank=True)
    numberProtocol = models.CharField('Номер протокола (обязательно)',max_length=255,null=True,blank=True)
    dateDiplomEnd = models.CharField('Дата выдачи диплома (обязательно)',max_length=255,null=True,blank=True)
    numberDiplomSeria = models.CharField('Серия и номер диплома (обязательно)',max_length=255,null=True,blank=True)
    registrationDimplom = models.CharField('Регистрационный № диплома (обязательно)',max_length=255,null=True,blank=True)
    numberDiplomSeria2 = models.CharField('Серия и номер диплома (обязательно)',max_length=255,null=True,blank=True)
    dateEndDublicat = models.CharField('Дата выдачи дубликата (обязательно)',max_length=255,null=True,blank=True)

    class Meta:

        verbose_name = 'Выпускник 2019(Новая версия)'
        verbose_name_plural = 'Выпускники 2019(Новая версия)'

class SwiuDiplomBefore2018(models.Model):

    nameUniversity = models.CharField('наименование вуза (полностью)',max_length=255,null=True,blank=True)
    fio = models.CharField('ФИО (полностью)',max_length=255,null=True,blank=True)
    iin = models.CharField('ИИН',max_length=255,null=True,blank=True)
    pnn = models.CharField('РНН (в случае отсутствия ИИН)',max_length=255,null=True,blank=True)
    dateOfBirthDay = models.CharField('дата рождения  (обязательно)',max_length=255,null=True,blank=True)
    passNumber = models.CharField('номер уд. личности ',max_length=255,null=True,blank=True)
    companyName = models.CharField('Орган, выдавший документ, удостоверяющий личность',max_length=255,null=True,blank=True)
    dateEnter = models.CharField('Дата поступления (обязательно)',max_length=255,null=True,blank=True)
    numberOrder = models.CharField('Номер приказа о зачислении (обязательно)',max_length=255,null=True,blank=True)
    formEducation = models.CharField('Форма обучения (очное, заочное, вечернее) (обязательно)',max_length=255,null=True,blank=True)
    codeIn = models.CharField('код (обязательно)',max_length=255,null=True,blank=True)
    nameSpecialization = models.CharField('наименование специальности (обязательно)',max_length=255,null=True,blank=True)
    degreeAcademic = models.CharField('Академическая степень (бакалавр, магистр, доктор, резидент, интерн (обязательно)',max_length=255,null=True,blank=True)
    dateOut = models.CharField('Год выпуска (обязательно)',max_length=255,null=True,blank=True)
    numberOrderEnd = models.CharField('Номер приказа об окончании (обязательно)',max_length=255,null=True,blank=True)
    dateProtocol = models.CharField('Дата протокола (обязательно)',max_length=255,null=True,blank=True)
    numberProtocol = models.CharField('Номер протокола (обязательно)',max_length=255,null=True,blank=True)
    dateDiplomEnd = models.CharField('Дата выдачи диплома (обязательно)',max_length=255,null=True,blank=True)
    numberDiplomSeria = models.CharField('Серия и номер диплома (обязательно)',max_length=255,null=True,blank=True)
    registrationDimplom = models.CharField('Регистрационный № диплома (обязательно)',max_length=255,null=True,blank=True)
    numberDiplomSeria2 = models.CharField('Серия и номер диплома (обязательно)',max_length=255,null=True,blank=True)
    dateEndDublicat = models.CharField('Дата выдачи дубликата (обязательно)',max_length=255,null=True,blank=True)

    class Meta:

        verbose_name = 'Выпускник до 1996-2019(Новая версия)'
        verbose_name_plural = 'Выпускники до 1996-2019(Новая версия)'