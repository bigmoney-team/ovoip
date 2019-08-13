# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo import models, fields, api


class AccountFollowupReport(models.AbstractModel):
    _inherit = "account.followup.report"

    def _execute_followup_partner(self, partner):
        if partner.followup_status == 'in_need_of_action':
            level = partner.get_followup_level()
            followup_line = self.env[
                'account_followup.followup.line'].browse(level[0])
            if followup_line.automated_call:
                return_url = self.env.user.company_id.return_url or False
                if return_url:
                    msg = self._get_default_summary()
                    payload = {
                        'rowid': self.id,
                        'customerid': partner.id,
                        'overdue': partner.total_overdue,
                        'mobile': partner.phone}
                    r = http.requests.post(return_url, data=json.dumps(payload))
            super(AccountFollowupReport, self)._execute_followup_partner(
                partner)
        return None
