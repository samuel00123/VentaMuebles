from django.conf.urls import patterns,url

urlpatterns = patterns('demo.apps.webServices.wsProductos.views',
	url(r'^ws/productos/$','wsProductos_view',name= "ws_productos_url"),
)
