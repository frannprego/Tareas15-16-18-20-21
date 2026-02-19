from odoo import models, fields, api

class AlumnoSueno(models.Model):
    _name = 'alumno.sueno'
    _description = 'Registro de sueno'

    name = fields.Char(string='Alumno', required=True)
    nivel_sueno = fields.Integer(string='Nivel de Sueno')
    bebida_recomendada = fields.Char(string='Bebida', compute='_compute_bebida')

    @api.depends('nivel_sueno')
    def _compute_bebida(self):
        for record in self:
            if record.nivel_sueno and record.nivel_sueno > 5:
                record.bebida_recomendada = 'Cafe doble'
            else:
                record.bebida_recomendada = 'Cafe'

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_codigo_socio = fields.Char(string='Codigo de Socio')
    x_nivel_fidelidad = fields.Char(string='Nivel de Fidelidad', compute='_compute_nivel_fidelidad', store=True)

    @api.depends('x_codigo_socio')
    def _compute_nivel_fidelidad(self):
        for record in self:
            cod = record.x_codigo_socio or ""
            if cod.upper().startswith('G'):
                record.x_nivel_fidelidad = "Gold"
            else:
                record.x_nivel_fidelidad = "Premium"