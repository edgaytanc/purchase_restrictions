# Restricciones en Compras para Odoo 17

Este módulo implementa restricciones personalizadas para usuarios en el módulo de compras de Odoo 17.

## Características

* **Restricción de Visibilidad de Precios:** Los usuarios pertenecientes al grupo "Usuario Restringido" no pueden ver los precios de los productos ni los totales en las órdenes de compra.
* **Proveedor Único:** Los usuarios del grupo "Usuario Restringido" solo pueden usar un proveedor fijo: "Proveedor Interno". Este proveedor se asigna automáticamente al crear una orden de compra.

## Configuración

1. **Instalar el Módulo:** Copia el directorio del módulo (`purchase_restrictions`) en tu directorio de addons de Odoo.
2. **Actualizar la Lista de Módulos:** En Odoo, ve a *Aplicaciones* y haz clic en *Actualizar*.
3. **Instalar el Módulo:** Busca "Restricciones en Compras" en la lista de aplicaciones y haz clic en *Instalar*.
4. **Configurar Grupos de Usuarios:**
    * Crea un nuevo grupo de usuarios llamado "Usuario Restringido".
    * Asigna los usuarios que deseas restringir a este grupo.
5. **Configurar el Proveedor Interno:**
    * Asegúrate de que existe un contacto de proveedor llamado "Proveedor Interno". Puedes crearlo si no existe.

## Notas

* Este módulo ha sido probado en Odoo 17.
* El proveedor "Proveedor Interno" debe existir en el sistema para que el módulo funcione correctamente.
* Puedes personalizar aún más las restricciones modificando el código del módulo.

## Autor

David Gaytan

## Licencia

[Especifica la licencia aquí, por ejemplo, AGPL-3]