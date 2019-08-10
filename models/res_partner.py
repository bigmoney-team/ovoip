# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    call_success = fields.Boolean()
    call_minutes = fields.Float()
    record_voice = fields.Binary()
