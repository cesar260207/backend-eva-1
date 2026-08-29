# Evidencias de uso de Inteligencia Artificial

## Prompt 1
**Pregunta:** "Necesito un proyecto Django con dos aplicaciones independientes, una para delegaciones y otra para gestión, usando Bootstrap local y JSON para alimentar las pantallas. Diseña la estructura y la lógica para leer solicitudes y metas desde archivos JSON."

**Respuesta de apoyo:** El asistente propuso una arquitectura con:
- proyecto principal `gestion_laserena`
- apps `delegaciones_app` y `gestion_app`
- archivo `base.html` con navbar y pie de página
- lectura de JSON desde una carpeta `data/`
- funciones de procesamiento para estados y semáforos
- plantillas heredadas de Bootstrap

**Implementación realizada:** Se aplicó esa estructura en el proyecto, con vistas, rutas y plantillas compartidas para la administración territorial.

## Prompt 2
**Pregunta:** "Quiero que las solicitudes muestren estado según una regla de vencimiento: si la fecha compromiso pasó y sigue pendiente, debe marcarse como Alerta Roja. Además, necesito un semáforo en el dashboard por delegación con porcentajes y días transcurridos."

**Respuesta de apoyo:** Se recomendó calcular la diferencia entre la fecha actual y la fecha de compromiso, y clasificar los porcentajes en `Verde`, `Amarillo` y `Rojo` según umbrales del 80%, 65% y menores valores.

**Implementación realizada:** El cálculo se incorporó a las vistas de `delegaciones_app` y `gestion_app` usando Python, estructuras condicionales e iteraciones sobre los JSON.

## Implementación final
La IA apoyó principalmente en:
- diseño de cards y tablas con Bootstrap
- lógica de carga y procesamiento de JSON
- estructura de navegación y plantillas reutilizables
- organización del contenido territorial y de métricas municipales

Este documento forma parte de la evidencia del uso de IA como apoyo al desarrollo del proyecto.
