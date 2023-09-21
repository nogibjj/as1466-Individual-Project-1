{%- extends 'full.tpl' -%}

{%- block codecell -%}
{% if cell.metadata.hide_code %}
<div style="display: none;">
{{ super() }}
</div>
{% else %}
{{ super() }}
{% endif %}
{%- endblock codecell -%}
