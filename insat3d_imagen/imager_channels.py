#
# This file is part of the Insat3DImagen
# Copyright (c) 2022 Rupesh Sreeraman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from enum import Enum


class ImagerChannelType(str, Enum):
    """INSAT 3D Imager channels types"""

    image_vis = "IMG_VIS"  # Visible channel
    image_swir = "IMG_SWIR"  # Shortwave Infrared Channel
    image_mir = "IMG_MIR"  # Middle wave Infrared Channel
    image_tir1 = "IMG_TIR1"  # Thermal Infrared Channel 1
    image_tir2 = "IMG_TIR2"  # Thermal Infrared Channel 2
    image_wv = "IMG_WV"  # Water Vapor Channel


class CaliberationType(str, Enum):
    """INSAT 3D Imager caliberation types"""

    image_vis_radiance = "IMG_VIS_RADIANCE"
    image_swir_radiance = "IMG_SWIR_RADIANCE"
    image_mir_radiance = "IMG_MIR_RADIANCE"
    image_tir1_radiance = "IMG_TIR1_RADIANCE"
    image_tir2_radiance = "IMG_TIR2_RADIANCE"
    image_wv_radiance = "IMG_WV_RADIANCE"
