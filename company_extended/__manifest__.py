# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Company Extended Details",
    "version" : "1.10.1",
    "author" : "Bista Solutions",
    'category': 'Multi Company',
    "summary": "Add details to Company list view (Bista)",
    'description': "For Odoo Version 10.0, this module adds the Country, Currency and Parent Company to the Companies TreeView.",
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/erp-implementation-company/erp-customization-company',
    "depends" : ["base"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        'views/res_company.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
