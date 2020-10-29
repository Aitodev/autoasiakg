# Generated by Django 3.1.2 on 2020-10-28 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Automodel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('automodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.automodel')),
            ],
        ),
        migrations.CreateModel(
            name='Automodel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('automodel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.automodel1')),
            ],
        ),
        migrations.CreateModel(
            name='Bestproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('img', models.ImageField(upload_to='static/img/bestproduct/', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('price_disc', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена со скидкой')),
                ('new', models.BooleanField(verbose_name='Новый товар')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('product_code', models.CharField(blank=True, max_length=32, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/img/bestproduct/', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена')),
                ('price_disc', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена со скидкой')),
                ('new', models.BooleanField(default=False, verbose_name='Новый товар')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('automodel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.automodel')),
                ('automodel1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.automodel1')),
                ('automodel2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.automodel2')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.manufacturer')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subcategory')),
                ('subcategory1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subcategory1')),
            ],
        ),
        migrations.AddField(
            model_name='automodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand'),
        ),
    ]
