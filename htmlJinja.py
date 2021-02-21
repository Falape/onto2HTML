import jinja2 as j2


def htmlClass(nome, lista, path):

    temp= j2.Template('''
    <html>
    <head>
    <title>Classe {{name}}</title>
    </head>
     <h1> {{ name }}  </h1>
     <ul>
        {% for a in li %}
        <li><a href={{link+a}}.html>{{a}}</a></li>
        {% endfor %}
     </ul>
    </html>
    ''')

    return temp.render({"name": nome,"li":lista, "link":path})

def htmlIndividuals(nome, classList, pathClass, individuoList, pathindividuos):

    temp= j2.Template('''
    <html>
     <h1> {{ name }}  </h1>
        <hr style="width:50%;text-align:left;margin-left:0">
        <h2> Classes  </h2>
            <ul>
                {% for a in class %}
                <p>{{a[0]}} <a href={{link+a[1]}}.html>{{a[1]}}</a></p>
                {% endfor %}
            </ul>
        <hr style="width:50%;text-align:left;margin-left:0">
        <h2> Objects </h2>
            <ul>
                {% for a in individuo %}
                <p>{{a[0]}}: <a {{a[0]}}: href={{linkInd+a[1]}}.html>{{a[1]}}</a></p>
                {% endfor %}
            </ul>
    </html>
    ''')

    return temp.render({"name": nome, "class":classList , "individuo":individuoList, "link":pathClass, "linkInd":pathindividuos})
