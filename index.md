---
layout: page
---

This project began on Monday November 28, 2011. I am posting here my progress
as I complete each problem. I will not include any answers nor will I say what
website I am getting these problems from. I intend for this to be a repository
for what I've learned from this experience and not a searchable site for those
looking for an easy answer.

----------

## Problems

{% for num in (1..750) %}
{% assign title = "" | append: num %}
{% assign problem = site.problems | where: "title", title | first %}
[Problem {{ title }}]({{ site.url }}{{ site.baseurl }}{{ problem.url }}){% if problem.completed != nil %}&nbsp;&nbsp;&nbsp;&nbsp;completed {{ problem.completed }}{% endif %}
{% endfor %}
