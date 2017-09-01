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
    meeting_count = fields.Integer("# Meetings",
                                   compute='_compute_meeting_count')

    @api.depends('salary_visible')
    def _get_user(self):
        res_user = self.env['res.users'].search([('id', '=', self._uid)])
        if res_user.has_group('hr_recruitment.group_hr_recruitment_manager'):
            self.salary_visible = True
        else:
            self.salary_visible = False

    @api.multi
    def action_get_attachment_tree_view(self):
        attachment_action = self.env.ref('oit_hr_recruitment.oit_hr_applicant_resumes')
        action = attachment_action.read()[0]
        action['context'] = {'default_res_model': self._name,
                             'default_res_id': self.ids[0]}
        action['domain'] = str(
            ['&', ('res_model', '=', self._name), ('res_id', 'in', self.ids)])
        action['search_view_id'] = (self.env.ref(
            'hr_recruitment.ir_attachment_view_search_inherit_hr_recruitment').id,)
        return action

    @api.multi
    def _compute_meeting_count(self):
        for record in self:
            if record.partner_id:
                record.meeting_count = len(record.partner_id.meeting_ids)
