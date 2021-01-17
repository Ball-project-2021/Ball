# -*- coding: utf-8 -*-
# !/usr/bin/env python
from django.db import models


class RegionModel(models.Model):
    region_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.region_name}'

    class Meta:
        verbose_name = "Տարածաշրջան"
        verbose_name_plural = "Տարածաշրջան"


class CountryModel(models.Model):
    country_name = models.CharField(max_length=32, verbose_name='Երկիր')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Երկիր"
        verbose_name_plural = "Երկիր"


class RegionChildModel(models.Model):
    region_child = models.CharField(max_length=55, verbose_name='Տարածաշրջան')
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, verbose_name='Տարածաշրջան')

    def __str__(self):
        return f'{self.region_child}'

    class Meta:
        verbose_name = "Տարածաշրջան-Raion"
        verbose_name_plural = "Տարածաշրջան-Raion"


class ManufacturerCountry(models.Model):
    man_country = models.CharField(max_length=30, verbose_name='Արտադրման երկիր')


def __str__(self):
    return self.man_country


class Meta:
    verbose_name = "Արտադրման երկիր"
    verbose_name_plural = "Արտադրման երկիր"


class CarBrand(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='Մակնիշ')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Մակնիշ"
        verbose_name_plural = "Մակնիշ"


class CarModel(models.Model):
    model_name = models.CharField(max_length=30, verbose_name='Մոդել')
    category = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "Մոդել"
        verbose_name_plural = "Մոդել"


class ProductYear(models.Model):
    product_year = models.CharField(max_length=32, verbose_name='Տարի')

    def __str__(self):
        return self.product_year

    class Meta:
        verbose_name = "Տարի"
        verbose_name_plural = "Տարի"


class Transmission(models.Model):
    transmission = models.CharField(max_length=32, verbose_name='Փոխանցման տուփ')

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = "Փոխանցման տուփ"
        verbose_name_plural = "Փոխանցման տուփ"


class Clearance(models.Model):
    clearance = models.CharField(max_length=32, verbose_name='Մաքսազերծված է')

    def __str__(self):
        return self.clearance

    class Meta:
        verbose_name = "Մաքսազերծված է"
        verbose_name_plural = "Մաքսազերծված է"


class Steering(models.Model):
    steering = models.CharField(max_length=32, verbose_name='Ղեկ')

    def __str__(self):
        return self.steering

    class Meta:
        verbose_name = "Ղեկ"
        verbose_name_plural = "Ղեկ"


class Color(models.Model):
    color = models.CharField(max_length=32, verbose_name='Գույն')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Գույն"
        verbose_name_plural = "Գույն"


class DriveUnit(models.Model):
    drive_unit = models.CharField(max_length=32, verbose_name='Քարշակ')

    def __str__(self):
        return self.drive_unit

    class Meta:
        verbose_name = "Քարշակ"
        verbose_name_plural = "Քարշակ"


class TransportFieldsModel(models.Model):
    class ChoiceMileageType(models.TextChoices):
        KM = 'km'
        ML = 'ml'

    class ChoiceDescLanguage(models.TextChoices):
        AM = 'ARM'
        RU = 'RUS'
        EN = 'EN'

    class ChoiceContact(models.TextChoices):
        WHATSAPP = 'whatsapp'
        VIBER = 'viber'
        TELEGRAM = 'telegram'
        ZANGI = 'zangi'

    class PriceType(models.TextChoices):
        AMD = "AMD"
        RU = "RUB"
        USD = "USD"
        EUR = "EUR"

    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    region_name = models.ForeignKey(RegionModel, on_delete=models.CASCADE)
    region_child = models.ForeignKey(RegionChildModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    product_year = models.OneToOneField(ProductYear, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    clearance = models.ForeignKey(Clearance, on_delete=models.CASCADE)
    steering = models.ForeignKey(Steering, on_delete=models.CASCADE)
    new = models.BooleanField(default=False, verbose_name='Նոր')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    millage_int = models.IntegerField(verbose_name='Վազք', null=True, default=None)
    mileage = models.CharField(max_length=50, choices=ChoiceMileageType.choices, default=ChoiceMileageType.KM,
                               verbose_name='Վազք-type')
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Գին')

    photo_1 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)

    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Գին')
    price_type = models.CharField(max_length=50, choices=PriceType.choices,
                                  default=PriceType.AMD)
    desc_language = models.CharField(max_length=50, choices=ChoiceDescLanguage.choices,
                                     default=ChoiceDescLanguage.AM)
    description = models.TextField(verbose_name='Նկարագրել', blank=True, null=True)
    hashtag = models.CharField(max_length=255, verbose_name='Գաղտնի որոնում', blank=True, null=True)
    contact = models.CharField(max_length=33, verbose_name='Կոնտակտ')
    contact_type = models.CharField(max_length=32, choices=ChoiceContact.choices,
                                    verbose_name='Կոնտակտ_type')
    dealer = models.BooleanField(default=False, verbose_name='Դիլլեր')
    created_at = models.DateTimeField(auto_now=True, verbose_name="don't touch")

    def __str__(self):
        return str('Ավտոմեքենաներ')

    class Meta:
        verbose_name = "ԿԳՆԵՄ"
        verbose_name_plural = "ԿԳՆԵՄ"
