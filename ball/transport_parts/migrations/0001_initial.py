# Generated by Django 3.1.5 on 2021-01-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_body', models.CharField(max_length=32, verbose_name='Թափքի տեսակ')),
            ],
            options={
                'verbose_name': 'Թափքի տեսակ',
                'verbose_name_plural': 'Թափքի տեսակ',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50, verbose_name='Մակնիշ')),
            ],
            options={
                'verbose_name': 'Մակնիշ',
                'verbose_name_plural': 'Մակնիշ',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30, verbose_name='Մոդել')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.carbrand')),
            ],
            options={
                'verbose_name': 'Մոդել',
                'verbose_name_plural': 'Մոդել',
            },
        ),
        migrations.CreateModel(
            name='Clearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clearance', models.CharField(max_length=32, verbose_name='Մաքսազերծված է')),
            ],
            options={
                'verbose_name': 'Մաքսազերծված է',
                'verbose_name_plural': 'Մաքսազերծված է',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=32, verbose_name='Գույն')),
            ],
            options={
                'verbose_name': 'Գույն',
                'verbose_name_plural': 'Գույն',
            },
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=32, verbose_name='Երկիր')),
            ],
            options={
                'verbose_name': 'Երկիր',
                'verbose_name_plural': 'Երկիր',
            },
        ),
        migrations.CreateModel(
            name='DriveUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_unit', models.CharField(max_length=32, verbose_name='Քարշակ')),
            ],
            options={
                'verbose_name': 'Քարշակ',
                'verbose_name_plural': 'Քարշակ',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=32, verbose_name='Վառելիք')),
            ],
            options={
                'verbose_name': 'Վառելիք',
                'verbose_name_plural': 'Վառելիք',
            },
        ),
        migrations.CreateModel(
            name='ManufacturerCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_country', models.CharField(max_length=30, verbose_name='Արտադրման երկիր')),
            ],
            options={
                'verbose_name': 'Արտադրման երկիր',
                'verbose_name_plural': 'Արտադրման երկիր',
            },
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor', models.CharField(max_length=32, verbose_name='Շարժիչի ծավա')),
            ],
            options={
                'verbose_name': 'Շարժիչի ծավալ',
                'verbose_name_plural': 'Շարժիչի ծավալ',
            },
        ),
        migrations.CreateModel(
            name='ProductYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_year', models.CharField(max_length=32, verbose_name='Տարի')),
            ],
            options={
                'verbose_name': 'Տարի',
                'verbose_name_plural': 'Տարի',
            },
        ),
        migrations.CreateModel(
            name='RegionChildModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_child', models.CharField(max_length=55, verbose_name='Տարածաշրջան')),
            ],
            options={
                'verbose_name': 'Տարածաշրջան-Raion',
                'verbose_name_plural': 'Տարածաշրջան-Raion',
            },
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Տարածաշրջան',
                'verbose_name_plural': 'Տարածաշրջան',
            },
        ),
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steering', models.CharField(max_length=32, verbose_name='Ղեկ')),
            ],
            options={
                'verbose_name': 'Ղեկ',
                'verbose_name_plural': 'Ղեկ',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=32, verbose_name='Փոխանցման տուփ')),
            ],
            options={
                'verbose_name': 'Փոխանցման տուփ',
                'verbose_name_plural': 'Փոխանցման տուփ',
            },
        ),
        migrations.CreateModel(
            name='TransportFieldsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_code', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Vin Code')),
                ('show_vin_code', models.BooleanField(default=True)),
                ('new', models.BooleanField(default=False, verbose_name='Նոր')),
                ('used', models.BooleanField(default=False, verbose_name='Օգտագործված')),
                ('horse_power', models.IntegerField(verbose_name='Ձիաուժ')),
                ('millage_int', models.IntegerField(verbose_name='Վազք')),
                ('photo_main', models.ImageField(upload_to='photos/transport/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/transport/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/transport/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/transport/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/transport/%Y/%m/%d/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Գին')),
                ('price_type', models.CharField(choices=[('AMD', 'Amd'), ('RUB', 'Ru'), ('USD', 'Usd'), ('EUR', 'Eur')], default='AMD', max_length=50)),
                ('mileage', models.CharField(choices=[('ARM', 'Am'), ('RUS', 'Ru'), ('EN', 'En')], default='ARM', max_length=50)),
                ('description', models.TextField(verbose_name='Նկարագրել')),
                ('hashtag', models.CharField(blank=True, max_length=255, verbose_name='Գաղտնի որոնում')),
                ('contact', models.CharField(max_length=33, verbose_name='Կոնտակտ')),
                ('contact_type', models.CharField(choices=[('whatsapp', 'Whatsapp'), ('viber', 'Viber'), ('telegram', 'Telegram'), ('zangi', 'Zangi')], max_length=32, verbose_name='Կոնտակտ_type')),
                ('change_or_buy', models.CharField(choices=[('Կգնեմ', 'Buy'), ('Փոխանակում', 'Exchange')], default='Կգնեմ', max_length=50)),
                ('exchange', models.BooleanField(default=False, verbose_name='Փոխանակում')),
                ('dealer', models.BooleanField(default=False, verbose_name='Դիլլեր')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name="don't touch")),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.carbrand')),
                ('car_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.carbody')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.carmodel')),
                ('clearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.clearance')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.color')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.countrymodel')),
                ('drive_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.driveunit')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.fuel')),
                ('man_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.manufacturercountry')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.motor')),
                ('product_year', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.productyear')),
                ('region_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.regionchildmodel')),
                ('region_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.regionmodel')),
                ('steering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.steering')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.transmission')),
            ],
            options={
                'verbose_name': 'ՎԹԱՐՎԱԾ ՈՐՊԵՍ ՊԱՀԵՍՏԱՄԱՍ',
                'verbose_name_plural': 'ՎԹԱՐՎԱԾ ՈՐՊԵՍ ՊԱՀԵՍՏԱՄԱՍ',
            },
        ),
        migrations.AddField(
            model_name='regionchildmodel',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_parts.regionmodel', verbose_name='Տարածաշրջան'),
        ),
    ]
