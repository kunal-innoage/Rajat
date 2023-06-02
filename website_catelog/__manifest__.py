{
    'name': 'Website Catelog',
    'version': '1.0',
    'summary': 'This module manages catelog for website',
    'category': 'Sales',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/website_catelog.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
