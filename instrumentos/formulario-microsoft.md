# Montar el cuestionario en Microsoft Forms

Hacen falta **dos formularios idénticos**, uno por medida. Las mismas preguntas en los
dos: lo que distingue una medida de otra es en cuál se responde, porque cada formulario
tiene su propia hoja de respuestas.

- **El inicial** lo pasa el docente en clase, antes de que el alumnado vea ninguna
  lección. **No se enlaza desde el curso ni se publica**: el docente lo abre o lo proyecta
  en clase. Si el enlace circulase, cualquiera podría responderlo después de haber leído
  las lecciones y la medida de partida dejaría de serlo.
- **El final** lo reparte el docente por Enseñanza Virtual o en clase, cuando el
  alumnado ha terminado el curso. Tampoco se publica.

Móntalo una vez y **duplícalo** en Forms: así son idénticos sin esfuerzo.

**Los dos son comunes a toda la red**, de modo que la coordinación recoge en dos hojas
todas las respuestas. Por eso la pregunta de asignatura y grupo es imprescindible: es lo
único que permite separarlas después.

La pregunta sobre cuántas lecciones ha leído va también en el inicial, aunque ahí la
respuesta esperable sea «ninguna»: sirve de comprobación de que nadie llega al
cuestionario con el curso ya leído.

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
| A | El código que se repartió en clase (`FP-024`) | Texto, respuesta corta |
| A | Asignatura y grupo | Opción |
| A | Curso más alto en el que estás matriculado | Opción |
| A | Formación previa en IA | Opción, Sí / No |
| A | Frecuencia de uso | Opción |
| B | Los 16 ítems de competencia percibida | **Likert**, escala 1–5 |
| C | Tareas en las que has usado IA | Opción, varias respuestas |
| C | Qué sueles pedirle · Si compruebas · Si lo declaras | Opción |
| C | Cuántas lecciones has leído (**solo en el formulario final**) | Opción |

El tipo **Likert** permite meter varias afirmaciones en una sola pregunta con la misma
escala: monta cuatro, una por dimensión, con sus cuatro ítems. El cuestionario queda en
una pantalla por bloque y se responde en diez minutos.

## 3. Ajustes que importan

- **Respuestas anónimas.** En *Configuración*, permite responder a «cualquier persona» o,
  si lo restringes a la Universidad, **desactiva el registro del nombre**. Si Forms guarda
  el nombre, el cuestionario deja de ser anónimo y el consentimiento que firmaron deja de
  ser cierto.
- **Una respuesta por persona: desactivado.** Esa opción obliga a identificar.
- **Marca todas las preguntas como obligatorias.** No hay ninguna que no se pueda
  responder, y las respuestas incompletas estropean la comparación pre/post. La
  voluntariedad está en participar o no, no en dejar huecos: quien no quiera participar,
  no envía el formulario.
- **Orden fijo:** no barajes preguntas ni opciones, o las dos medidas dejan de ser
  comparables.

## 4. El consentimiento, al principio

La primera página recoge la información y el consentimiento. Copia el texto del
[modelo en Word](https://jorgebigs.github.io/innovacion-US-3165/descargas/consentimiento-informado.docx) y cierra
con una pregunta de opción única:

> He leído esta información y acepto participar. · **Sí** / **No**

Quien responda «No» no continúa.

## 5. El código de emparejamiento

El código se reparte en clase, con el formato **código de asignatura + número**, por
ejemplo `FP-024`. En el formulario se pide tal cual, con una pregunta de texto corto:

> Escribe el código que te dieron en clase, por ejemplo FP-024.

Sin él, las respuestas del principio y del final no se pueden cruzar. No hay forma de
recuperarlo —no se guarda ninguna lista de a quién se dio cada número, y esa es justamente
la garantía de anonimato—, así que recuérdales que lo conserven al repartirlo y vuelve a
recordárselo antes de abrir el formulario final.

## 6. Control de acceso

En *Configuración*, cambia «Cualquier persona puede responder» por **«Solo las personas
de mi organización»**: así hace falta la cuenta de la Universidad y nadie de fuera entra
aunque tenga el enlace.

Esa opción **activa el registro del nombre**, que rompe el anonimato prometido en el
consentimiento: junto a ella hay un interruptor de «Registrar nombre» que hay que
**desactivar**. Comprueba que queda así antes de repartirlo, y revísalo también en los
formularios ya montados.

El enlace no se publica en ninguna página: lo reparte el docente por Enseñanza Virtual o
en clase. El código de emparejamiento hace de último filtro, porque una respuesta sin
código válido se descarta al analizar.

## 7. Recoger los resultados

Forms exporta a Excel. De ahí salen las medias por dimensión que se entregan al proyecto,
**siempre agregadas**: al equipo no va la hoja de respuestas, sino las distribuciones.
Véanse las [plantillas de análisis](../analisis/).

Un formulario por asignatura mantiene los datos separados por grupo sin esfuerzo. Si
prefieres uno solo para varias, añade una pregunta de asignatura y grupo al principio.
