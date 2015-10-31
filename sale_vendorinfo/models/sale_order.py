
# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vendor_info = fields.Text(related="partner_id.vendor_info",string='Vendor Information')

