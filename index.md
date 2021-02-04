---
layout: poem
---

----------

## Problems

{% for num in (1..750) %}
{% assign title = "" | append: num %}
{% assign text = site.texts | where: "title", title | first %}
[Problem {{ title }}]({{ site.baseurl }}{{ text.url }}){% if text != nil %}&nbsp;&nbsp;&nbsp;&nbsp;completed {{ text.completed }}{% endif %}
{% endfor %}
