import xmlrpc.client

url = 'http://localhost:8070'
db = 'odoo'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

clientes = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
    [[['is_company', '=', True]]],
    {'fields': ['name', 'email'], 'limit': 5})

print("MIS CLIENTES")
for c in clientes:
    email = c['email'] if c['email'] else 'Sin email'
    print(f"Empresa: {c['name']} | Email: {email}")