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

from abc import ABC, abstractmethod
from PIL import Image


class InsatImageInterface(ABC):
    """INSAT 3D image processor interface"""

    @abstractmethod
    def open_file(self, file_path: str):
        """Open a INSAT 3D HDF file

        Args:
            file_path (str): File path
        """
        pass

    @abstractmethod
    def get_vis_image(self) -> Image:
        """Get Shortwave Infrared(SWIR) channel image

        Returns:
            Image: PIL image
        """
        pass

    @abstractmethod
    def get_swir_image(self) -> Image:
        """Get Short Wave IR(SWIR) channel image

        Returns:
            Image: PIL image
        """
        pass

    @abstractmethod
    def get_mir_image(self) -> Image:
        """Get Middle Wave Infrared(MIR) channel image

        Returns:
            Image: PIL image
        """
        pass

    @abstractmethod
    def get_tir1_image(self) -> Image:
        """Get Thermal Infrared(TIR1) channel image

        Returns:
            Image: PIL image
        """
        pass

    @abstractmethod
    def get_tir2_image(self) -> Image:
        """Get Thermal Infrared(TIR2) channel image

        Returns:
            Image: PIL image
        """
        pass

    @abstractmethod
    def get_wv_image(self) -> Image:
        """Get Water Vapor channel image

        Returns:
            Image: PIL image
        """
        pass

    def get_composite_dmp_image(self) -> Image:
        """Get RGB composite daytime microphysics(DMP) image

        Returns:
            Image: PIL image
        """
        pass

    def get_composite_nmp_image(self) -> Image:
        """Get RGB composite nighttime microphysics(NMP) image

        Returns:
            Image: PIL image
        """
        pass
