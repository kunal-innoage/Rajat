{
    'name' : "suryaweb",
    'depends' : ['website','website_sale','website_catelog','product','product_image_types'],
    'author' : "InnoAge Technologies",
    'category': 'Website/Website',
    'assets': {
        'web.assets_frontend': [
            'Suryaweb/static/src/scss/style.scss',
            'Suryaweb/static/src/scss/styles.scss',
            'Suryaweb/static/src/scss/product.scss',
            'Suryaweb/static/src/scss/aboutus.scss',
            'Suryaweb/static/src/scss/contactus.scss',
            'Suryaweb/static/src/scss/policy.scss',
            'Suryaweb/static/src/js/styleproduct.js',
            'Suryaweb/static/src/js/productstyle.js'
        ],
   },
   'data': [
        "security/ir.model.access.csv",
        "views/assests.xml",
        "views/template.xml",
        "views/product.xml",
        "views/product_image.xml",
        "views/policy.xml",
        "views/policy_banner.xml",
        "views/snippets/crousel.xml",      
        "views/snippets/productstyle.xml",
        "views/snippets/inno_banner.xml",
        "views/snippets/textimage.xml",
        "views/snippets/features.xml",
        "views/snippets/shoppagebanner.xml",
        "views/snippets/shopproductsize.xml",
        "views/snippets/apartmentrugs.xml",
        "views/snippets/latestblogs.xml",
        "views/snippets/marketplace.xml",
        "views/snippets/inno_heading.xml",
        "views/snippets/collection.xml",
        "views/snippets/contactusbanner.xml",
        "views/snippets/aboutusbanner.xml",
        "views/snippets/productpagebanner.xml",
        "views/snippets/aboutus/marqueeref.xml",
        
   ],
   'license': 'LGPL-3',
}
