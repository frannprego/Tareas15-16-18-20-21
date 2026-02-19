from odoo import http

class HolaMundo(http.Controller):
    @http.route('/hola', auth='public', website=True)
    def hola_mundo(self, **kw):
        return "<h1>¡Hola! Soy Fran y estoy mirando el PAOK-CELTA</h1>"