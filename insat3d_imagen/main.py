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

from exception import InsatImageException
from insat_image import InsatImage
from insat_image_interface import InsatImageInterface


def get_satellite_image(
    insat_image: InsatImageInterface,
    file_path: str,
) -> None:
    try:
        insat_image.open_file(file_path)
        image_vis = insat_image.get_vis_image()
        image_vis.save("outputs/image_vis.png")

        image_swir = insat_image.get_swir_image()
        image_swir.save("outputs/image_swir.png")

        image_mir = insat_image.get_mir_image()
        image_mir.save("outputs/image_mir.png")

        image_tir1 = insat_image.get_tir1_image()
        image_tir1.save("outputs/image_tir1.png")

        image_tir2 = insat_image.get_tir2_image()
        image_tir2.save("outputs/image_tir2.png")

        image_wv = insat_image.get_wv_image()
        image_wv.save("outputs/image_wv.png")

        image_rgb_dmp = insat_image.get_composite_dmp_image()
        image_rgb_dmp.save("outputs/image_dmp_rgb.png")

        image_rgb_nmp = insat_image.get_composite_nmp_image()
        image_rgb_nmp.save("outputs/image_nmp_rgb.png")

        print("Processing : OK")

    except InsatImageException as err:
        print("ERROR -> ", str(err.error) + " (" + str(err.msg) + ")")


if __name__ == "__main__":
    # file_path = r"E:\Satellite\insat3d\28-05-2022\3DIMG_12JUN2022_2130_L1B_STD.h5"
    file_path = r"E:\Satellite\insat3d\28-05-2022\3DIMG_28MAY2022_0930_L1B_STD.h5"
    get_satellite_image(InsatImage(), file_path)
