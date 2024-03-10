from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(RawMaterial)
admin.site.register(ProductRawMaterial)
admin.site.register(WarehouseBatch)
