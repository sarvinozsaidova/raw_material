import json
from django.http import JsonResponse
from .models import  RawMaterial, WarehouseBatch

def product_materials(request):
    data = json.loads(request.body)

    result = []

    for item in data['result']:
        product_name = item['product_name']
        product_qty = item['product_qty']
        product_materials = item['product_materials']

        materials_needed = []

        for material_info in product_materials:
            material_name = material_info['material_name']
            quantity_needed = material_info['qty']


            raw_material = RawMaterial.objects.get(name=material_name)

            
            remaining_qty = quantity_needed
            batches = WarehouseBatch.objects.filter(raw_material=raw_material, remainder__gt=0).order_by('price')

            for batch in batches:
                if remaining_qty <= batch.remainder:
                    materials_needed.append({
                        'warehouse_id': batch.id,
                        'material_name': material_name,
                        'qty': remaining_qty,
                        'price': batch.price
                    })
                    remaining_qty = 0
                    break
                else:
                    materials_needed.append({
                        'warehouse_id': batch.id,
                        'material_name': material_name,
                        'qty': batch.remainder,
                        'price': batch.price
                    })
                    remaining_qty -= batch.remainder

            if remaining_qty > 0:
                materials_needed.append({
                    'warehouse_id': None,
                    'material_name': material_name,
                    'qty': remaining_qty,
                    'price': None
                })

        result.append({
            'product_name': product_name,
            'product_qty': product_qty,
            'product_materials': materials_needed
        })

    return JsonResponse({'result': result})
