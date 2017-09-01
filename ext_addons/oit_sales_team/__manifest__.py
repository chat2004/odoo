# -*- coding: utf-8 -*-
{
    'name': "OutsourceIt Custom Sales",

    'summary': """
        Custom features for Sales
        """,

    'description': """
        More security for Sale messages
    """,

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sales_team', 'oit_mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/res_partner_security.xml',
        'security/sales_team_security.xml',
    ],
}
