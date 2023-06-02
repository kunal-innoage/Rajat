from odoo import models,fields

class WebsiteCatelog(models.Model):
    _name = 'website.catelog'
    _description = 'Website Catelog'
    _rec_name = "tag_name"

    sku = fields.Char(string='SKU')
    tag_name = fields.Char(string='SKU Tag Name')
    final_formula = fields.Html(string='FINAL Formula')
    backing_material = fields.Char(string='Backing Material')
    desc = fields.Html(string='Description')
    model_name = fields.Char(string='Model Name')
    collection = fields.Char(string='Collection')
    main_color = fields.Char(string='Main Colour')
    colors = fields.Char(string='Colours')
    style = fields.Char(string='Style')
    material = fields.Char(string='Material')
    product_dimension = fields.Char(string='Product Dimensions')
    weight = fields.Char(string='Weight')
    pile_height = fields.Char(string='Pile Height ')
    care_instructions = fields.Char(string='Care Instructions: Hand/Machine')
    shape = fields.Char(string='Shape')
    certifications = fields.Char(string='Certifications')
    use = fields.Char(string='Use')
    feature1 = fields.Char(string='Features 1')
    feature2 = fields.Char(string='Features 2')
    feature3 = fields.Char(string='Features 3')
    feature4 = fields.Char(string='Features 4')
    feature5 = fields.Char(string='Features 5')
    
