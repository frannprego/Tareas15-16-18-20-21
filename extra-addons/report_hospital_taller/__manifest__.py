{
    'name': 'Tarea 20: Reportes de Taller',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Añade hoja de taller y modifica el horario en presupuestos',
    'depends': ['sale'],
    'data': [
        'report/ir_actions_report.xml',
        'report/hoja_taller_report.xml',
        'report/sale_report_inherit.xml',
    ],
    'installable': True,
    'application': False,
}