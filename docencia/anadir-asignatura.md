# Añadir una asignatura al sitio

> **Procedimiento interno.** En esta red los cambios los centraliza la coordinación: si
> eres docente del proyecto, manda los ejemplos de tu materia y se publican por ti. Esta
> página es para quien mantiene el sitio, y para quien reutilice el repositorio por su
> cuenta.

Los cursos no se escriben uno a uno: se **generan**. Las cuatro lecciones son comunes a
toda la red y cada asignatura aporta sus ejemplos, sus fuentes y sus reglas. Así, cuando
mejoramos una explicación, mejora en las diez asignaturas a la vez.

Tú rellenas un bloque de datos. El sitio hace el resto.

## Todas las asignaturas tienen ya curso

Las que nadie ha revisado usan los **ejemplos comunes de su rama de conocimiento**,
definidos en
[`_data/ramas.yml`](https://github.com/jorgeBIGS/innovacion-US-3165/blob/main/_data/ramas.yml),
y lo advierten en la página.

Así que nunca se parte de cero: se corrige lo que no encaje y, cuando el docente da el
visto bueno, `estado: borrador` pasa a `estado: completo` y desaparece el aviso.

La precedencia es simple: lo que define la asignatura gana; lo que no define, lo pone su
rama.

## 1. Edita `_data/asignaturas.yml`

Busca tu asignatura —ya están las diez— y completa los campos. Toma como modelo la de
Fundamentos de Programación, que está completa.

```yaml
- slug: mi-asignatura            # identificador en la URL, sin acentos ni espacios
  nombre: Nombre de la asignatura
  titulacion: Grado en …
  curso: Primero
  centro: Facultad de …
  rama: Derecho
  docente: Nombre del docente
  estado: completo               # 'preparacion' mientras no esté lista
  pesos: { d1: 20, d2: 40, d3: 25, d4: 15 }
```

### El formulario de autoevaluación

Toda la red comparte un mismo formulario, definido en `formulario_comun` dentro de
`_config.yml`. Aparece como una tarjeta al final de las cuatro lecciones de cada curso, y
no hay que hacer nada para que salga.

Solo si una asignatura necesita el suyo propio:

```yaml
  formulario: https://…
```

Prepáralo con las mismas preguntas del
[cuestionario de autopercepción](../instrumentos/cuestionario-autopercepcion.md) y pide en
él el mismo código de emparejamiento que usaste en la medida inicial; sin ese código, las
dos respuestas no se pueden cruzar. Si lo montas con la cuenta institucional, sigue
[montar el cuestionario en Microsoft Forms](../instrumentos/formulario-microsoft.md). Mientras no lo pongas, la tarjeta avisa de que el
enlace está pendiente.

La medida **inicial** no va aquí: esa se pasa en clase, antes de que el alumnado vea
ninguna lección.

### Los campos que dan contenido

| Campo | Qué es | Dónde sale |
| --- | --- | --- |
| `contexto` | Dos o tres frases sobre qué está en juego con la IA en tu materia | Lección 1 |
| `tareas` | Lista de tareas en las que tu alumnado ya usa la IA | Lección 1 |
| `fallo` | `pregunta` que provoca un fallo comprobable y qué cabe `esperado` | Lección 1 |
| `peticiones` | Pares `pobre` / `mejor` con peticiones reales de tu materia | Lección 2 |
| `riesgos` | Qué se pierde o qué daño hace un mal uso en tu disciplina | Lecciones 2 y 4 |
| `verificacion` | Cómo se comprueba en tu materia, en un párrafo | Lección 3 |
| `fuentes` | Tus fuentes de verdad, por orden | Lección 3 |
| `casos` | Seis situaciones ambiguas para clasificar | Lección 4 |
| `entrega` | Qué producción valorarás con la rúbrica | Uso interno |

Escribe los ejemplos **como hablarías a tu alumnado**. Van a leerlos ellos.

## 2. Genera las páginas

```
python3 bin/generar-cursos.py
```

Crea la portada del curso y sus cuatro lecciones. Las páginas son solo cabeceras: el
contenido vive en los datos y en las lecciones comunes, así que no hay nada que copiar.

## 3. Publica

```
git add -A
git commit -m "Curso de <asignatura>"
git push
```

En un par de minutos está en línea.

## Los vídeos

Cada lección incluye uno o dos vídeos cortos de la asociación Programamos, definidos en
`_data/videos.yml` y comunes a toda la red. Se incrustan desde YouTube con el dominio sin
cookies; no hay ninguna copia alojada aquí.

Si en tu materia prefieres otra selección, añade un bloque `videos` a tu asignatura con la
misma estructura y sustituirá a la común en las lecciones que indiques:

```yaml
  videos:
    "1":
      - yt: IDENTIFICADOR
        titulo: "Título del vídeo"
        duracion: "6 min"
        por_que: "Por qué le conviene verlo a tu alumnado"
        articulo: "https://…"
```

Son opcionales para el alumnado y no evaluables.

## Textos a medida

Los campos anteriores cubren la personalización habitual. Cuando una asignatura necesita
cambiar además algún párrafo de las lecciones, se añade un bloque `textos` con las claves
que quiera sobrescribir; las que no estén, usan el texto común:

```yaml
  textos:
    l1_comprobacion: |        # lista de comprobación de la lección 1
    l2_cierre: >-             # cierre de la tabla de peticiones
    l2_riesgos_intro: >-      # entradilla de 'Cuándo no usarla'
    l2_comprobacion: |
    l3_entrega: >-            # párrafo de 'Lo que entregas es tuyo'
    l3_comprobacion: |
    l4_colectivo: >-          # el plano colectivo, más allá de la asignatura
    l4_casos_contraste: …     # contra qué se contrastan los casos dudosos
    l4_casos_cierre: >-
    l4_comprobacion: |
```

Las claves `_comprobacion` son listas numeradas en Markdown, así que usan `|` para
conservar los saltos de línea. Las demás son texto corrido con `>-`.

Añadir una clave nueva exige tocar la lección correspondiente en `_includes/lecciones/`:
envuelve el texto común en `{% raw %}{% if t.clave %}…{% else %}…{% endif %}{% endraw %}`.

## Si no te encaja la lección común

Los datos cubren la personalización habitual. Si tu materia necesita algo que no encaja,
dilo en el grupo antes de improvisar: probablemente le sirva a más gente y el sitio pueda
mejorarse para todas.

## Comprobar antes de publicar

- El curso se ve bien con tus datos y no queda ningún hueco genérico.
- Los seis casos de la lección 4 son realmente ambiguos, no obvios.
- La pregunta de `fallo` **falla de verdad**: pruébala antes.
- Las reglas de uso de tu asignatura están escritas y son claras.
