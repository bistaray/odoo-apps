
# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    vendor_info = fields.Text(related="commercial_partner_id.vendor_info",string='Vendor Information')

