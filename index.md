---
layout: default
---

This project began on Monday November 28, 2011. I am posting here my progress
as I complete each problem. I will not include any answers nor will I say what
website I am getting these problems from. I intend for this to be a repository
for what I've learned from this experience and not a searchable site for those
looking for an easy answer.

Check out the [highlights]({{ site.url }}{{ site.baseurl }}/problems/highlights)
for a list of my favorite problems.

----------

## Problems

{% assign problems = site.problems | sort_date | reverse %}
{% for problem in problems %}

[Problem {{ problem.title }}]({{ site.url }}{{ site.baseurl }}{{ problem.url }})
&emsp;&emsp;completed {{ problem.completed | date: "%B %e, %Y" }}

{% endfor %}
