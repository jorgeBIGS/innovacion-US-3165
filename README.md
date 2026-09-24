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
| [`marco/`](marco/) | El [marco común](marco/marco-comun.md), con los descriptores observables de cada dimensión, y las fichas de calibración de cada asignatura. |
| [`materiales/base/`](materiales/base/) | Las cuatro unidades del material transversal, unas tres horas de clase. |
| [`materiales/asignaturas/`](materiales/asignaturas/) | Adaptaciones de ese material a cada asignatura, con su autoría propia. |
| [`instrumentos/`](instrumentos/) | [Rúbrica de calidad de uso](instrumentos/rubrica-calidad-uso-ia.md), [cuestionario de autopercepción](instrumentos/cuestionario-autopercepcion.md) y [protocolo de aplicación y consentimiento](instrumentos/protocolo-aplicacion.md). |
| [`analisis/`](analisis/) | Plantillas de entrega agregada. Sin datos. |

### El material base, de un vistazo

| Unidad | Dimensión |
| --- | --- |
| [1. Cómo funciona la IA generativa, y por qué se equivoca](materiales/base/01-como-funciona-la-ia-generativa.md) | Conocer y entender |
| [2. Preguntar para aprender, no para terminar](materiales/base/02-preguntar-para-aprender.md) | Usar y aplicar |
| [3. Verificar lo que devuelve el sistema](materiales/base/03-verificar-las-salidas.md) | Evaluar y crear |
| [4. Integridad académica, responsabilidad y ética](materiales/base/04-integridad-y-etica.md) | Cuestiones éticas |

## Cómo reutilizar el material

1. Lee el [marco común](marco/marco-comun.md) y el [material base](materiales/base/).
2. Rellena una ficha de calibración para tu asignatura, a partir de
   [`marco/PLANTILLA-ficha-calibracion.md`](marco/PLANTILLA-ficha-calibracion.md): decide
   el peso de cada dimensión e identifica las tareas reales en las que tu alumnado
   recurre a la IA.
3. Adapta las actividades del material base a esas tareas, con la
   [plantilla de adaptación](materiales/asignaturas/PLANTILLA-adaptacion.md). Cada unidad
   necesita que lleves material propio de tu materia: la pregunta que falla, las peticiones
   pobres, la respuesta con errores y los casos ambiguos.
4. Si quieres medir el efecto, aplica los [instrumentos](instrumentos/) siguiendo el
   [protocolo](instrumentos/protocolo-aplicacion.md), antes y después de la intervención.

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
