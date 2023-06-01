
from odoo import models, fields


class Innoproducts(models.Model):
    _inherit=["product.template"]
 


    prod_desc = fields.Text("Product More Information")
    sku = fields.Char("SKU")
    tags = fields.Char("Tags")
    product_id = fields.Char("Product Id")
    