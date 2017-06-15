# -*- coding: utf-8 -*-
{
    'name': "OutousrceIt Custom LDAP",

    'summary': """Custom LDAP authentication""",

    'description': """
        Fix update LDAP user login history
    """,

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['auth_ldap'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
