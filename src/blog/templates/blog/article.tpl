{% extends 'core/base.tpl' %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
    <div class="container-fluid">
        <h2>{{article.title}}</h2>
        <hr />
        {{ article.content|safe }}
    </div>
{% endblock %}