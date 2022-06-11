# -*- coding: utf-8 -*-
# from odoo import http


# class Resort(http.Controller):
#     @http.route('/resort/resort/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/resort/resort/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('resort.listing', {
#             'root': '/resort/resort',
#             'objects': http.request.env['resort.resort'].search([]),
#         })

#     @http.route('/resort/resort/objects/<model("resort.resort"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('resort.object', {
#             'object': obj
#         })
