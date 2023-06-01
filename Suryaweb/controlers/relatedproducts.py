import logging
from odoo.http import request
from odoo import http
_logger = logging.getLogger(__name__)


class RelatedProducts(http.Controller):

    @http.route('/product/related_products', auth="none", type="json", methods=['POST'])
    def product_related(self, product_id, **kwargs):
        
        product = request.env['product.template'].search([('id', '=', product_id)])
        _logger.info("~~~~~~~~~~~%r~~~~~~~~~", product.alternative_product_ids)
        values={
            'products': product.alternative_product_ids
        }
        return True
            
        

        
                                           
  
    