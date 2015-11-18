# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BackupLayer
                                 A QGIS plugin
 Backup the selected layer by saving the corresponding data file(s) in a zip file with datetime stamp appended to name
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
    """Load BackupLayer class from file bkuplyr.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bkuplyr import BackupLayer
    return BackupLayer(iface)
