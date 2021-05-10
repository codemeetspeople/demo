{% extends 'core/base.tpl' %}

{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    <div class="container-fluid">
        <h2>{{category.title}}:</h2>
        <hr />
        {{ category.description|safe }}
        <ol class="list-group list-group-numbered">
            {% for article in category.articles.all %}
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold"><h3><a href="/{{category.id}}/{{article.id}}">{{ article.title }}</a></h3></div>
                    </div>
                </li>
            {% endfor %}
        </ol>
    </div>
{% endblock %}