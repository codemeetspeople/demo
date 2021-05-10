{% load bootstrap4 %}

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{% block title %}Base template{% endblock %}</title>
        {% bootstrap_css %}
    </head>
    <body>
        {% include 'core/navbar.tpl' %}

        {% block content %}{% endblock %}

        {% bootstrap_javascript jquery='full' %}
    </body>
</html>