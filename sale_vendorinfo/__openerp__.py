# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Sales Vendor Information",
    "version" : "1.9.1",
    "author" : "Bista Solutions",
    'category': 'Sales',
    "summary": "Vendor Info. on Customer, Order, Shipment, Invoice (Bista)",
    'description': """
For Odoo Enterprise Version 9.0, this module supports Vendor Information.  Some large Customers have additional requirements for products sold to them.  
They require Vendor Information listed on all documents - Orders, Shipments and Invoices.  
Typically they have a Seller identification number and/or an Accounts Payable identification number that links you to their business system(s).  
This module allows Vendor Information to be stored on these Large Customers (partner records) and propagated to Orders, Shipments and Invoices
    """,
    'maintainer': "Bista Solutions",
    'website': 'http://www.bistasolutions.com/odoo-implementation-partners',
    "depends" : ["base","sale_stock","account"],
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
        'views/account_invoice.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
