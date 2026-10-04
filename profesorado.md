---
title: "Área del profesorado"
permalink: /profesorado/
seccion: profesorado
portada_seccion: true
---

# Área del profesorado

Todo lo que no ve el alumnado: cómo se lleva cada lección a clase, cómo adaptar el curso a
tu asignatura, con qué se mide y cómo se analiza.

> El contenido de estudio está en los [cursos del alumnado](/). Si solo quieres ver qué
> leen tus estudiantes, entra por ahí.

## Empieza aquí

| | |
| --- | --- |
| **¿Nunca has visto esto?** | Lee el [marco común](marco/marco-comun.md); diez minutos y entiendes el resto |
| **¿Vas a calibrar tu asignatura?** | Descarga la [ficha en Word]({{ '/descargas/ficha-calibracion.docx' | relative_url }}) y rellénala |
| **¿Vas a pasar el cuestionario?** | Descarga el [cuestionario en Word]({{ '/descargas/cuestionario-autopercepcion.docx' | relative_url }}), ya sin la parte metodológica |
| **¿Vas a darlo en clase?** | [Guía del profesorado](docencia/README.md), una página por lección |
| **¿Quieres adaptar tu curso?** | [Cómo añadir tu asignatura](docencia/anadir-asignatura.md) |
| **¿Vas a medir?** | [Instrumentos](instrumentos/README.md) y su [protocolo](instrumentos/protocolo-aplicacion.md) |

## El marco

- [Marco común de alfabetización en IA](marco/marco-comun.md) — las cuatro dimensiones
  con sus descriptores observables (D1.1 a D4.5), los perfiles de riesgo por rama y las
  reglas de calibración.
- [Ficha de calibración](marco/PLANTILLA-ficha-calibracion.md) — el reparto de 100
  puntos entre dimensiones en tu asignatura, y las tareas reales en que tu alumnado usa la
  IA. Descargable **[en Word]({{ '/descargas/ficha-calibracion.docx' | relative_url }})**.

## En el aula

La secuencia completa es: **medida inicial → material → medida final**. El cuestionario y
el test van antes de que el alumnado vea ninguna lección; si llega con el material visto,
la medida de partida se pierde.

Cada lección que lee el alumnado tiene su sesión presencial. Unas tres horas en total,
repartidas por el cuatrimestre y dentro del horario de clase.

| Lección del alumnado | Guía de aula | En clase |
| --- | --- | --- |
| Qué es esto que estás usando | [El fallo provocado](docencia/01-el-fallo-provocado.md) | 30–40 min |
| Preguntar para aprender | [Reescribir peticiones](docencia/02-reescribir-peticiones.md) | 50–60 min |
| Comprobar antes de entregar | [La respuesta envenenada](docencia/03-la-respuesta-envenenada.md) | 45 min |
| Tu responsabilidad | [La línea](docencia/04-la-linea.md) | 40 min |

## Los cursos de la red

Los diez están publicados. Los que su docente aún no ha revisado usan los ejemplos comunes
de su rama y lo advierten en la página.

<div class="tabla-envoltorio">
<table>
  <thead><tr><th>Asignatura</th><th>Rama</th><th>Centro</th><th>Docente</th><th>Estado</th></tr></thead>
  <tbody>
  {% for o in site.data.asignaturas %}
    <tr>
      <td><a href="{{ '/cursos/' | append: o.slug | append: '/' | relative_url }}">{{ o.nombre }}</a></td>
      <td>{{ o.rama }}</td><td>{{ o.centro }}</td><td>{{ o.docente }}</td>
      <td>{% if o.estado == 'completo' %}Revisado{% elsif o.estado == 'borrador' %}Ejemplos de la rama{% else %}En preparación{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

Para adaptarlo no escribes páginas: rellenas los datos de tu asignatura y el sitio genera
el curso. Lo explica [cómo añadir tu asignatura](docencia/anadir-asignatura.md).

## Medir

Tres vías independientes, todas agregadas y anónimas.

| Vía | Instrumento | A quién | Cuándo |
| --- | --- | --- | --- |
| Competencia percibida y actitudes | [Cuestionario de autopercepción](instrumentos/cuestionario-autopercepcion.md) ([Word]({{ '/descargas/cuestionario-autopercepcion.docx' | relative_url }})) | Grupos intervenidos | Antes y después |
| Calidad del uso de la IA | [Tu propia rúbrica](instrumentos/rubrica-calidad-uso-ia.md), con cada ítem asignado a una dimensión y su peso declarado | Todos los grupos que tuteles, intervenidos y de control | Después de la medida final |
| Calificaciones | [Distribuciones agregadas](analisis/README.md) | Intervenidos y de control | Al cerrar actas |

Antes de aplicar nada, lee el [protocolo](instrumentos/protocolo-aplicacion.md): código
de emparejamiento anónimo, consentimiento informado y condiciones de aplicación.

**Sin datos del alumnado en el repositorio**, nunca. Solo distribuciones agregadas.

## Recursos externos

La página [Para saber más](recursos.md) reúne los recursos de profundización que ve el
alumnado. Dos reglas al añadir uno nuevo a
[`_data/recursos.yml`](https://github.com/jorgeBIGS/innovacion-US-3165/blob/main/_data/recursos.yml):

- **Se enlaza, no se reproduce.** No alojamos material de terceros. Anota su autoría y su
  licencia si la declara.
- **Siempre opcional.** La convocatoria excluye las actividades fuera del horario de clase,
  así que nada externo puede ser exigible ni evaluable. Si obliga a crear cuenta en una
  plataforma, con más motivo: ofrece alternativa.

Los vídeos que acompañan a cada lección se definen en
[`_data/videos.yml`](https://github.com/jorgeBIGS/innovacion-US-3165/blob/main/_data/videos.yml)
y se incrustan sin cookies.

## Sobre el proyecto

Proyecto de innovación docente **nº 3165** del IV Plan Propio de Docencia de la Universidad
de Sevilla, Acción 221, Modalidad B, Redes de Colaboración, curso 2026/2027. Una red de
diez asignaturas de cuatro ramas que comparte marco e instrumentos y calibra el peso de
cada dimensión según su disciplina.

Los materiales están bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
y son obra original de la red. Para citarlos,
[CITATION.cff](https://github.com/jorgeBIGS/innovacion-US-3165/blob/main/CITATION.cff).
Los recursos externos se enlazan, no se reproducen.
