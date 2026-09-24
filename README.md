# Alfabetización en IA generativa como recurso docente transversal

Materiales abiertos del proyecto de innovación docente **nº 3165**, *Alfabetización en IA
generativa como recurso docente transversal: efecto en la evaluación de una red
multidisciplinar de asignaturas*, desarrollado durante el curso 2026/2027 en la
Universidad de Sevilla.

Este repositorio publica el marco común, los materiales de alfabetización y los
instrumentos de valoración que genera la red, para que cualquier docente pueda
reutilizarlos y adaptarlos a su asignatura.

**Sitio web:** <https://jorgebigs.github.io/innovacion-US-3165/>

## Punto de partida

El alumnado universitario ya emplea la IA generativa, esté o no regulada en cada
asignatura. El proyecto asume esa realidad y, en lugar de restringir su uso, alfabetiza
al estudiantado para que la emplee de forma competente y crítica.

## El marco común

La red trabaja sobre cuatro dimensiones, tomadas de Ng et al. (2021) y alineadas con los
marcos de competencias en IA de la UNESCO y de la OCDE/Unión Europea:

1. **Conocer y entender**
2. **Usar y aplicar**
3. **Evaluar y crear**
4. **Cuestiones éticas**

Todas las asignaturas comparten el marco y los instrumentos de medición. Cada una
calibra el peso relativo de las cuatro dimensiones según el perfil de uso y de riesgo de
la IA propio de su disciplina: en programación pesa más el uso aplicado; en contextos
jurídicos, la evaluación crítica de las salidas del sistema.

## La red

Diez asignaturas de cuatro ramas de conocimiento:

| Rama | Centro | Asignaturas |
| --- | --- | --- |
| Informática | ETSII | Fundamentos de Programación · Sistemas Operativos · Proceso Software y Gestión I · Evolución y Gestión de la Configuración · Procesadores de Lenguajes |
| Economía y Empresa | CECYE · Facultad de Turismo y Finanzas | Aplicaciones de la Minería de Datos a la Investigación de Mercados · Contabilidad para Directivos de Empresas |
| Derecho | Facultad de Ciencias Económicas y Empresariales | Instituciones Básicas de Derecho Privado |
| Ciencias de la Salud | Facultad de Medicina · Facultad de Odontología | Anatomía Patológica (Grado en Medicina y Grado en Odontología) |

## Contenido del repositorio

| Carpeta | Contenido |
| --- | --- |
| [`cursos/`](cursos/) | Una carpeta por asignatura. Son solo cabeceras: el curso se genera a partir de los datos y de las lecciones comunes. |
| [`_data/asignaturas.yml`](_data/asignaturas.yml) | **El contenido propio de cada asignatura**: contexto, tareas, ejemplos de peticiones, fuentes de verdad, riesgos y casos. |
| [`_includes/lecciones/`](_includes/lecciones/) | Las cuatro lecciones del alumnado, comunes a toda la red, con los huecos que rellena cada asignatura. |
| [`docencia/`](docencia/) | [Guía del profesorado](docencia/README.md): qué se hace en clase con cada lección y [cómo añadir una asignatura](docencia/anadir-asignatura.md). |
| [`marco/`](marco/) | El [marco común](marco/marco-comun.md) con los descriptores observables, y las fichas de calibración. |
| [`instrumentos/`](instrumentos/) | [Rúbrica](instrumentos/rubrica-calidad-uso-ia.md), [cuestionario](instrumentos/cuestionario-autopercepcion.md) y [protocolo con consentimiento](instrumentos/protocolo-aplicacion.md). |
| [`analisis/`](analisis/) | Plantillas de entrega agregada. Sin datos. |

### Las cuatro lecciones

Comunes a todas las asignaturas; los ejemplos, las fuentes y las reglas, no.

| Lección | Dimensión | Guía de aula |
| --- | --- | --- |
| 1. Qué es esto que estás usando | Conocer y entender | [El fallo provocado](docencia/01-el-fallo-provocado.md) |
| 2. Preguntar para aprender | Usar y aplicar | [Reescribir peticiones](docencia/02-reescribir-peticiones.md) |
| 3. Comprobar antes de entregar | Evaluar y crear | [La respuesta envenenada](docencia/03-la-respuesta-envenenada.md) |
| 4. Tu responsabilidad | Cuestiones éticas | [La línea](docencia/04-la-linea.md) |

## Cómo llevarlo a tu asignatura

1. Lee el [marco común](marco/marco-comun.md) y la [guía del profesorado](docencia/README.md).
2. Rellena una [ficha de calibración](marco/PLANTILLA-ficha-calibracion.md): el peso de
   cada dimensión según el perfil de uso y de riesgo de tu materia.
3. Completa tus datos en [`_data/asignaturas.yml`](_data/asignaturas.yml) y ejecuta
   `python3 bin/generar-cursos.py`. Los pasos, en
   [cómo añadir tu asignatura](docencia/anadir-asignatura.md).
4. Si quieres medir el efecto, aplica los [instrumentos](instrumentos/) siguiendo el
   [protocolo](instrumentos/protocolo-aplicacion.md), antes y después.

## Protección de datos

Este repositorio no contiene ni contendrá datos del alumnado. Los cuestionarios se
administran con consentimiento informado y los resultados se tratan y se difunden
siempre de forma agregada.

## Origen y autoría

Todo el contenido de este repositorio es **obra original de la red del proyecto**,
elaborada a partir de los marcos públicos de alfabetización en IA que se citan en el
[marco común](marco/marco-comun.md). No reproduce ni adapta materiales docentes de
terceros. Las adaptaciones por asignatura indican su autoría propia.

## Licencia

Los materiales docentes se publican bajo [CC BY-SA 4.0](LICENSE) y el código de análisis
bajo [licencia MIT](LICENSE-CODE). Los instrumentos de terceros que la red traduce o
adapta conservan la licencia y la atribución de sus autores originales, indicadas en
[`instrumentos/`](instrumentos/).

## Cómo citar

Consulta [`CITATION.cff`](CITATION.cff).

## Reconocimiento

Proyecto financiado por el IV Plan Propio de Docencia de la Universidad de Sevilla,
actuación de Apoyo a la Innovación Docente (Ref. 221), Modalidad B, Redes de
Colaboración para la Innovación Docente, convocatoria 2026/2027, proyecto nº 3165.

## Referencias del marco

- Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence*, 2, 100041. <https://doi.org/10.1016/j.caeai.2021.100041>
- UNESCO (2025). *Marco de competencias para estudiantes en materia de IA*. <https://doi.org/10.54675/EKCU4552>
- UNESCO (2023). *Guidance for generative AI in education and research*. <https://doi.org/10.54675/EWZM9535>
- OECD / European Union (2026). *Empowering learners for the age of AI: An AI literacy framework for primary and secondary education*. <https://doi.org/10.1787/65cd27d4-en>
- Ng, D. T. K., Wu, W., Leung, J. K. L., Chiu, T. K. F., & Chu, S. K. W. (2024). Design and validation of the AI literacy questionnaire. *British Journal of Educational Technology*, 55, 1082–1104. <https://doi.org/10.1111/bjet.13411>
