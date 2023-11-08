---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/sysadmin/audit.md"
revision_date: "2021-06-14"
---

# Auditoría { #audit }

## Introducción { #introduction }

DHIS2 soporta un nuevo servicio de auditoría que está basado en Apache ActiveMQ Artemis. Artemis se utiliza como un sistema de mensajería asíncrona por DHIS2.

Después de guardar una entidad en la base de datos, se enviará un mensaje de auditoría al servicio consumidor de mensajes de Artemis. El mensaje entonces será procesado en un subproceso diferente.

Los registros de auditoría pueden recuperarse de la base de datos de DHIS2. Actualmente no hay UI o API endpoint disponible para recuperar las entradas de auditoría.

## Tabla de auditoría única { #audit_table }

Todas las entradas de auditoría se guardarán en una sola tabla llamada `auditoría`

| Columna | Tipo |  |  |
| --- | --- | --- | --- |
| auditid | entero |  |  |
| auditType | texto | LEER, CREAR, ACTUALIZAR, ELIMINAR, BUSCAR |  |
| auditscope | texto | METADATOS, AGREGADOS, TRACKER |  |
| klass | texto | Nombre de la clase Java de la entidad auditoría |  |
| attributes | jsonb | La cadena Json almacena atributos de la entidad de auditoría, utilizados para búsqueda. Ejemplo: {"valueType":"TEXT", "categoryCombo":"SWQW313FQY", "domainType":"TRACKER"} |  |
| data | bytea | Cadena Json comprimida de la Entidad de Auditoría. Actualmente está en formato de matriz de bytes y no es legible por humanos. |  |
| createdat | marca de tiempo sin zona horaria |  |  |
| createdby | texto |  |  |
| uid | texto |  |  |
| code | texto |  |  |
|  |  |

El nuevo servicio de Auditoría hace uso de dos nuevos conceptos: Ámbitos de Auditoría y Tipo de Auditoría.

## Ámbito de auditoría { #audit_scope }

Un ámbito de auditoría es un área lógica de la aplicación que puede ser auditada. Actualmente existen tres ámbitos de auditoría:

```
Tracker

Metadatos

Agregados
```

-   Para el ámbito de auditoría Tracker, los objetos auditados son: Instancia de entidad Tracker, Valor de atributo de entidad Tracker, Inscripción, Evento

-   Para el ámbito de metadatos, todos los objetos "metadatos" son auditados.

-   Para el Ámbito Agregado, los objetos de Valor de Datos Agregados son auditados.

## Tipo de auditoría { #audit_type }

Un tipo de auditoría es una acción que desencadena una operación de auditoría. Actualmente admitimos los siguientes tipos:

```
LEER

CREAR

ACTUALIZAR

ELIMINAR
```

Como ejemplo, cuando se crea una nueva instancia de entidad Tracker, y si se configura como tal, la acción CREAR es utilizada para insertar una nueva entrada de Auditoría en la tabla de la base de datos de auditoría.

`Nota: El tipo de auditoría READ generará una gran cantidad de datos en la base de datos y puede tener un impacto en el rendimiento.`

## Configurar { #audit_configuration }

El sistema de auditoría se configura automáticamente para auditar los siguientes ámbitos y tipos:

-   CREAR, ACTUALIZAR, ELIMINAR

-   METADATOS, TRACKER, AGREGADO

**No se requiere ninguna acción para activar la auditoría.** La auditoría todavía puede ser configurada usando la "matriz de auditoría". La matriz de auditoría está dirigida por 3 propiedades en dhis.conf:

```
audit.metadata

audit.tracker

audit.aggregate
```

Cada propiedad acepta una lista delimitada por punto y coma de tipos de auditoría válidos:

```
CREATE

UPDATE

DELETE

READ
```

Por ejemplo, para auditar solo la creación y eliminación de objetos relacionados con Tracker, se debe agregar la siguiente propiedad a `dhis.conf`:

```
audit.tracker = CREATE;DELETE
```

Para deshabilitar completamente la auditoría, esta es la configuración a usar:

```
audit.metadata = DISABLED

audit.tracker = DISABLED

audit.aggregate = DISABLED
```
