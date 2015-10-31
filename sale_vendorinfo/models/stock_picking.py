
# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vendor_info = fields.Text(related="sale_id.partner_id.vendor_info",string='Vendor Information')

