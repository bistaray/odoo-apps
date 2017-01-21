# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2012 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': 'Show Message Recipients',
    'version': '1.10.1',
    "author": 'Bista Solutions Pvt. Ltd.',
    'website': 'https://www.odoo.com/page/mrp-cloud-software',
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
