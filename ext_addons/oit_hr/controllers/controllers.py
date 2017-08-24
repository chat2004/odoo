# -*- coding: utf-8 -*-
from odoo import http

# class OitHr(http.Controller):
#     @http.route('/oit_hr/oit_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oit_hr/oit_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oit_hr.listing', {
#             'root': '/oit_hr/oit_hr',
#             'objects': http.request.env['oit_hr.oit_hr'].search([]),
#         })

#     @http.route('/oit_hr/oit_hr/objects/<model("oit_hr.oit_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oit_hr.object', {
#             'object': obj
#         })