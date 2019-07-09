from django.conf.urls import url
from viajes import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	#Material
    url(r'materiales/list', views.materiales_list, name='materiales_list'),
    url(r'materiales/ledit', views.materiales_ledit, name='materiales_ledit'),
	url(r'material/nuevo', views.material_nuevo, name='material_nuevo'),
	url('material/edit/(?P<pk>.+)/$', views.material_edit, name='material_edit'),
	#Vehiculo
	url(r'vehiculos/list', views.vehiculos_list, name='vehiculos_list'),
    url(r'vehiculos/ledit', views.vehiculos_ledit, name='vehiculos_ledit'),
	url(r'vehiculo/nuevo', views.vehiculo_nuevo, name='vehiculo_nuevo'),
	url('vehiculo/edit/(?P<pk>.+)/$', views.vehiculo_edit, name='vehiculo_edit'),
	#Chofer
	url(r'choferes/list', views.choferes_list, name='choferes_list'),
    url(r'choferes/ledit', views.choferes_ledit, name='choferes_ledit'),
	url(r'chofer/nuevo', views.chofer_nuevo, name='chofer_nuevo'),
	url('chofer/edit/(?P<pk>.+)/$', views.chofer_edit, name='chofer_edit'),
	#sucursal (se la gestionara por medio del admin)
	#Proveedor
	url(r'proveedores/list', views.proveedores_list, name='proveedores_list'),
    url(r'proveedores/ledit', views.proveedores_ledit, name='proveedores_ledit'),
    url(r'proveedor/nuevo', views.proveedor_nuevo, name='proveedor_nuevo'),
    url('proveedor/edit/(?P<pk>.+)/$', views.proveedor_edit, name='proveedor_edit'),

	#Orden / Recepcion
	#url(r'ordenes/list', views.ordenes_list, name='ordenes_list'),
    #url(r'cordenes/ledit', views.ordenes_ledit, name='ordenes_ledit'),
	url(r'orden/nuevo', views.orden_nuevo, name='orden_nuevo'),
	#url('orden/edit/(?P<pk>.+)/$', views.orden_edit, name='orden_edit'),
	



]