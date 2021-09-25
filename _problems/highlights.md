---
layout: default
permalink: /problems/highlights
---

# Highlights

{% assign problems = site.problems | sort_date | reverse %}
{% for problem in problems %}

{% if problem.highlight %}
[Problem {{ problem.title }}]({{ site.url }}{{ site.baseurl }}{{ problem.url }})
&emsp;&emsp;{{ problem.highlight }}
{% endif %}

{% endfor %}
