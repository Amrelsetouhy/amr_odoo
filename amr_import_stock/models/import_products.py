import csv
from odoo import api, models

class MyClass(models.Model):
    _inherit = 'product.template'

    def process_csv_file(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            product_cache = {}

            for row in reader:
                product_name = row.get('name', '').strip("()',")
                default_code = row.get('default_code', '').strip("()',")
                location = int(row.get('location_id', '0'))  # Removed extra parenthesis
                categ_id = int(row.get('categ_id', '0'))
                inventory_quantity = float(row.get('inventory_quantity', '0.00'))
                standard_price = float(row.get('standard_price', '0.00'))
                print(product_name, default_code, location, inventory_quantity, standard_price)
                key = (product_name, default_code)

                if key in product_cache:
                    # Product already exists, update standard price in product
                    product = product_cache[key]
                    product.write({
                        'standard_price': standard_price,
                    })

                    # Update inventory quantity in stock.quant
                    product_quant = self.env['stock.quant'].search([
                        ('product_id', '=', product.id),
                        ('location_id', '=', location),
                    ])
                    #product_quant.action_set_inventory_quantity()
                    product_quant.inventory_quantity = inventory_quantity + lastqty  # Corrected field name
                    product_quant.action_apply_inventory()
                    lastqty = lastqty + inventory_quantity
                else:
                    lastqty = 0
                    # Create a new product
                    product = self.env['product.product'].create({
                        'name': product_name,
                        'default_code': default_code,
                        'standard_price': standard_price,
                        'categ_id' : categ_id,
                    })

                    # Create a new stock.quant record
                    self.env['stock.quant'].create({
                        'product_id': product.id,
                        'location_id': location,
                        'inventory_quantity': inventory_quantity,  # Corrected field name
                    })
                    product_quant = self.env['stock.quant'].search([
                        ('product_id', '=', product.id),
                        ('location_id', '=', location),
                    ])
                    product_quant.action_apply_inventory()
                    lastqty = inventory_quantity
                    # Add the newly created product to the cache
                    product_cache[key] = product
