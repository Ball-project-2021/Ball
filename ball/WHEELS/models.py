from django.db import models
from transports.models import ProductYear, Clearance, CarModel, CarBrand


class Color(models.Model):
    color = models.CharField(max_length=40, verbose_name="Գույն")

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = "Գույն"
        verbose_name_plural = "Գույներ"


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


class Caliber(models.Model):
    caliber_type = models.CharField(max_length=33, verbose_name='Տրամաչափ')


    def __str__(self):
        return f'{self.caliber_type}'

    class Meta:
        verbose_name = 'Անվահեծի տրամաչափ'
        verbose_name_plural = 'Անվահեծերի տրամաչափ'

class HolesQty(models.Model):
    qty = models.PositiveIntegerField(verbose_name="Անցքերի քանակը")

    def __str__(self):
        return f'{self.qty}'

    class Meta:
        verbose_name = 'Անցքերի քանակը'
        verbose_name_plural = 'Անցքերի քանակը'


class ContactCode(models.Model):
    code = models.CharField(max_length=12)
    cod_country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}{self.cod_country}'

    class Meta:
        verbose_name = 'Երկրի կոդ'
        verbose_name_plural = "Երկրների կոդեր"


class Wheel(models.Model):
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
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    caliber = models.ForeignKey(Caliber, on_delete=models.CASCADE)
    The_size_of_the_wheel_holes = models.PositiveIntegerField(verbose_name="Անվահեծի անցքերի չափ")
    holes_qty = models.ForeignKey(HolesQty, on_delete=models.CASCADE)
    new = models.BooleanField(default=False, verbose_name='Նոր')
    used = models.BooleanField(default=False, verbose_name='Օգտագործված')
    product_year = models.OneToOneField(ProductYear, on_delete=models.CASCADE)
    clearance = models.ForeignKey(Clearance, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(verbose_name="Քանակ")
    photo_1 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Գին')
    price_per_unit = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Գինը հատի դեպքում')
    price_type = models.CharField(max_length=50, choices=PriceType.choices,
                                  default=PriceType.AMD)
    desc_language = models.CharField(max_length=50, choices=ChoiceDescLanguage.choices,
                                     default=ChoiceDescLanguage.AM)
    description = models.TextField(verbose_name='Նկարագրել', blank=True, null=True)
    hashtag = models.CharField(max_length=255, verbose_name='Գաղտնի որոնում', blank=True, null=True)
    contact_code = models.ForeignKey(ContactCode, on_delete=models.CASCADE, default=None)
    contact = models.CharField(max_length=33, verbose_name='Կոնտակտ')
    contact_type = models.CharField(max_length=32, choices=ChoiceContact.choices,
                                    verbose_name='Կոնտակտ_type')
    dealer = models.BooleanField(default=False, verbose_name='Դիլլեր')
    created_at = models.DateTimeField(auto_now=True, verbose_name="don't touch")
    exchange = models.BooleanField(default=False, verbose_name='Փոխանակում')

    def __str__(self):
        return f'{self.brand}{self.price}'

    class Meta:
        verbose_name = "Անվահեծ"
        verbose_name_plural = "Անվահեծեր"
