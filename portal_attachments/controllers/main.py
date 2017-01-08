# -*- coding: utf-8 -*-
import datetime

from openerp import http
from openerp.http import request


class WebsitePortalAttachment(http.Controller):

    @http.route(['/my/my_attachments'], type='http', auth="user", website=True)
    def my_attachment(self):
        if request.env.user:
		partner = request.env.user.partner_id
		att = request.env['ir.attachment'].sudo().search([
						('res_id', '=', partner.id),
						('res_model','=','res.partner'),
						('type','=','binary')])
		values = {
		    'attachment_details': att,
		}
		return request.render("portal_attachments.my_attachments", values)
	else:
		return request.render("portal_attachments.my_attachments", {})
