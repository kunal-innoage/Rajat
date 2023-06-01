
odoo.define('Suryaweb.related_product', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $( document ).ready(function() {
            var productId = $('#product_details h1').attr('data-oe-id')
            console.log(productId)

            // let productImgRow = this.el.Selector("product_img_row")

            if(productId){

                ajax.jsonRpc('/product/related_products', 'call', {'product_id' : productId,}).then(function (json_data) {
                    console.log(json_data)
                    
                });
            }

    });
    
    
});
