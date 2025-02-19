from odoo import models, fields, api, exceptions

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def default_get(self, fields):
        """ Forzar el proveedor "Proveedor Interno" para usuarios restringidos antes de mostrar el formulario """
        res = super(PurchaseOrder, self).default_get(fields)

        restricted_group = self.env.ref('purchase_restrictions.group_restricted_user', raise_if_not_found=False)

        if restricted_group and restricted_group.id in self.env.user.groups_id.ids:
            internal_supplier = self.env['res.partner'].search([('name', '=', 'Proveedor Interno')], limit=1)
            if not internal_supplier:
                raise exceptions.UserError("El proveedor 'Proveedor Interno' no está configurado. Por favor, contacte al administrador.")

            # Forzar el proveedor "Proveedor Interno"
            res['partner_id'] = internal_supplier.id

        return res

    # @api.model
    # def create(self, vals):
    #     """ Validar que los usuarios restringidos solo usen el proveedor "Proveedor Interno" al guardar """
    #     restricted_group = self.env.ref('purchase_restrictions.group_restricted_user', raise_if_not_found=False)

    #     if restricted_group and restricted_group.id in self.env.user.groups_id.ids:
    #         internal_supplier = self.env['res.partner'].search([('name', '=', 'Proveedor Interno')], limit=1)
    #         if not internal_supplier:
    #             raise exceptions.UserError("El proveedor 'Proveedor Interno' no está configurado. Por favor, contacte al administrador.")

    #         if vals.get('partner_id') != internal_supplier.id:
    #             raise exceptions.UserError("Solo puedes seleccionar el 'Proveedor Interno'.")

    #     return super(PurchaseOrder, self).create(vals)

    @api.constrains('partner_id')
    def _check_restricted_supplier(self):
        """ Validar que los usuarios restringidos solo usen el proveedor "Proveedor Interno" """
        restricted_group = self.env.ref('purchase_restrictions.group_restricted_user', raise_if_not_found=False)
        if restricted_group and restricted_group.id in self.env.user.groups_id.ids:
            internal_supplier = self.env['res.partner'].search([('name', '=', 'Proveedor Interno')], limit=1)
            if not internal_supplier:
                raise exceptions.UserError("El proveedor 'Proveedor Interno' no está configurado. Por favor, contacte al administrador.")

            if self.partner_id != internal_supplier:
                raise exceptions.UserError("Solo puedes seleccionar el 'Proveedor Interno'.")