# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def map(request):
	return render(request, 'maps/mappage.html')

def mapConfirmed(request):
	from queryDBfunction import qDB
	SWval = request.GET['SW']
	NEval = request.GET['NE']

	pointNE = NEval.split()
	lat1 = pointNE[0]
	lat1 = float(str(lat1[0:-1]))
	lon1 = float(str(pointNE[1]))

	pointSW = SWval.split()
	lat2 = pointSW[0]
	lat2 = float(str(lat2[0:-1]))
	lon2 = float(str(pointSW[1]))	

	print lat1
	print lat2
	print lon1
	print lon2

	# Convert coordinates system
	from django.contrib.gis.gdal import SpatialReference, CoordTransform
	from django.contrib.gis.geos import Point
	gcoord = SpatialReference(4326)
	mycoord = SpatialReference(27700)
	trans = CoordTransform(gcoord, mycoord)

	pnt = Point(lon1, lat1, srid=4326)
	print 'x: %s; y: %s; srid: %s' % (pnt.x, pnt.y, pnt.srid)
	pnt.transform(trans)
	print 'x: %s; y: %s; srid: %s' % (pnt.x, pnt.y, pnt.srid)

	lon1Conv = str(pnt.x)
	lat1Conv = str(pnt.y)

	pnt = Point(lon2, lat2, srid=4326)
	print 'x: %s; y: %s; srid: %s' % (pnt.x, pnt.y, pnt.srid)
	pnt.transform(trans)
	print 'x: %s; y: %s; srid: %s' % (pnt.x, pnt.y, pnt.srid)

	lon2Conv = str(pnt.x)
	lat2Conv = str(pnt.y)

	# ll = lon2Conv + ' ' + lat2Con
	# ul = lon1Conv + ' ' + lat2Con
	# ur = lon1Conv + ' ' + lat1Con
	# lr = lon2Conv + ' ' + lat1Con
	# ll2 = lon2Conv + ' ' + lat2Con

	ll = lon2Conv + ' ' + lat2Conv
	ul = lon2Conv + ' ' + lat1Conv
	ur = lon1Conv + ' ' + lat1Conv
	lr = lon1Conv + ' ' + lat2Conv

	ll2 = lon2Conv + ' ' + lat2Conv

	print ll
	print ul
	print ur
	print lr
	print ll2


	# return HttpResponse("Thanks for your selection <br/>SW: " + request.GET['SW'] + " <br/>NE " + request.GET['NE'] )
	result = qDB(ll,ul,ur,lr,ll2)
	return render(request, 'maps/mappageConfirmed.html', {'SWval':str(SWval), 'NEval':str(NEval)})




