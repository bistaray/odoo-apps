# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Custom App Switcher",
    "version" : "1.9.2",
    "author" : "Bista Solutions",
    "category" : "Extra Tools",
	"summary": "Change App Switcher background image (Bista)",
    'description': "For Odoo Enterprise Version 9.0, this module replaces the default App Switcher background with a single gray image background. By replacing the image file in this module, you can further personalize the Odoo App Switcher page. This is a very simply module. It serves as an ideal example for those who are learning how to build modules with Odoo.",
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/odoo-implementation-partners',
    'images': ['static/description/custom_app_switcher.png'],
    "depends" : ["base"],
    "init_xml" : [],
    "demo_xml" : [],
        "data" : [
        'web.assets_backend.xml',
    ],
    "test" : [
    ],
    "images": ['static/description/custom_app_switcher.png'],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
