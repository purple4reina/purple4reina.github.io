---
layout: poem
---

----------

## Problems

{% for text in site.texts %}
[Problem {{ text.title }}]({{ site.baseurl }}{{ text.url }})&nbsp;&nbsp;&nbsp;&nbsp;completed {{ text.completed }}
{% endfor %}
