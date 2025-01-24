from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        """ Ocultar precios para el grupo 'Compra/Usuario Restringido' """
        res = super(PurchaseOrder, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

        # Verificar si el usuario pertenece al grupo Compra/Usuario Restringido
        restricted_group = self.env.ref('purchase_restrictions.group_restricted_user', raise_if_not_found=False)
        if restricted_group and restricted_group.id in self.env.user.groups_id.ids and view_type == 'form':
            doc = res['arch']
            # Ocultar campos de precios
            doc = doc.replace('<field name="price_unit"', '<field name="price_unit" invisible="1"')
            doc = doc.replace('<field name="price_subtotal"', '<field name="price_subtotal" invisible="1"')
            res['arch'] = doc
        return res

    @api.model
    def create(self, vals):
        """ Restringir creación de órdenes de compra a 'Proveedor Interno' """
        restricted_group = self.env.ref('purchase_restrictions.group_restricted_user', raise_if_not_found=False)
        if restricted_group and restricted_group.id in self.env.user.groups_id.ids:
            internal_supplier = self.env['res.partner'].search([('name', '=', 'Proveedor Interno')], limit=1)
            if vals.get('partner_id') != internal_supplier.id:
                raise ValueError("Solo puedes crear órdenes de compra con 'Proveedor Interno'.")
        return super(PurchaseOrder, self).create(vals)
