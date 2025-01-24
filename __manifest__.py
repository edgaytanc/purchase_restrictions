{
    'name': 'Restricciones en Compras',
    'version': '1.0',
    'author': 'Tu Nombre',
    'category': 'Purchases',
    'summary': 'Restricciones personalizadas para usuarios en el módulo de compras',
    'description': """
        Este módulo restringe a los usuarios del grupo "Usuario Restringido":
        - No pueden ver los precios de los productos en las órdenes de compra.
        - Solo pueden trabajar con un proveedor específico ("Proveedor Interno").
    """,
    'depends': ['purchase'],
    'data': [
        'security/custom_restrictions_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
