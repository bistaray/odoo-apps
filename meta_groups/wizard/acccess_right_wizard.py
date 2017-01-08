# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class AccessRight(models.TransientModel):
    _name = "access.right"

    access_right = fields.Many2one('access.access',
                                   string='Meta Group',type="Selection")

    @api.multi
    def apply_access(self):
        for g in self:
            if self._context and self._context.get('active_id') and g.access_right:
                user_rec = self.env['res.users'].browse(self._context.get('active_id'))
                user_rec.groups_id = [(6, 0, g.access_right.groups_id.ids)]
            else:
                raise exceptions.Warning(
                    _('Please create a Meta Group via '
                      'Settings --> Users --> Meta Groups.'))
