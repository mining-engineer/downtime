from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Park(models.Model):
    '''Таблица со списком парков'''
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Парк'
        )

    class Meta:
        verbose_name = 'парк'
        verbose_name_plural = 'Парки'

    def __str__(self):
        return self.title


class Sample(models.Model):
    '''Таблица списком моделей ТС в привязке к паркам'''
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Модель'
    )
    park = models.ForeignKey(
            Park,
            on_delete=models.SET,
            related_name='park',
    )

    class Meta:
        verbose_name = 'модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.title


class Equip(models.Model):
    '''Таблица списком ТС в привязке к моделям'''
    state_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Гос.номер'
    )
    eo = models.IntegerField(
        unique=True,
        verbose_name='ЕО'
    )
    model = models.ForeignKey(
        Sample,
        on_delete=models.SET,
        related_name="model"
    )

    class Meta:
        verbose_name = 'транспортное средство'
        verbose_name_plural = 'Транспортные средства'

    def __str__(self):
        return self.state_number


class Failure_сategory(models.Model):
    '''Таблица с причиной остановки'''
    failure_title = models.CharField(
        max_length=35,
        unique=True,
        verbose_name='Причина остановки'
    )

    class Meta:
        verbose_name = 'категория остановки'
        verbose_name_plural = 'Категории останвоки'

    def __str__(self):
        return self.failure_title


class Downtime(models.Model):
    '''Таблица простоев'''
    failure = models.ForeignKey(
        Failure_сategory,
        on_delete=models.SET,
        related_name="failure",
        verbose_name='Причина остановки',
        help_text='Укажите одну из основных причин остановки ТС'
    )
    state_number = models.ForeignKey(
        Equip,
        on_delete=models.SET,
        related_name="st_num",
        verbose_name='Гос.номер',
        help_text='Введите гос. номер ТС'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание случая'
    )
    time_startstamp = models.DateTimeField(
        verbose_name='Время начала',
        help_text='Выберите время остановки'
    )
    time_endstamp = models.DateTimeField(
        verbose_name='Время окончания',
        help_text='Выберите фактическое время завершения ремонта',
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Автор публикации'
    )

    class Meta:
        verbose_name = 'простой'
        verbose_name_plural = 'Простои'

    def __str__(self):
        return str(self.id)
    