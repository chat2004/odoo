# -*- coding: utf-8 -*-
{
    'name': "OutsourceIt Base Module",

    'summary': """
        OutsourceIt Base Module
        Customize res.partner
        """,

    'description': """
        OutsourceIt Base Module
        Customize res.partner
    """,

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
}
