# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
import math

# from django.conf import settings
# import mapnik
# import utils

MAX_ZOOM_LEVEL = 10
TILE_WIDTH     = 256
TILE_HEIGHT    = 256

def root(request):
	try:
		baseURL = request.build_absolute_uri()
		xml = []
		xml.append('<?xml version="1.0" encoding="utf-8" ?>')
		xml.append('<Services>')
		xml.append(' <TileMapService ' +
			'title="Paperplaces Tile Map Service" ' +
			'version="1.0" href="' + baseURL + '/1.0"/>')
		xml.append('</Services>')
		return HttpResponse("\n".join(xml), content_type="text/xml")
	except:
		traceback.print_exc()
		return HttpResponse("Error")

def service(request, version):
	try:
		if version != "1.0":
			raise Http404
		baseURL = request.build_absolute_uri()
		xml = []
		xml.append('<?xml version="1.0" encoding="utf-8" ?>')
		xml.append('<TileMapService version="1.0" services="' +
			baseURL + '">')
		xml.append(' <Title>ShapeEditor Tile Map Service' +
			'</Title>')
		xml.append(' <Abstract></Abstract>')
		xml.append(' <TileMaps>')
		# This is commented out as i dont have the tables set up
		# for shapefile in Shapefile.objects.all():
		# 	id = str(shapefile.id)
		# 	xml.append(' <TileMap title="' +
		# 	shapefile.filename + '"')
		# 	xml.append(' srs="EPSG:4326"')
		# 	xml.append(' href="'+baseURL+'/'+id+'"/>')
		xml.append(' </TileMaps>')
		xml.append('</TileMapService>')
		return HttpResponse("\n".join(xml), content_type="text/xml")
	except:
		traceback.print_exc()
		return HttpResponse("Error")



def tileMap(request, version, shapefile_id):
    if version != "1.0":
        raise Http404

    # try:
    #     shapefile = Shapefile.objects.get(id=shapefile_id)
    # except Shapefile.DoesNotExist:
    #     raise Http404

    try:
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version="1.0" encoding="utf-8" ?>')
        xml.append('<TileMap version="1.0" ' +
                   'tilemapservice="' + baseURL + '">')
		# This is commented out as i dont have the tables set up
        # xml.append('  <Title>' + shapefile.filename + '</Title>')
        xml.append('  <Abstract></Abstract>')
        xml.append('  <SRS>EPSG:4326</SRS>')
        xml.append('  <BoundingBox minx="-180" miny="-90" ' +
                   'maxx="180" maxy="90"/>')
        xml.append('  <Origin x="-180" y="-90"/>')
        xml.append('  <TileFormat width="' + str(TILE_WIDTH) +
                   '" height="' + str(TILE_HEIGHT) + '" ' +
                   'mime-type="image/png" extension="png"/>')
        xml.append('  <TileSets profile="global-geodetic">')
        for zoomLevel in range(0, MAX_ZOOM_LEVEL+1):
            href = baseURL + "/{}".format(zoomLevel)
            unitsPerPixel = "{}".format(_unitsPerPixel(zoomLevel))
            order = "{}".format(zoomLevel)

            xml.append('    <TileSet href="' + href + '" ' +
                       'units-per-pixel="'+  unitsPerPixel + '"' +
                       ' order="' + order + '"/>')
        xml.append('  </TileSets>')
        xml.append('</TileMap>')
        response = "\n".join(xml)
        return HttpResponse(response, content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Error")

def tile(request, version, shapefile_id, zoom, x, y):
	return HttpResponse("Tile")


def _unitsPerPixel(zoomLevel):
    return 0.703125 / math.pow(2, zoomLevel)
