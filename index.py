from bottle import route, static_file, run, error, static_file


@route('/')
@route('/a')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> a </title>
                    <meta charset="utf-8">
                </head>

                <body>
                    <h1> Stafurinn A </h1>
                    
                    <a href="a"><img src="/static/img/a.png"></a>
                    <h3> Fleiri Stafir </h3>
                    <a href="b"><img src="/static/img/b.png"></a>
                    <a href="c"><img src="/static/img/c.png"></a>
                </body>
            </html>
        '''

@route('/b')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> b </title>
                    <meta charset="utf-8">
                </head>

                <body>
                    <h2> <h1> Stafurinn V </h1>
                    
                    <a href="b"><img src="/static/img/b.png"></a>
                    <h3> Fleiri Stafir </h3>
                    <a href="a"><img src="/static/img/a.png"></a>
                    <a href="c"><img src="/static/img/c.png"></a>
                </body>
            </html>
        '''

@route('/c')
def index():
    return '''
        <!DOCTYPE html>
            <html>
                <head>
                    <title> c </title>
                    <meta charset="utf-8">
                </head>

                <body>
                    <h1> Stafurinn C </h1>
                    
                    <a href="c"><img src="/static/img/c.png"></a>
                    <h3> Fleiri Stafir </h3>
                    <a href="b"><img src="/static/img/b.png"></a>
                    <a href="a"><img src="/static/img/a.png"></a>
                </body>
            </html>
        '''

@error(404)
def error404(error):
    return "Error! Shit's Fooked mate"

@route('/static/img/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./static/img', mimetype='image/png')

run(host='localhost', port=8080, debug=True)