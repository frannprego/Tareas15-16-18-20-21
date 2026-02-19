import xmlrpc.client

url = 'http://localhost:8070'
db = 'odoo_sxe'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

print("Forzando creación de contacto visible...")

nuevo_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': 'Contacto_Tarea21_Apartado3',
    'email': 'test@ejemplo.com',
    'is_company': True,
    'type': 'contact'
}])

print(f"¡Exito! ID generado: {nuevo_id}")