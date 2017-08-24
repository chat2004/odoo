from odoo import api, fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    attachment_number = fields.Integer(compute='_get_attachment_number',
                                       string="Number of Attachments")

    @api.multi
    def _get_attachment_number(self):
        read_group_res = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'hr.employee'), ('res_id', 'in', self.ids), ('res_field', '=', False)],
            ['res_id'], ['res_id'])
        attach_data = dict(
            (res['res_id'], res['res_id_count']) for res in read_group_res)
        for record in self:
            record.attachment_number = attach_data.get(record.id, 0)

    @api.multi
    def action_get_attachment_tree_view(self):
        attachment_action = self.env.ref('oit_hr.oit_action_hr_employee_documents')
        action = attachment_action.read()[0]
        action['context'] = {'default_res_model': self._name,
                             'default_res_id': self.ids[0]}
        action['domain'] = str(
            ['&', ('res_model', '=', self._name), ('res_id', 'in', self.ids)])
        action['search_view_id'] = (self.env.ref(
            'oit_hr.oit_ir_attachment_view_search_inherit_hr_employee').id,)
        return action
