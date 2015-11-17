# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BackupShape
                                 A QGIS plugin
 This plugin backups the selected shapefile layer and stores in a zipped file with current date time stamp
                             -------------------
        begin                : 2015-11-17
        copyright            : (C) 2015 by Josef Källgården
        email                : groundwatergis@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BackupShape class from file BackupShape.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bkupshp import BackupShape
    return BackupShape(iface)
