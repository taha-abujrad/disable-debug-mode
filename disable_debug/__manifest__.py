# -*- coding: utf-8 -*-
{
    'name': "Disable Debug Mode",

    'summary': """
        Control The use of Odoo Debug Mode By Access Group""",

    'description': """
        This module is used to disable the odoo debug mode for all users except for those
        having the Use Debug Mode group, this feature is essential is production environment.
    """,

    'author': "Taha Abujrad",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
