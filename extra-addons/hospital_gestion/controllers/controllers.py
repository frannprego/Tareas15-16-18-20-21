# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalGestion(http.Controller):
#     @http.route('/hospital_gestion/hospital_gestion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_gestion/hospital_gestion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_gestion.listing', {
#             'root': '/hospital_gestion/hospital_gestion',
#             'objects': http.request.env['hospital_gestion.hospital_gestion'].search([]),
#         })

#     @http.route('/hospital_gestion/hospital_gestion/objects/<model("hospital_gestion.hospital_gestion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_gestion.object', {
#             'object': obj
#         })

