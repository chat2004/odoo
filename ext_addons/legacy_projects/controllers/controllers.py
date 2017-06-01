# -*- coding: utf-8 -*-
from odoo import http

# class LegacyProjects(http.Controller):
#     @http.route('/legacy_projects/legacy_projects/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legacy_projects/legacy_projects/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('legacy_projects.listing', {
#             'root': '/legacy_projects/legacy_projects',
#             'objects': http.request.env['legacy_projects.legacy_projects'].search([]),
#         })

#     @http.route('/legacy_projects/legacy_projects/objects/<model("legacy_projects.legacy_projects"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legacy_projects.object', {
#             'object': obj
#         })