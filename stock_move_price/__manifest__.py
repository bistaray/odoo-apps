# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Stock Move Price",
    "version" : "1.10.1",
    "author" : "Bista Solutions",
    'category': 'Warehouse',
    "summary": "Add unit price to Stock Move Reports (Bista)",
    'description': "For Odoo Version 10.0, this module adds the unit price to the list and form views of Stock Moves.",
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/erp-implementation-company/erp-customization-company',
    "depends" : ["base","stock"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        'views/stock_move.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
