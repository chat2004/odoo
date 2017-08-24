# -*- coding: utf-8 -*-
{
    'name': "OutsourceIt Custom Human Resource Management",

    'summary': """
        Custom OutsourceIt Human Resource, Employee documents
        """,

    'description': """
        Employee documents
    """,

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_views.xml',
    ],
}
