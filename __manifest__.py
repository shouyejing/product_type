# -*- coding: utf-8 -*-
{
    'name': "Types Produit",

    'summary': """
        Ajoute des types de produits""",

    'description': """
        Ajoute un type de produit aux produits (ex : Sucré, Salé, Dangereux ...).
    """,

    'author': "Groupe 3 - LP CODESI",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','account','sale'],

    # always loaded
    'data': 
    [
        'security/ir.model.access.csv',
        'views/type.xml',
        'views/devis.xml',
        'views/facture.xml',
        'views/typeProduct_View.xml'
    ],

    'application':True,
}
