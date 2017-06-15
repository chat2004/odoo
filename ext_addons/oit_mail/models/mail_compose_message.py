# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OitMailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def send_mail(self, auto_commit=False):
        """ Process the wizard content and proceed with sending the related
            email(s), rendering any template patterns on the fly if needed. """
        if self.is_log and self.subtype_id:
            self.is_log = False

        res = super(OitMailComposer, self).send_mail(auto_commit)
        return res
