# -*- coding: utf-8 -*-

from odoo import models, fields, api

class legacy_projects(models.Model):
    _inherit = 'project.project'

    legacy_projects_id = fields.Integer(default=0, string='Legacy project ID')
