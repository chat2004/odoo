# -*- coding: utf-8 -*-
{
    'name': "OutsourceIt Custom Mail Message",

    'summary': 'Customized mail message module',

    'description': '',

    'author': "OutsourceIt",
    'website': "http://www.outsourceit-int.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/mail_message_data.xml',
        'security/mail_security.xml',
        'views/mail_compose_message_views.xml',
        'views/mail_message_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
