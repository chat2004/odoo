# -*- coding: utf-8 -*-
from odoo import http

# class OitBase(http.Controller):
#     @http.route('/oit_base/oit_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oit_base/oit_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oit_base.listing', {
#             'root': '/oit_base/oit_base',
#             'objects': http.request.env['oit_base.oit_base'].search([]),
#         })

#     @http.route('/oit_base/oit_base/objects/<model("oit_base.oit_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oit_base.object', {
#             'object': obj
#         })