---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/edit/master/chapters/introduction.md" 
---
# Introducción

Tracker es la aplicación dentro de la plataforma de DHIS2 que permite la captura y el uso de datos longitudinales individuales. La funcionalidad de Tracker cubre una amplia gama de necesidades, desde el monitoreo de la calidad y disponibilidad de los pozos de agua hasta la recopilación de la asistencia de los estudiantes en un aula o la captura de datos de pacientes en una historia clínica. A los fines de esta guía, muchos de los ejemplos provendrán de los sistemas sanitarios, aunque Tracker también se utiliza ampliamente para sistemas educativos, sistemas ambientales y logística, entre otros ámbitos.

Con la intención de acercar los sistemas de información al nivel donde se generan los datos primarios, muchos países y programas están aprovechando una mayor disponibilidad de red y la presencia generalizada de dispositivos móviles y otros equipos. Los datos a nivel individual agregan granularidad y matices a los sistemas de información, lo que proporciona oportunidades para hacer análisis con fines específicos, cambiar los indicadores con el tiempo y mejorar la calidad de los datos. Más allá de su utilidad para la generación de informes y el análisis, los datos a nivel individual también se pueden utilizar para eliminar las redundancias en la generación de informes, capacitar al personal de nivel inferior con mejores herramientas para la toma de decisiones y colocar al cliente en el centro del sistema de información. En resumen, los datos a nivel individual representan la unidad de datos más pequeña y, como tal, pueden reutilizarse de muchas maneras para satisfacer las diversas necesidades que entran en competencia en los sistemas de información nacionales.

El fin de esta guía es ayudar a determinar si Tracker es la solución adecuada para un caso de uso potencial, así como proporcionar orientación práctica para ayudar a planificar implementaciones exitosas. El uso de Tracker a gran escala introduce factores adicionales que deberían planificarse más allá de lo que ya pueda haber para una instancia agregada de DHIS2 existente. Las oportunidades y los beneficios potenciales de los sistemas de información aumentan a medida que un sistema hace el trayecto de datos agregados → datos anónimos rastreados → datos de personas identificables → datos del paciente en tiempo real en el lugar de asistencia. Aquellas personas que planifiquen una implementación de Tracker deben reconocer que los desafíos aumentan junto con los beneficios.

Esta guía de implementación incluye recomendaciones para proporcionarle ayuda a la hora de:

-  determinar si Tracker satisfacerá sus necesidades;
-  evaluar la preparación de su entorno para introducir la recopilación de datos a nivel individual;
-  comprender de qué manera se diferencia la implementación de Tracker de la agregación de DHIS2;
-  reconocer las preocupaciones específicas de los sistemas de datos a nivel individual, incluida la privacidad y la seguridad;
-  revisar las lecciones aprendidas y las prácticas recomendables derivadas de casos de uso del mundo real;
-  planificar la introducción de su(s) programa(s) de Tracker con la escala deseada; y
-  establecer la infraestructura que mantendrá un programa de Tracker a largo plazo.

La guía se divide en dos secciones básicas:

- La sección **¿Está preparado mi proyecto para implementar Tracker?** describe cinco importantes factores contextuales que es necesario comprender para preparar su entorno antes de continuar con la planificación de una implementación de Tracker:

    - Asistencia y compromiso institucional
    - Financiamiento;
    - Legislación y políticas;
    - Capacidad y competencia; e
    - Infrastructura.

- La sección **Creación de su(s) programa(s) de Tracker** proporciona orientación y recomendaciones específicas para nueve aspectos diferentes de una implementación de Tracker:

    - Determinación de escala;
    - Proceso de configuración y diseño;
    - Determinación de marco de trabajo de monitoreo y evaluación;
    - Entrada de datos en tiempo real vs. entrada de datos secundaria;
    - Versión móvil vs. versión web;
    - Creación de una infraestructura de RR. HH. de asistencia;
    - Alojamiento;
    - Capacitación e implementación; y
    - Relación de Tracker con su sistema de agregación.

