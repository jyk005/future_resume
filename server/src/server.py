# Pyramid Imports
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response
import json

""" Routes """

# VIEW: Web Controller Route
def web_ui_route(req):
  return render_to_response('templates/web_ui.html', [], request=req)


""" Main Entrypoint """

if __name__ == '__main__':
  with Configurator() as config:
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('web_ui', '/')
    config.add_view(web_ui_route, route_name='web_ui')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 1234, app)
  print('Web server started on: http://0.0.0.0:8000 OR http://localhost:8000')
  server.serve_forever()
