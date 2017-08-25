from odoo import api, fields, models


class OitJob(models.Model):
    _inherit = 'hr.job'

    @api.multi
    def action_get_attachment_tree_view(self):
        action = self.env.ref('oit_hr_recruitment.oit_hr_job_documents').read()[0]
        action['context'] = {
            'default_res_model': self._name,
            'default_res_id': self.ids[0]
        }
        action['search_view_id'] = (self.env.ref(
            'hr_recruitment.ir_attachment_view_search_inherit_hr_recruitment').id,)
        action['domain'] = ['|', '&', ('res_model', '=', 'hr.job'),
                            ('res_id', 'in', self.ids), '&',
                            ('res_model', '=', 'hr.applicant'), (
                            'res_id', 'in', self.mapped('application_ids').ids)]
        return action
