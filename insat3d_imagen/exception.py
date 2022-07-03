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


class InsatImageError(Enum):
    FILE_NOT_FOUND = "FILE_NOT_FOUND"
    PROCESSING_ERROR = "PROCESSING_ERROR"


class InsatImageException(Exception):
    """
    INSAT Image Exception
    """

    __slots__ = ["error", "msg"]

    def __init__(self, error: InsatImageError, msg: str):
        super().__setattr__("error", error)
        super().__setattr__("msg", msg)
