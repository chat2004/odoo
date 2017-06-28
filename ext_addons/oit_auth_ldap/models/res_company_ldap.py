from odoo import api, models


class CompanyLDAP(models.Model):
    _inherit = 'res.company.ldap'

    def map_ldap_attributes(self, conf, login, ldap_entry):
        result = super(CompanyLDAP, self).map_ldap_attributes(conf, login,
                                                              ldap_entry)
        if result:
            result['email'] = ldap_entry[1]['mail'][0]

        return result
