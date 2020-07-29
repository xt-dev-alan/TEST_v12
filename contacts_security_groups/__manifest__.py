# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': "Contacts security groups",
    'version': "12.0.0.0",
    'category': "Contacts",
    'summary': "Adds another two groups for extra security",
    'description': """
        Adds another two groups for extra security
    """,
    'author': "XETECHS",
    "website": "",
    'depends': ['account','base','account_reports','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/permissions.xml',
        'views/res_users.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