Se proporcionan enlaces de herramientas de planificación específicas en todo el documento y en el apéndice.

## ¿Para qué puede utilizarse Tracker?

Al igual que con el resto de la plataforma de DHIS2, Tracker tiene un modelo de datos genérico cuya configuración puede establecer el usuario para muchos fines diferentes. En su forma más básica, Tracker permite al usuario definir un tipo particular de cosas (persona, producto, muestra de laboratorio, área de captación, etcétera) que desea seguir a lo largo del tiempo (una entidad rastreada), definir los datos que desea recopilar acerca de dicha entidad (elementos de datos), colocar los elementos de datos en un orden específico y con las condiciones o lógica que los acompañan (programa, reglas de programa), y determinar los análisis que se deben producir (indicadores de programa, informes de eventos, visualizaciones de datos, etcétera).

Un ejemplo de un programa de Tracker simple podría ser un programa para recopilar información sobre casos de malaria en el lugar de asistencia. La entidad rastreada sería una persona, definida por atributos como nombre, apellido, fecha de nacimiento o pueblo. El programa contendría elementos de datos como síntomas, prueba utilizada y resultado, tratamiento proporcionado, etcétera. Estos elementos de datos pueden tener opciones preconfiguradas para posibles respuestas, como posibles pruebas disponibles, o una lógica que ayude a asegurar la calidad de los datos, como posibles valores mínimos y máximos para un elemento de datos determinado. Los datos recopilados serían visibles para el usuario médico como parte de la historia clínica compartida del paciente con malaria, pero también podrían utilizarse para generar informes mensuales requeridos por el programa nacional de control de la malaria, para proporcionar asistencia al médico en la toma de decisiones, para generar recordatorios destinados al paciente vía mensaje de texto con el fin de promover la adherencia al tratamiento o para completar un panel orientado al consultorio que contenga indicadores clave de rendimiento. Para todos estos fines, los datos se recopilaron solo una vez —durante la visita del paciente— pero se reutilizaron muchas veces para cubrir diferentes necesidades.

Mediante las aplicaciones Event y Capture, DHIS2 admite además la recopilación de datos individuales sin rastreo longitudinal. A lo largo de esta documentación también se hará referencia al rastreo no longitudinal, el cual sigue prácticamente el mismo modelo de datos que tracker, con la excepción de la definición de una entidad rastreada, que no es una parte requerida del rastreo no longitudinal. Un ejemplo de dicho programa de eventos podría ser la generación de informes de los mismos datos de malaria obtenidos de personas al igual que en el programa anterior (de entidad rastreada), pero sin vincular estos datos a un paciente específico. Como tales, los datos no se convertirían en parte de una historia clínica compartida (o tal vez no se utilizarían para generar recordatorios destinados al paciente vía mensaje de texto u otras funciones que dependen del rastreo de una entidad a lo largo del tiempo), pero los otros usos de los datos aún podrían aprovecharse.

Como puede observarse en los ejemplos anteriores, Tracker y la recopilación de datos individuales son bastante diferentes de los informes agregados tradicionales para los Sistemas de Información de Gestión de la Salud (HMIS, por sus siglas en inglés). Solo uno de los usos potenciales descritos anteriormente se satisface mediante la recopilación de datos agregados —el de los informes mensuales—, mientras que los usos orientados a pacientes, médicos y centros de salud son posibles mediante la recopilación de datos individuales.

Incluso con respecto a los informes de rutina, la recopilación de datos individuales presenta oportunidades para mejorar tanto la interpretación como el análisis de los datos y —más importante aún— para tomar las medidas correspondientes. Por ejemplo, un informe agregado podría mostrar que la cobertura general de inmunización es del 80 %, pero carece de detalles en cuanto a si el 20 % restante refleja errores en los informes, la exclusión no intencional de ciertos individuos (en función de la geografía o grupos) u otros factores. Los números agregados tampoco permiten la identificación específica de niños no vacunados a los que se podría hacer seguimiento mediante un programa de divulgación dirigido. Los números agregados de este ejemplo abordan la necesidad básica de los ministerios de salud de informar el progreso nacional en relación con un indicador global, pero no las necesidades de los gerentes o proveedores de programas de inmunización de tomar medidas específicas para mejorar la cobertura.

