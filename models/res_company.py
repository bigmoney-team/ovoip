# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    return_url = fields.Char(string='Return URL')
