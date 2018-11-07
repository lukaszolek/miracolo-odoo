from odoo import fields, models

class Patient(models.Model): 
    
    _inherit = 'res.partner' 
    is_patient = fields.Boolean(string=u'Is patient?')
    
    interested_in = fields.Many2many(
        'miracolo.servicetype',
        string=u'Interested in'
    )