# -*- coding: utf-8 -*-
from odoo import http

# class MailCustom(http.Controller):
#     @http.route('/mail_custom/mail_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mail_custom/mail_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mail_custom.listing', {
#             'root': '/mail_custom/mail_custom',
#             'objects': http.request.env['mail_custom.mail_custom'].search([]),
#         })

#     @http.route('/mail_custom/mail_custom/objects/<model("mail_custom.mail_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mail_custom.object', {
#             'object': obj
#         })