# See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Credit Limit',
    'version': '12.0.1.0.0',
    'category': 'Partner',
    'license': 'AGPL-3',
    'author': 'Luis Aquino --> laquino@xetechs.com',
    'website': 'https://xetechs.odoo.com',
    'maintainer': 'Xetechs, S.A.',
    'summary': 'Set credit limit warning',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
