# -*- coding: utf-8 -*-
from odoo import http

# class AuthLdapCustom(http.Controller):
#     @http.route('/auth_ldap_custom/auth_ldap_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auth_ldap_custom/auth_ldap_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auth_ldap_custom.listing', {
#             'root': '/auth_ldap_custom/auth_ldap_custom',
#             'objects': http.request.env['auth_ldap_custom.auth_ldap_custom'].search([]),
#         })

#     @http.route('/auth_ldap_custom/auth_ldap_custom/objects/<model("auth_ldap_custom.auth_ldap_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auth_ldap_custom.object', {
#             'object': obj
#         })