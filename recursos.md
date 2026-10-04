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

Si eres docente y quieres proponer un recurso, pasa por el
[área del profesorado](/profesorado/).
