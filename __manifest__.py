{
    'name': "Restricciones en Compras",
    'version': '1.0',
    'depends': ['purchase'],
    'author': "David Gaytan",
    'category': 'Compras',
    'description': """
    Este módulo implementa restricciones en el módulo de compras para el grupo "Usuario Restringido":

    - Oculta los precios de los productos en las órdenes de compra.
    - Muestra solo el proveedor "Proveedor Interno".
    """,
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': True,
}