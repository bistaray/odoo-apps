# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Portal Attachments",
    "version" : "1.10.1",
    "author" : "Bista Solutions",
    'category': 'Attachment',
    "summary": "Display Partner Attachments on Portal (Bista)",
    'description': "For Odoo Version 10.0, this module publishes attachments for portal users.",
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/erp-implementation-company/erp-customization-company',
    "depends" : ["document","website_portal"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        'views/portal_attachment_view.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
