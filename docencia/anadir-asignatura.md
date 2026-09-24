---
title: "Añadir tu asignatura"
---

# Añadir tu asignatura al sitio

Los cursos no se escriben uno a uno: se **generan**. Las cuatro lecciones son comunes a
toda la red y cada asignatura aporta sus ejemplos, sus fuentes y sus reglas. Así, cuando
mejoramos una explicación, mejora en las diez asignaturas a la vez.

Tú rellenas un bloque de datos. El sitio hace el resto.

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

### Los campos que dan contenido

| Campo | Qué es | Dónde sale |
| --- | --- | --- |
| `contexto` | Dos o tres frases sobre qué está en juego con la IA en tu materia | Lección 1 |
| `tareas` | Lista de tareas en las que tu alumnado ya usa la IA | Lección 1 |
| `fallo` | `pregunta` que provoca un fallo comprobable y qué cabe `esperado` | Lección 1 y guía de aula 1 |
| `peticiones` | Pares `pobre` / `mejor` con peticiones reales de tu materia | Lección 2 |
| `riesgos` | Qué se pierde o qué daño hace un mal uso en tu disciplina | Lecciones 2 y 4 |
| `verificacion` | Cómo se comprueba en tu materia, en un párrafo | Lección 3 |
| `fuentes` | Tus fuentes de verdad, por orden | Lección 3 |
| `casos` | Seis situaciones ambiguas para clasificar | Lección 4 y guía de aula 4 |
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

## Si no te encaja la lección común

Los datos cubren la personalización habitual. Si tu materia necesita algo que no encaja,
dilo en el grupo antes de improvisar: probablemente le sirva a más gente y el sitio pueda
mejorarse para todas.

## Comprobar antes de publicar

- El curso se ve bien con tus datos y no queda ningún hueco genérico.
- Los seis casos de la lección 4 son realmente ambiguos, no obvios.
- La pregunta de `fallo` **falla de verdad**: pruébala antes.
- Las reglas de uso de tu asignatura están escritas y son claras.
