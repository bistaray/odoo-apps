from odoo import _, api, fields, models

class MailComposer(models.TransientModel):
    """ Generic message composition wizard. You may inherit from this wizard
        at model and view levels to provide specific features.
    """
    _inherit = 'mail.compose.message'
    
    ''' overried default_get method to set default value for partner_ids and subject of mail'''
    @api.model
    def default_get(self, fields):
        result = super(MailComposer, self).default_get(fields)
        partner_list = []
        if self._context.get('default_model'):
            result['model'] = str(self._context.get('default_model')) # updated default value for model
        if self._context.get('sub'):
            result['subject'] = str(self._context.get('sub')) # updated default value for subject
        if self._context.get('partner_ids'):
            partners = self._context.get('partner_ids')
            for partner in partners:
                p_id = partner.get('res_id')
                partner_list.append(p_id)
            result['partner_ids'] = [(6, 0, partner_list)] # updated default value for partner_ids
        return result