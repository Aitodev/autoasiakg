from main.models import Category, Subcategory, Subcategory1, Brand, Automodel, Automodel1, Automodel2, Manufacturer, Product
from uploader.forms import CsvUploadForm
from uploader.models import UploadModel
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path
from decimal import Decimal
import tempfile
import codecs
import xlrd
import csv


class CsvUploadAdmin(admin.ModelAdmin):
    change_list_template = "uploader.html"

    def get_urls(self):
        urls = super().get_urls()
        additional_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return additional_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra = extra_context or {}
        extra["csv_upload_form"] = CsvUploadForm()
        return super(CsvUploadAdmin, self).changelist_view(request, extra_context=extra)

    def upload_csv(self, request):
        if request.method == "POST":
            form = CsvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['csv_file']
                temp = tempfile.NamedTemporaryFile()
                temp.write(file.read())
                if (str(file).split('.')[-1] == 'xls') or (str(file).split('.')[-1] == 'xlsx'):
                    try:
                        with xlrd.open_workbook(temp.name) as wb:
                            sh = wb.sheet_by_index(0)
                            # keys = [key.value for key in sh.row(0)]
                            # 0 'Сategory', 1 'Subcategory1', 2 'Subcategory2',
                            # 3 'Productcode', 4 'Productname', 5 'Shortdescription',
                            # 6 'Aufobrand', 7 'Automodel1', 8 'Automodel2',
                            # 9 'Automodel3', 10 'manufacturer', 11'Aufobrand',
                            # 12 'Automodel1', 13 'Automodel2', 14 'Automodel3',
                            # 15 'manufacturer', 16 'Price'
                            for row in range(1, sh.nrows):
                                if sh.row(row)[0].value:
                                    subcategory = None
                                    subcategory1 = None
                                    brand = None
                                    automodel = None
                                    automodel1 = None
                                    automodel2 = None
                                    manufacturer = None
                                    if Category.objects.filter(name=sh.row(row)[0].value).exists():
                                        category = Category.objects.filter(name=sh.row(row)[0].value).first()
                                    else:
                                        category = Category.objects.create(name=sh.row(row)[0].value)
                                    if sh.row(row)[1].value:
                                        if Subcategory.objects.filter(name=sh.row(row)[1].value).exists():
                                            subcategory = Subcategory.objects.filter(name=sh.row(row)[1].value).first()
                                        else:
                                            subcategory = Subcategory.objects.create(name=sh.row(row)[1].value, category=category)
                                    if sh.row(row)[2].value:
                                        if Subcategory1.objects.filter(name=sh.row(row)[2].value).exists():
                                            subcategory1 = Subcategory1.objects.filter(name=sh.row(row)[2].value).first()
                                        else:
                                            subcategory1 = Subcategory1.objects.create(name=sh.row(row)[2].value, subcategory=subcategory)
                                    if sh.row(row)[6].value:
                                        if Brand.objects.filter(name=sh.row(row)[6].value).exists():
                                            brand = Brand.objects.filter(name=sh.row(row)[6].value).first()
                                        else:
                                            brand = Brand.objects.create(name=sh.row(row)[6].value)
                                    if sh.row(row)[7].value:
                                        if Automodel.objects.filter(name=sh.row(row)[7].value).exists():
                                            automodel = Automodel.objects.filter(name=sh.row(row)[7].value).first()
                                        else:
                                            automodel = Automodel.objects.create(name=sh.row(row)[7].value, brand=brand)
                                    if sh.row(row)[8].value:
                                        if Automodel1.objects.filter(name=sh.row(row)[8].value).exists():
                                            automodel1 = Automodel1.objects.filter(name=sh.row(row)[8].value).first()
                                        else:
                                            automodel1 = Automodel1.objects.create(name=sh.row(row)[8].value, automodel=automodel)
                                    if sh.row(row)[9].value:
                                        if Automodel2.objects.filter(name=sh.row(row)[9].value).exists():
                                            automodel2 = Automodel2.objects.filter(name=sh.row(row)[9].value).first()
                                        else:
                                            automodel2 = Automodel2.objects.create(name=sh.row(row)[9].value, automodel1=automodel1)
                                    if sh.row(row)[10].value:
                                        if Manufacturer.objects.filter(name=sh.row(row)[10].value).exists():
                                            manufacturer = Manufacturer.objects.filter(name=sh.row(row)[10].value).first()
                                        else:
                                            manufacturer = Manufacturer.objects.create(name=sh.row(row)[10].value)
                                    code = sh.row(row)[3].value
                                    name = sh.row(row)[4].value
                                    description = sh.row(row)[5].value
                                    price = sh.row(row)[16].value
                                    if name:
                                        Product.objects.create(name=name, description=description, product_code=code, category=category, price=price,
                                                               manufacturer=manufacturer, subcategory=subcategory, subcategory1=subcategory1,
                                                               brand=brand, automodel=automodel, automodel1=automodel1, automodel2=automodel2)
                                    # LOOKS LIKE THE EXCEL FILE IS WRONG !!!
                                    automodel = None
                                    automodel1 = None
                                    automodel2 = None
                                    manufacturer = None
                                    if sh.row(row)[11].value:
                                        if Brand.objects.filter(name=sh.row(row)[11].value).exists():
                                            brand = Brand.objects.filter(name=sh.row(row)[11].value).first()
                                        else:
                                            brand = Brand.objects.create(name=sh.row(row)[11].value)
                                    if sh.row(row)[12].value:
                                        if Automodel.objects.filter(name=sh.row(row)[12].value).exists():
                                            automodel = Automodel.objects.filter(name=sh.row(row)[12].value).first()
                                        else:
                                            automodel = Automodel.objects.create(name=sh.row(row)[12].value, brand=brand)
                                    if sh.row(row)[13].value:
                                        if Automodel1.objects.filter(name=sh.row(row)[13].value).exists():
                                            automodel1 = Automodel1.objects.filter(name=sh.row(row)[13].value).first()
                                        else:
                                            automodel1 = Automodel1.objects.create(name=sh.row(row)[13].value, automodel=automodel)
                                    if sh.row(row)[14].value:
                                        if Automodel2.objects.filter(name=sh.row(row)[14].value).exists():
                                            automodel2 = Automodel2.objects.filter(name=sh.row(row)[14].value).first()
                                        else:
                                            automodel2 = Automodel2.objects.create(name=sh.row(row)[14].value, automodel1=automodel1)
                                    if sh.row(row)[15].value:
                                        if Manufacturer.objects.filter(name=sh.row(row)[15].value).exists():
                                            manufacturer = Manufacturer.objects.filter(name=sh.row(row)[15].value).first()
                                        else:
                                            manufacturer = Manufacturer.objects.create(name=sh.row(row)[15].value)
                                    Product.objects.create(name=name, description=description, product_code=code, category=category, price=price,
                                                           manufacturer=manufacturer, subcategory=subcategory, subcategory1=subcategory1,
                                                           brand=brand, automodel=automodel, automodel1=automodel1, automodel2=automodel2)
                    except Exception as e:
                        raise e
                elif str(file).split('.')[-1] == 'csv':
                    data = csv.DictReader(codecs.iterdecode(file, 'utf-8'))
                    for row in data:
                        if row['Сategory']:
                            subcategory = None
                            subcategory1 = None
                            brand = None
                            automodel = None
                            automodel1 = None
                            automodel2 = None
                            manufacturer = None
                            if Category.objects.filter(name=row['Сategory']).exists():
                                category = Category.objects.filter(name=row['Сategory']).first()
                            else:
                                category = Category.objects.create(name=row['Сategory'])
                            if row['Subcategory1']:
                                if Subcategory.objects.filter(name=row['Subcategory1']).exists():
                                    subcategory = Subcategory.objects.filter(name=row['Subcategory1']).first()
                                else:
                                    subcategory = Subcategory.objects.create(name=row['Subcategory1'], category=category)
                            if row['Subcategory2']:
                                if Subcategory1.objects.filter(name=row['Subcategory2']).exists():
                                    subcategory1 = Subcategory1.objects.filter(name=row['Subcategory2']).first()
                                else:
                                    subcategory1 = Subcategory1.objects.create(name=row['Subcategory2'], subcategory=subcategory)
                            if row['Aufobrand']:
                                if Brand.objects.filter(name=row['Aufobrand']).exists():
                                    brand = Brand.objects.filter(name=row['Aufobrand']).first()
                                else:
                                    brand = Brand.objects.create(name=row['Aufobrand'])
                            if row['Automodel1']:
                                if Automodel.objects.filter(name=row['Automodel1']).exists():
                                    automodel = Automodel.objects.filter(name=row['Automodel1']).first()
                                else:
                                    automodel = Automodel.objects.create(name=row['Automodel1'], brand=brand)
                            if row['Automodel2']:
                                if Automodel1.objects.filter(name=row['Automodel2']).exists():
                                    automodel1 = Automodel1.objects.filter(name=row['Automodel2']).first()
                                else:
                                    automodel1 = Automodel1.objects.create(name=row['Automodel2'], automodel=automodel)
                            if row['Automodel3']:
                                if Automodel2.objects.filter(name=row['Automodel3']).exists():
                                    automodel2 = Automodel2.objects.filter(name=row['Automodel3']).first()
                                else:
                                    automodel2 = Automodel2.objects.create(name=row['Automodel3'], automodel1=automodel1)
                            if row['manufacturer']:
                                if Manufacturer.objects.filter(name=row['manufacturer']).exists():
                                    manufacturer = Manufacturer.objects.filter(name=row['manufacturer']).first()
                                else:
                                    manufacturer = Manufacturer.objects.create(name=row['manufacturer'])
                            code = row['Productcode']
                            name = row['Productname']
                            description = row['Shortdescription']
                            price = Decimal(row['Price'].replace(',', ''))
                            if name:
                                Product.objects.create(name=name, description=description, product_code=code, category=category, price=price,
                                                       manufacturer=manufacturer, subcategory=subcategory, subcategory1=subcategory1,
                                                       brand=brand, automodel=automodel, automodel1=automodel1, automodel2=automodel2)
        return redirect("..")


admin.site.register(UploadModel, CsvUploadAdmin)
