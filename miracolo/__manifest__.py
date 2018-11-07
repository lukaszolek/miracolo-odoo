# -*- coding: utf-8 -*-
{
    'name': "Miracolo Clinic Management System",

    'summary': """
        Patient/Operations management system for Miracolo Clinic - innovative endometriosis clinic.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Miracolo Clinic",
    'website': "http://miracolo.clinic",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patient_menu.xml',
        'views/res_partner_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'data/miracolo.servicetype.csv'
    ],
}