Un beneficio inherente de usar Tracker como su sistema a nivel individual es su alineación con el sistema agregado de DHIS2 existente, que ya se utiliza en la mayoría de los países de ingresos bajos y medios para sus HMIS. A diferencia de una historia clínica electrónica (EMR, por sus siglas en inglés) independiente u otra aplicación, Tracker fomenta la recopilación de datos estructurados que pueden agregarse en sentido ascendente e integrarse al HMIS nacional de forma nativa, reemplazando así la entrada y agregación de datos secundarios con datos de fuentes primarias.

Como componente central de la plataforma de DHIS2, Tracker se actualiza dos veces al año junto con el resto del software de DHIS2. Los aportes más significativos para las mejoras de Tracker provienen de implementaciones en países reales y están en sintonía con las recomendaciones mundiales, especialmente con las [Directrices de la OMS sobre intervenciones digitales para el fortalecimiento del sistema sanitario](https://www.who.int/reproductivehealth/publications/digital-interventions-health-system-strengthening/en/). De las diez intervenciones recomendadas, Tracker tiene una funcionalidad específica para admitir las siguientes:

- Notificación de nacimiento;
- Notificación de muerte;
- Notificación de activos y gestión de productos;
- Comunicación dirigida al cliente;
- Asistencia al trabajador sanitario en la toma de decisiones;
- Rastreo digital de los servicios y estado de salud del cliente combinado con la asistencia en la toma de decisiones;
- Rastreo digital combinado con asistencia en la toma de decisiones y comunicación dirigida al cliente; y
- Provisión digital de capacitación y contenido educativo para trabajadores sanitarios.

Aprovechar al máximo estas funciones requiere que los datos recopilados sean sistemáticos y uniformes. En la asistencia sanitaria, los servicios sanitarios públicos y primarios que están firmemente determinados ​​por directrices y flujos de trabajo estipulados son particularmente adecuados para los programas de Tracker. Por ejemplo, en la asistencia prenatal (ANC, por sus siglas en inglés), la mayoría de los países tienen directrices con algoritmos para la evaluación y la gestión de pacientes en respuesta a los resultados de las pruebas que se pueden incorporar en Tracker para seguir un flujo de trabajo clínico de rutina, lo que permite respaldar tanto al profesional sanitario como a las necesidades relacionadas con los informes. En áreas más complejas de la asistencia sanitaria, con algoritmos de toma de decisiones menos documentados y definidos (como, por ejemplo, en un hospital de referencia), Tracker puede ser más útil en la realización de una simple recopilación de datos, lo que permite, por un lado, que el médico determine la mejor manera de usar los datos para la clasificación de pacientes y, por el otro, que los elementos de datos estandarizados se utilicen para informes adicionales u otros fines.


## Ejemplos de casos de uso de Tracker

A lo largo de esta guía, haremos referencia a ejemplos de casos de uso para dar ejemplos del mundo real de principios de planificación, puntos de decisión, utilización de software y datos, obstáculos y problemas comunes, y lecciones aprendidas en diferentes etapas del proceso de planificación e implementación de Tracker. Aquí se proporciona un breve resumen introductorio de estos casos de uso individuales. Puede consultar más detalles para algunos de los casos de uso en www.dhis2.org.

### Paquetes de Tracker preconfigurados

En la sección [Kit de herramientas de la OMS sobre el análisis y el uso de datos de centros sanitarios](https://www.who.int/healthinfo/tools_data_analysis_routine_facility/en/), se han creado programas de Tracker preconfigurados para cubrir una serie de temas relacionados con la salud. Estos paquetes están destinados a ser el punto de partida de los programas en países, lo que permite una configuración adicional para adaptarlos al contexto local al mismo tiempo que se conservan los estándares globales para los indicadores y la práctica. Estos se pueden agregar a los sistemas de DHIS2 existentes, ya sea en conjunto o individualmente. Se puede acceder a estos paquetes desde el enlace de arriba o desde who.dhis2.org. Los paquetes preconfigurados actuales cubren los siguientes temas:

- Eventos adversos para la inmunización;
- Notificación de nacimiento, muerte fetal y muerte para el registro civil;
- Causa de muerte (incluidos los códigos ICD-10 de la lista de mortalidad inicial);
- Investigación del sitio de reproducción de la malaria;
- Investigación sobre la situación del hogar, el caso, el tratamiento y el diagnóstico de la malaria;
- Investigación sobre focos de la malaria;
- Campañas de inmunización masiva;
- Registro de inmunización de rutina; y
- Supervisión de casos de tuberculosis.

Se puede acceder a paquetes adicionales que aún están en desarrollo en https://who.dhis2.org/documentation/work_in_progress.html.

### Botsuana: programa de nutrición e inmunización

Botsuana ha creado un programa combinado de nutrición e inmunización que proporciona servicios clave a los niños pequeños que reciben asistencia nutricional, al mismo tiempo que se asegura de que los niños alcancen sus indicadores de crecimiento y reciban el conjunto de vacunas completo. Al trabajar con el equipo de Botsuana, la plataforma de Tracker se mejoró para producir puntuaciones z estandarizadas que proporcionan una evaluación rápida del peso para la estatura, del peso para la edad y de la altura para la edad.

### Ghana: Módulos de rastreador eletrónico de VIH/TAR y otros

Desde 2012, los Servicios de Salud de Ghana han liderado un programa pionero en informar datos a nivel del paciente a través de programas de Tracker de DHIS2 (en Ghana el proyecto se llama "eTrackers"). En 2019, comenzaron a usar 8 módulos de eTrackers diferentes. Un buen ejemplo es su eTracker de VIH/TAR, que, además de rastrear a pacientes individuales a través de pruebas y tratamientos, facilita que el personal sanitario identifique y haga un seguimiento de los pacientes incumplidores, al mismo tiempo que se respalda el flujo de informes para datos agregados sobre el VIH, que ha estado en curso en Ghana desde 2006.

### Palestina: Registro electrónico de salud materna e infantil

A cada mujer en Palestina se le asigna un consultorio de atención primaria de salud y, si ese consultorio no brinda los servicios que necesita, se le solicita que visite un consultorio de nivel superior. Este sistema de derivación requiere un registro electrónico que controle el acceso a los archivos clínicos del paciente, respalde la continuidad de la asistencia en diferentes sitios de asistencia sanitaria, permita la entrada de datos desde varios lugares diferentes y proporcione análisis para ayudar a tomar decisiones de conformidad con las directrices de asistencia prenatal de Palestina. Nuestra colaboración con Palestina inició en 2014. El desarrollo y la implementación del registro electrónico de salud materna e infantil (MCH, por sus siglas en inglés) incluyó un enfoque iterativo y un diálogo dinámico entre los desarrolladores, las personas responsables de formular políticas, los funcionarios de salud pública y los profesionales sanitarios. Esta implementación presenta un amplio uso de mensajes de texto automatizados para comunicarse con los pacientes, así como paneles de mejora de calidad para medir el desempeño de los consultorios y respaldar la prestación sanitaria.

### Zimbabue: Programa Nacional de Control de la Malaria

La implementación en Zimbabue de Tracker para Android de DHIS2 se inició en 2014 como un proyecto colaborativo entre el Programa Nacional de Control de la Malaria (NMCP, por sus siglas en inglés) y la Universidad de Oslo, y desde entonces se ha ampliado para cubrir casi la mitad de los más de 60 distritos del país. Además de presentar la recopilación de datos sin conexión, datos detallados de ubicación, y análisis y recopilación de datos casi en tiempo real, esta implementación es un ejemplo de trabajo con múltiples partes interesadas a nivel mundial para desarrollar un programa con potencial de expansión en regiones geográficas y áreas de enfermedades.



