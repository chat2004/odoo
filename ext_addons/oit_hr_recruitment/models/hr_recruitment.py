from odoo import api, fields, models


class OitApplicant(models.Model):
    _inherit = 'hr.applicant'

    def _get_user_default(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('hr_recruitment.group_hr_recruitment_manager'):
            return True
        else:
            return False

    salary_visible = fields.Boolean(string="Salary Visible", compute='_get_user',
                                    default=_get_user_default)

    @api.depends('salary_visible')
    def _get_user(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('hr_recruitment.group_hr_recruitment_manager'):
            self.salary_visible = True
        else:
            self.salary_visible = False
