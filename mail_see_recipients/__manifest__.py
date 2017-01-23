# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2012 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': 'Show Message Recipients',
    'version': '1.10.2',
    "author": 'Bista Solutions Pvt. Ltd.',
    'website': 'https://www.odoo.com/page/mrp-cloud-software',
	'summary': "More intuitive message sending (Bista)",
    'description': "For Odoo Enterprise Version 9.0, this module replaces the default Apps Switcher background with a single gray image background. By replacing the image file in this module, you can further personalize the Odoo Apps Switcher page. This is a very simply module. It serves as an ideal example for those who are learning how to build modules with Odoo.",	
    'category': 'Mail',
    'sequence': 10,
	'images': ['static/description/mail_see_recipients.png'],
    'depends': [
        'mail',
        'web',
        'web_editor',
        'web_planner'
    ],
    'data': [
             'views/mail_see_recipients.xml',
            ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
