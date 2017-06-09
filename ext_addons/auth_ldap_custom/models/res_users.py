from odoo.exceptions import AccessDenied

from odoo import api, models, registry, SUPERUSER_ID


class Users(models.Model):
    _inherit = "res.users"

    @classmethod
    def _login(cls, db, login, password):
        user_id = super(Users, cls)._login(db, login, password)
        if user_id:
            with registry(db).cursor() as cr:
                self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
                SudoUser = self.env['res.users'].sudo(user_id)
                SudoUser._update_last_login()

        return user_id
