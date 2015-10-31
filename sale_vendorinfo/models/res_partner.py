# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendor_info = fields.Text(string='Vendor Information')

