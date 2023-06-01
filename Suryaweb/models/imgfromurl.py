from odoo import models, fields,api, _
import logging
from PIL import Image
import requests

import base64
_logger = logging.getLogger(__name__)


class ProductImage(models.Model):
    _inherit = "product.image.type"

    # image = fields.Binary(string="Image", store=True, attachment=False)
    
    
    def get_image_from_url(self, data):

        file_data = ""
        try:
            file_data = base64.b64encode(data).replace(b"\n", b"")
            # data = base64.b64encode(requests.get(data.strip()).content)
        except Exception as e:
            _logger.warning("Can’t load the image from URL %s" % data)
            logging.exception(e)
        return file_data
    
    def get_product_image_id(self, image_url, product):
        
        # Add Flat Image 
        response = False
        try:
            _logger.info("Getting Image data from url ~~~~~~~~~ %r ~~~~~~~", image_url)
            response = requests.get(image_url)
        except Exception as e:
            _logger.info("Error while getting URL status ~~~~~~~~~~ %r ~~~~!!!!!!!!!",e)
        if response:
            if response.status_code == 200:
                data =  self.get_image_from_url(response.content)
                if data:
                    product_image_id = self.env['product.image'].create({'image_1920':data})
                    return product_image_id
        return False
        
     
    def get_image_url(self):
        expired = []
        for rec in self:
            if rec.sku:
                products = self.env['product.template'].search([('default_code','=',rec.sku)],limit=1)
                for product in products:
                    if product.flat_image:
                        
                        # Check for existing flat image in this product 
                        # existing_image = False
                        # to_delete_product_image = False
                        # for product_image in product.product_template_image_ids:
                        #     if "Flat" in product_image.name:
                        #         existing_image = True
                        #         to_delete_product_image = product_image
                        #         break
                        # if to_delete_product_image:
                            # Delete Product Image 
                            # image_id = self.search(['name','=', 'product.default_code+ Flat']).unlink()
                            # product.product_template_image_ids = product_image_id.unlink()
   
                        
                        try:
                            product_image_id = self.get_product_image_id(product.flat_image, product)
                            if product_image_id:
                                product.image_ += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                        
                    if product.corner:
                        
                       # Check for existing corner image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "Corner" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.corner, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.fold_image:
                         
                       # Check for existing fold_image  in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "fold_image" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.fold_image, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.front:
                          
                       # Check for existing front image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "front" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.front, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.roomscene1:
                             
                       # Check for existing roomscene1 image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "roomscene1" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.roomscene1, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.roomscene2:
                              
                       # Check for existing roomscene2 image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "roomscene2" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.roomscene2, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.roomscene3:
                               
                       # Check for existing roomscene3 image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "roomscene3" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.roomscene3, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.texture:
                              
                       # Check for existing texture image in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "texture" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.texture, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                    if product.video:
                              
                       # Check for existing video in this product 

                        existing_image = False
                        to_delete_product_image = False
                        for product_image in product.product_template_image_ids:
                            if "video" in product_image.name:
                                existing_image = True
                                to_delete_product_image = product_image
                                break
                        if to_delete_product_image:
                            # Delete Product Image 
                            pass
                        
                        try:
                            product_image_id = self.get_product_image_id(product.video, product)
                            if product_image_id:
                                product.product_template_image_ids += product_image_id
                                _logger.info("~~~~~~~~~~~~ Product Image Added ~~~~~~~~~~~~~~")
                            else:
                                _logger.info("Error in getting image data from URL ~~~~~~~!!!!!!!!")
                                
                        except Exception as e:
                            _logger.info("Error while adding product image ~~~~~~ %r ~~~~~!!!!!!!!!!`", e)
                            
                            
                            
                    
                    if expired:
                        _logger.info("~~~~~~~~~~~~  %r   ~~~~~~~~~~~~~", expired)
                        raise ValidationError(_('Error URLS - %s',expired))







    


       

                     
                   
         

    