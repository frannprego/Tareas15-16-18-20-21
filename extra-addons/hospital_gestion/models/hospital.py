from odoo import models, fields

class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'

    name = fields.Char(string='Nombre y Apellidos', required=True)
    sintomas = fields.Text(string='Síntomas')

class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico'

    name = fields.Char(string='Nombre y Apellidos', required=True)
    numero_colegiado = fields.Char(string='Número de Colegiado', required=True)

class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico'

    name = fields.Text(string='Diagnóstico', required=True)
    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True)
    medico_id = fields.Many2one('hospital.medico', string='Médico', required=True)