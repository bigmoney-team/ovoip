# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountFolloupFollowupLine(models.Model):
    _inherit = ["account_followup.followup.line"]

    automated_call = fields.Boolean(string="Automated Call")
