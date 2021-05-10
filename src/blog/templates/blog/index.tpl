{% extends 'core/base.tpl' %}

{% block title %}Blog Home{% endblock %}

{% block content %}
    <div class="container-fluid">
        <h2>Категории:</h2>
        <hr />
        <ol class="list-group list-group-numbered">
            {% for category in categories %}
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold"><h3><a href="/{{category.id}}">{{ category.title }}</a></h3></div>
                        <br />
                        {{ category.description|safe }}
                    </div>
                    <span class="badge bg-primary rounded-pill">{{ category.articles.all|length }}</span>
                </li>
            {% endfor %}
        </ol>
    </div>
{% endblock %}