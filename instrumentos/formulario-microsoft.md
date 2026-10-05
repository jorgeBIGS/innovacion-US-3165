# Montar el cuestionario en Microsoft Forms

El formulario en línea sirve para la **medida final**, la que el alumnado repite al
terminar el curso desde la tarjeta «Autoevalúate». La medida inicial se pasa en clase,
antes de que vea ninguna lección.

Usa tu cuenta institucional de la Universidad de Sevilla, no una personal: así las
respuestas quedan en el entorno de la Universidad.

## 1. Crear el formulario

En [Microsoft Forms](https://forms.office.com), *Nuevo formulario*. Si tu versión ofrece
**importar preguntas desde un documento**, dale el
[cuestionario en Word](https://jorgebigs.github.io/innovacion-US-3165/descargas/cuestionario-autopercepcion.docx)
y te creará el esqueleto; luego revisa los tipos de pregunta. Si no, créalas a mano
siguiendo el [cuestionario](cuestionario-autopercepcion.md).

## 2. Qué tipo de pregunta usar

| Bloque | Pregunta | Tipo en Forms |
| --- | --- | --- |
| A | Código de emparejamiento | Texto, respuesta corta, **obligatoria** |
| A | Asignatura y grupo | Opción |
| A | Curso más alto en el que estás matriculado | Opción |
| A | Formación previa en IA | Opción, Sí / No |
| A | Frecuencia de uso | Opción |
| B | Los 16 ítems de competencia percibida | **Likert**, escala 1–5 |
| D | Tareas en las que has usado IA | Opción, varias respuestas |
| D | Qué sueles pedirle · Si compruebas · Si lo declaras | Opción |

El tipo **Likert** permite meter varias afirmaciones en una sola pregunta con la misma
escala: monta cuatro, una por dimensión, con sus cuatro ítems. El cuestionario queda en
una pantalla por bloque y se responde en diez minutos.

## 3. Ajustes que importan

- **Respuestas anónimas.** En *Configuración*, permite responder a «cualquier persona» o,
  si lo restringes a la Universidad, **desactiva el registro del nombre**. Si Forms guarda
  el nombre, el cuestionario deja de ser anónimo y el consentimiento que firmaron deja de
  ser cierto.
- **Una respuesta por persona: desactivado.** Esa opción obliga a identificar.
- **No marques preguntas como obligatorias**, salvo el código. Participar es voluntario, y
  eso incluye saltarse una pregunta.
- **Orden fijo:** no barajes preguntas ni opciones, o las dos medidas dejan de ser
  comparables.

## 4. El consentimiento, al principio

La primera página recoge la información y el consentimiento. Copia el texto del
[modelo en Word](https://jorgebigs.github.io/innovacion-US-3165/descargas/consentimiento-informado.docx) y cierra
con una pregunta de opción única:

> He leído esta información y acepto participar. · **Sí** / **No**

Quien responda «No» no continúa.

## 5. El código de emparejamiento

El código **se lo asignaste tú** al entregar el consentimiento. En el formulario pídelo
tal cual, con una pregunta de texto corto y obligatoria:

> Escribe el código que te dieron al principio del curso.

Sin ese código, las respuestas del principio y del final no se pueden cruzar y la
comparación pre/post se pierde. Es el error más caro de todo el proceso, y no tiene
arreglo después, así que recuérdaselo también en clase antes de abrir el formulario.

## 6. Publicar el enlace

Copia el enlace para responder y ponlo en el campo `formulario` de tu asignatura; véase
[cómo añadir tu asignatura](../docencia/anadir-asignatura.md). Aparecerá como la tarjeta
«Autoevalúate» al final de tu curso.

## 7. Recoger los resultados

Forms exporta a Excel. De ahí salen las medias por dimensión que se entregan al proyecto,
**siempre agregadas**: al equipo no va la hoja de respuestas, sino las distribuciones.
Véanse las [plantillas de análisis](../analisis/).

Un formulario por asignatura mantiene los datos separados por grupo sin esfuerzo. Si
prefieres uno solo para varias, añade una pregunta de asignatura y grupo al principio.
