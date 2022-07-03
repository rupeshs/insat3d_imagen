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
from typing import Tuple

import h5py
import numpy as np
from PIL import Image, ImageChops
from skimage.transform import resize

from exception import InsatImageException
from imager_channels import CaliberationType, ImagerChannelType
from insat3d_imagen.exception import InsatImageError
from insat_image_interface import InsatImageInterface


def exception_handler(func):
    def handle_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            raise InsatImageException(
                InsatImageError.FILE_NOT_FOUND,
                "Failed to open HDF file!",
            )
        except Exception as err:
            raise InsatImageException(
                InsatImageError.PROCESSING_ERROR,
                str(err),
            )

    return handle_error


class InsatImage(InsatImageInterface):
    """INSAT 3D image processor implementations"""

    def __init__(self):
        self._width = 2816
        self._height = 2805

    @exception_handler
    def open_file(self, file_path: str):
        self.insat_hf = h5py.File(file_path, "r")

    @exception_handler
    def get_vis_image(self) -> Image:
        image_vis, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_vis.value,
            CaliberationType.image_vis_radiance.value,
        )
        image_vis_radiance = self._apply_lut(
            image_vis,
            radiance_lut,
        )
        image_vis_radiance = resize(
            image_vis_radiance,
            (
                self._width,
                self._height,
            ),
        )
        return self._down_sample_image(image_vis_radiance)

    @exception_handler
    def get_swir_image(self) -> Image:
        image_vis, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_swir.value,
            CaliberationType.image_swir_radiance.value,
        )
        image_vis_radiance = self._apply_lut(
            image_vis,
            radiance_lut,
        )
        image_vis_radiance = resize(
            image_vis_radiance,
            (
                self._width,
                self._height,
            ),
        )
        return self._down_sample_image(image_vis_radiance)

    @exception_handler
    def get_mir_image(self) -> Image:
        image_mir, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_mir.value,
            CaliberationType.image_mir_radiance.value,
        )
        image_mir_radiance = self._apply_lut(
            image_mir,
            radiance_lut,
        )
        return self._down_sample_image(image_mir_radiance)

    @exception_handler
    def get_tir1_image(self) -> Image:
        image_tir1, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_tir1.value,
            CaliberationType.image_tir1_radiance.value,
        )

        image_tir1_radiance = self._apply_lut(
            image_tir1,
            radiance_lut,
        )
        return self._down_sample_image(image_tir1_radiance)

    @exception_handler
    def get_tir2_image(self) -> Image:
        image_tir2, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_tir2.value,
            CaliberationType.image_tir2_radiance.value,
        )
        image_tir2_radiance = self._apply_lut(
            image_tir2,
            radiance_lut,
        )
        return self._down_sample_image(image_tir2_radiance)

    @exception_handler
    def get_wv_image(self) -> Image:
        image_wv, radiance_lut = self._get_image_radiance(
            ImagerChannelType.image_wv.value,
            CaliberationType.image_wv_radiance.value,
        )
        image_wv_radiance = self._apply_lut(
            image_wv,
            radiance_lut,
        )
        return self._down_sample_image(image_wv_radiance)

    @exception_handler
    def get_composite_dmp_image(self) -> Image:
        image_vis = self.get_vis_image()
        image_vis_r = np.array(image_vis)
        image_swir = self.get_swir_image()
        image_swir_g = np.array(image_swir)
        image_tir = self.get_tir1_image()
        image_tir_b = np.array(image_tir)
        arr_rgb = np.array(
            [
                image_vis_r.flatten(),
                image_swir_g.flatten(),
                image_tir_b.flatten(),
            ]
        )
        arr_rgb = arr_rgb.T.reshape((self._width, self._height, 3))
        return Image.fromarray(arr_rgb, mode="RGB")

    @exception_handler
    def get_composite_nmp_image(self) -> Image:
        image_tir1 = self.get_tir1_image()
        image_tir1_array = np.array(image_tir1)
        image_tir2 = self.get_tir2_image()
        image_mir = self.get_mir_image()
        image_r = np.array(ImageChops.difference(image_tir2, image_tir1))
        image_g = np.array(ImageChops.difference(image_tir1, image_mir))

        arr_rgb = np.array(
            [
                image_r.flatten(),
                image_g.flatten(),
                image_tir1_array.flatten(),
            ]
        )

        arr_rgb = arr_rgb.T.reshape((self._width, self._height, 3))
        return Image.fromarray(arr_rgb, mode="RGB")

    def _get_image_radiance(
        self,
        image_channel: ImagerChannelType,
        radiance: str,
    ) -> Tuple:
        sensor_data = self.insat_hf[image_channel]
        image_vis = np.array(sensor_data).squeeze()
        radiance_lut = np.array(self.insat_hf[radiance])
        return (image_vis, radiance_lut)

    def _apply_lut(
        self,
        image: np.ndarray,
        radiance_lut: np.ndarray,
    ) -> np.ndarray:
        # Normalize LUT
        radiance_lut = radiance_lut * (255 / radiance_lut.max())
        radiance_lut = radiance_lut[image]
        return radiance_lut

    def _down_sample_image(
        self,
        image: np.ndarray,
    ) -> Image:
        # Convert to 8 bit
        image = image.astype(np.uint8)
        return Image.fromarray(image)
