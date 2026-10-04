---
title: "Para saber más"
permalink: /recursos/
---

# Para saber más

Las cuatro lecciones de tu curso te dan lo imprescindible. Si quieres entender mejor cómo
funcionan estos sistemas, estos recursos externos están bien hechos y son gratuitos.

**Nada de esto es obligatorio ni cuenta para tu nota.** Son para quien quiera ir un paso
más allá.

{% for r in site.data.recursos %}
## {{ r.titulo }}

<ul class="datos">
  <li><b>Quién lo hace</b><span>{{ r.autor }}</span></li>
  <li><b>Qué es</b><span>{{ r.tipo }} · {{ r.duracion }} · {{ r.idioma }}</span></li>
  <li><b>Dimensión</b><span>{{ r.dimension }}</span></li>
</ul>

{{ r.descripcion }}

{{ r.nota }}

<p><a href="{{ r.url }}">Ir al recurso →</a></p>
{% endfor %}

---

## Para el profesorado

Estos recursos se **enlazan, no se reproducen**: no hay material de terceros alojado en
este repositorio. Antes de añadir uno nuevo a
[`_data/recursos.yml`](https://github.com/jorgeBIGS/innovacion-US-3165/blob/main/_data/recursos.yml),
anota su autoría y su licencia, si la declara.

Dos cautelas al proponerlos al alumnado:

- **Solo como opcional.** La convocatoria del proyecto excluye las actividades fuera del
  horario de clase de las asignaturas implicadas, así que nada de esto puede ser exigible
  ni evaluable.
- **Plataformas externas.** Si un recurso obliga a crear cuenta, no puede imponerse: hay
  quien no quiera o no pueda aceptar sus condiciones. Ofrece siempre una alternativa.
