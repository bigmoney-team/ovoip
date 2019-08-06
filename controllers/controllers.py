# -*- coding: utf-8 -*-
from odoo import http

# class OdooVoipApi(http.Controller):
#     @http.route('/odoo_voip_api/odoo_voip_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_voip_api/odoo_voip_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_voip_api.listing', {
#             'root': '/odoo_voip_api/odoo_voip_api',
#             'objects': http.request.env['odoo_voip_api.odoo_voip_api'].search([]),
#         })

#     @http.route('/odoo_voip_api/odoo_voip_api/objects/<model("odoo_voip_api.odoo_voip_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_voip_api.object', {
#             'object': obj
#         })