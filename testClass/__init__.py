# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testClass
                                 A QGIS plugin
 This is a test plugin
                             -------------------
        begin                : 2014-11-18
        copyright            : (C) 2014 by Will Buchanan
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
    # load testClass class from file testClass
    from testclass import testClass
    return testClass(iface)
