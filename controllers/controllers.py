# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OdooVoipApi(http.Controller):
    @http.route('/odoo_voip_api/odoo_voip_api/return',
                auth='public', type='http', methods=['POST'])
    def return_data(self, **post):
        if post.get('partner_id', False):
            partner = request.env['res.partner'].browse(
                [post.get('partner_id')])
            partner.write({
                'call_success': post.get('call_success', False),
                'call_minutes': post.get('call_minutes', False),
                'record_voice': post.get('record_voice', False)
            })
