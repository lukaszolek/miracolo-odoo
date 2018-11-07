# -*- coding: utf-8 -*-
from odoo import http

# class Miracolo(http.Controller):
#     @http.route('/miracolo/miracolo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miracolo/miracolo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('miracolo.listing', {
#             'root': '/miracolo/miracolo',
#             'objects': http.request.env['miracolo.miracolo'].search([]),
#         })

#     @http.route('/miracolo/miracolo/objects/<model("miracolo.miracolo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miracolo.object', {
#             'object': obj
#         })