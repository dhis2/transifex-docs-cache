---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/developer/web-api/organisation-unit-profile.md"
revision_date: '2021-06-29'
---

# Perfil de la unidad organizativa { #org_unit_profile }

El recurso  perfil de la unidad organizativa permite definir y recuperar un perfil de información para las unidades organizativas en DHIS 2.

```
/api/organisationUnitProfile
```

Se puede crear un único perfil de unidad organizativa y se aplicará a todas las unidades organizativas.

La parte de información del perfil de la unidad organizativa incluye:

- Nombre, nombre corto, descripción, fecha de apertura, fecha de cierre, URL.
- Persona de contacto, dirección, correo electrónico, número de teléfono (si existe).
- Ubicación (longitud/latitud).
- Atributos de metadatos (configurables).
- Sets de grupos de unidad organizativa y grupos (configurables).
- Datos agregados para elementos de datos, indicadores, tasas de informes, indicadores de programa (configurables).

## Crear perfil de la unidad organizativa { #create-organisation-unit-profile } 

Para definir el perfil de la unidad organizativa, puede utilizar una petición `POST`:

```
POST /api/organisationUnitProfile
```

La carga útil se ve así, donde `attributes` se refiere a atributos de metadatos, `groupSets` se refiere a sets de grupos de unidad organizativa y `dataItems` se refiere a elementos de datos, indicadores, sets de datos e indicadores de programas:

```json
{
    "attributes": [
        "xqWyz9jNCA5",
        "n2xYlNbsfko"
    ],
    "groupSets": [
        "Bpx0589u8y0",
        "J5jldMd8OHv"
    ],
    "dataItems": [
        "WUg3MYWQ7pt",
        "vg6pdjObxsm",
        "DTVRnCGamkV",
        "Uvn6LCg7dVU",
        "eTDtyyaSA7f"        
    ]
}
```

La autoridad `F_ORG_UNIT_PROFILE_ADD` es requerida para definir el perfil.

## Obtener perfil de la unidad organizativa { #get-organisation-unit-profile } 

Para recuperar la definición del perfil de la unidad organizativa, puede utilizar una petición `GET`:

```
GET /api/organisationUnitProfile
```

## Obtener datos de perfil de la unidad organizativa { #get-organisation-unit-profile-data } 

Para recuperar los datos del perfil puede utilizar una petición `POST`:

```
GET /api/organisationUnitProfile/{org-unit-id}/data?period={iso-period}
```

El endpoint de los datos del perfil de la unidad organizativa combinará la definición del perfil con los valores de información/datos asociados.

* La variable de ruta `{org-unit-id}` es obligatoria y hace referencia al ID de la unidad organizativa para la que se proporcionan datos agregados.
* El parámetro de consulta `iso-period` es opcional y hace referencia al ID de periodo ISO para que el periodo proporcione datos agregados para los elementos de datos. Si no se especifica ninguno, el período relativo _este año_ se utilizará como alternativa.

La respuesta incluirá las siguientes secciones:

* `info`: Información fija sobre la unidad organizativa.
* `attributes`: Atributos de metadatos con los valores de atributos correspondientes.
* `groupSets`: Sets de grupos de unidad organizativa con el correspondiente grupo de unidades organizativas del que es miembro la unidad organizativa.
* `dataItems`: Elementos de datos con el correspondiente valor de datos agregados.

Tenga en cuenta que se realizan comprobaciones de control de acceso y se omitirán los elementos de metadatos que no son accesibles para el usuario actual.

Una ejemplo de petición se ve así:

```
GET /api/organisationUnitProfile/DiszpKrYNg8/data?period=2021
```

La carga útil de la respuesta de datos del perfil se verá así, donde los campos `id` y `label` se refieren al elemento de metadatos, y el campo `value` se refiere al valor asociado:

```json
{
    "info": {
        "id": "DiszpKrYNg8",
        "code": "OU_559",
        "name": "Ngelehun CHC",
        "shortName": "Ngelehun CHC",
        "openingDate": "1970-01-01T00:00:00.000",
        "longitude": -11.4197,
        "latitude": 8.1039
    },
    "attributes": [
        {
            "id": "n2xYlNbsfko",
            "label": "NGO ID",
            "value": "GHE51"
        },
        {
            "id": "xqWyz9jNCA5",
            "label": "TZ code",
            "value": "NGE54"
        }
    ],
    "groupSets": [
        {
            "id": "Bpx0589u8y0",
            "label": "Facility Ownership",
            "value": "Public facilities"
        },
        {
            "id": "J5jldMd8OHv",
            "label": "Facility Type",
            "value": "CHC"
        }
    ],
    "dataItems": [
        {
            "id": "WUg3MYWQ7pt",
            "label": "Total Population",
            "value": 3503.0
        },
        {
            "id": "DTVRnCGamkV",
            "label": "Total population < 1 year",
            "value": 140.0
        },
        {
            "id": "vg6pdjObxsm",
            "label": "Population of women of child bearing age (WRA)",
            "value": 716.0
        },
        {
            "id": "Uvn6LCg7dVU",
            "label": "ANC 1 Coverage",
            "value": 368.2
        },
        {
            "id": "eTDtyyaSA7f",
            "label": "FIC <1y",
            "value": 291.4
        }
    ]
}
```

