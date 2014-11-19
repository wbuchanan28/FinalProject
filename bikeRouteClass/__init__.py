# -*- coding: utf-8 -*-
"""
/***************************************************************************
 bikeRouteClass
                                 A QGIS plugin
 Maps a bike route and its difficulty
                             -------------------
        begin                : 2014-11-18
        copyright            : (C) 2014 by William Buchanan
        email                : wbuch28@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load bikeRouteClass class from file bikeRouteClass
    from bikerouteclass import bikeRouteClass
    return bikeRouteClass(iface)
