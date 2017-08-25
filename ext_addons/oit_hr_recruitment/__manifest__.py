# -*- coding: utf-8 -*-
{
    'name': "OutsourceIt Custom Recruitment",

    'summary': "Custom Recruitment process",

    'description': "",

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_recruitment', 'oit_mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/hr_recruitment_security.xml',
        'views/hr_recruitment_views.xml',
        'views/hr_job_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
