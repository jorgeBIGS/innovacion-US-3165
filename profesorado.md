---
title: "Para el profesorado"
permalink: /profesorado/
seccion: profesorado
portada_seccion: true
---

# Para el profesorado

El alumnado se forma por su cuenta con el curso de su asignatura. **Tú no impartes nada**:
pasas un cuestionario antes, le das el enlace al curso, pasas el mismo cuestionario
después y envías los datos agregados.

Son unos **20 minutos de clase** en todo el cuatrimestre.

## Qué hacer, por orden

1. **Consentimiento y cuestionario inicial**, en clase, **antes de que el alumnado vea
   nada del curso**. Si llega con las lecciones leídas, la medida de partida ya no mide el
   punto de partida y la comparación se pierde.
2. **Entrega a cada estudiante su código** de emparejamiento y dile que lo conserve: es lo
   único que permite cruzar su respuesta inicial con la final sin identificarlo.
3. **Pasa el enlace de tu curso.** Está publicado y es voluntario; no se califica.
4. **Cuestionario final**, el mismo, cuando hayan terminado. Si lo montas en línea, su
   enlace aparece como la tarjeta «Autoevalúate» al final del curso.
5. **Envía los datos agregados por grupo.** Nunca respuestas individuales.

Si además evalúas a tu alumnado con una rúbrica propia, puedes aportar esa comparación
entre un grupo que haya hecho el curso y otro que no. La única condición para que sea
agregable: que cada ítem de tu rúbrica esté asignado a una de las cuatro dimensiones y
tenga un peso declarado.

## Los ficheros que necesitas

| | Para qué |
| --- | --- |
| **[Consentimiento informado]({{ '/descargas/consentimiento-informado.docx' | relative_url }})** | Se entrega y se firma antes del cuestionario inicial. Sustituye el nombre de tu asignatura |
| **[Cuestionario de autoevaluación]({{ '/descargas/cuestionario-autopercepcion.docx' | relative_url }})** | El mismo al principio y al final. 16 ítems de competencia percibida más contexto y uso declarado |
| **[Ficha de calibración]({{ '/descargas/ficha-calibracion.docx' | relative_url }})** | El peso de cada dimensión en tu materia y las tareas en que tu alumnado usa la IA |
| **[Plantilla de calificaciones]({{ '/descargas/plantilla-distribucion-calificaciones.docx' | relative_url }})** | Distribuciones agregadas, si comparas grupos |
| **[Plantilla de rúbrica]({{ '/descargas/plantilla-rubrica-agregada.docx' | relative_url }})** | Resultados de tu rúbrica por grupo, con sus ítems y pesos |

## Dos cosas que no pueden fallar

**El anonimato.** No se recogen nombres, matrículas ni correos junto a las respuestas. Si
montas el cuestionario en Microsoft Forms con la cuenta institucional, comprueba en los
ajustes que **no registra el nombre** y desactiva «una respuesta por persona»: ambas
identifican. Si guardas la lista que relaciona códigos con estudiantes, consérvala
separada de las respuestas y destrúyela al terminar la recogida.

**El código de emparejamiento.** El mismo al principio y al final, y pedido con las mismas
palabras. Sin él no hay comparación pre/post, y no tiene arreglo después.

## El marco, en cuatro dimensiones

Es lo que miden el cuestionario y, si la usas, tu rúbrica.

| Dimensión | Qué observa |
| --- | --- |
| **Conocer y entender** | Sabe explicar, a alto nivel, qué hace el sistema y por qué falla |
| **Usar y aplicar** | Pide ayuda a su proceso, con contexto, en vez del producto terminado |
| **Evaluar y crear** | Verifica, detecta invenciones y reelabora en lugar de entregar la salida en bruto |
| **Cuestiones éticas** | Declara su uso, responde de lo que entrega y protege los datos |

Cada asignatura decide cuánto pesa cada dimensión según su perfil de uso y de riesgo. Eso
es lo que recoge la ficha de calibración.

## Tu curso

Los diez cursos están publicados. Los que su docente aún no ha revisado usan los ejemplos
comunes de su rama de conocimiento y lo advierten en la página.

<div class="tabla-envoltorio">
<table>
  <thead><tr><th>Asignatura</th><th>Docente</th><th>Estado</th></tr></thead>
  <tbody>
  {% for o in site.data.asignaturas %}
    <tr>
      <td><a href="{{ '/cursos/' | append: o.slug | append: '/' | relative_url }}">{{ o.nombre }}</a></td>
      <td>{{ o.docente }}</td>
      <td>{% if o.estado == 'completo' %}Revisado{% elsif o.estado == 'borrador' %}Ejemplos de la rama{% else %}En preparación{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

**Para que los ejemplos sean los de tu materia**, no hay que escribir páginas: se rellenan
los datos de tu asignatura y la web genera su curso. Dime qué quieres cambiar, o hazlo
directamente en
[`_data/asignaturas.yml`]({{ site.github_url }}/blob/main/_data/asignaturas.yml) siguiendo
[estas instrucciones]({{ site.github_url }}/blob/main/docencia/anadir-asignatura.md).

## Si necesitas el detalle

En el repositorio está toda la documentación larga: el
[marco común]({{ site.github_url }}/blob/main/marco/marco-comun.md) con sus descriptores
observables, el [protocolo de aplicación]({{ site.github_url }}/blob/main/instrumentos/protocolo-aplicacion.md),
la [guía para montar el cuestionario en Microsoft Forms]({{ site.github_url }}/blob/main/instrumentos/formulario-microsoft.md)
y la [guía para construir tu rúbrica]({{ site.github_url }}/blob/main/instrumentos/rubrica-calidad-uso-ia.md).

## Sobre el proyecto

Proyecto de innovación docente **nº 3165** del IV Plan Propio de Docencia de la Universidad
de Sevilla, Acción 221, Modalidad B, Redes de Colaboración, curso 2026/2027. Diez
asignaturas de cuatro ramas con un marco común y un mismo cuestionario.

Materiales bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es),
obra original de la red. Para citarlos,
[CITATION.cff]({{ site.github_url }}/blob/main/CITATION.cff).
