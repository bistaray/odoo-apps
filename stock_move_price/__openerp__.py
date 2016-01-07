# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Stock Move Price",
    "version" : "1.9.1",
    "author" : "Bista Solutions",
    'category': 'Inventory Management',
    "summary": "Add unit price to Stock Moves Reports (Bista)",
    'description': "For Odoo Enterprise Version 9.0, this module adds the unit price to the list and form views of Stock Moves.",
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/odoo-implementation-partners',
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
