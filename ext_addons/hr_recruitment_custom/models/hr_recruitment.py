from odoo import api, fields, models


class CustomApplicant(models.Model):
    _inherit = 'hr.applicant'

    salary_visible = fields.Boolean(string="User", compute='_get_user')

    @api.depends('salary_visible')
    def _get_user(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('hr_recruitment.group_hr_recruitment_manager'):
            self.salary_visible = True
        else:
            self.salary_visible = False
