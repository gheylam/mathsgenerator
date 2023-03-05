''' Methods that creates shapes widthd on given parameters.

@author: Tsz Hey Lam 
@data: 04.03.2023 
'''

import numpy as np
from vedo import *
from enum import Enum


class RightAngleTriangle:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
        self._coords = self._gen_coords(height, width)

    def get_coords(self):
        return self._coords

    def transform_reflect(self, reflect_line_start: '1x3 np.array',
                          relfect_line_end: '1x3 np.array', output: 'list' = []) -> 'list':
        return

    def gen_vedo_geometry(self):
        line_01 = Line(self._coords[0, :], self._coords[1, :])
        line_02 = Line(self._coords[1, :], self._coords[2, :])
        line_03 = Line(self._coords[2, :], self._coords[0, :])
        return [line_01, line_02, line_03]

    def _gen_coords(self, height: int, width: int):
        origin = [0, 0, 0]
        tl = [0, height, 0]
        br = [width, 0, 0]
        pts = np.array([origin, tl, br])
        return pts


class Grid:
    def __init__(self, height: int, width: int, quads: int):
        self._height = height
        self._width = width
        self._border_coords = self._gen_border_coords(height, width, quads)
        self._axis_coords = self._gen_axis_coords(height, width, quads)
        self._vedo_axes_dict = self._gen_vedo_axes_grid(height, width, quads)

    def gen_vedo_geometry(self):
        line_01 = Line(self._border_coords[1, :], self._border_coords[2, :])
        line_02 = Line(self._border_coords[2, :], self._border_coords[3, :])
        line_03 = Line(self._border_coords[3, :], self._border_coords[4, :])
        line_04 = Line(self._border_coords[4, :], self._border_coords[1, :])
        x_axis = Line(self._axis_coords[0, :], self._axis_coords[1, :])
        y_axis = Line(self._axis_coords[2, :], self._axis_coords[3, :])
        return [line_01, line_02, line_03, line_04, x_axis, y_axis]

    def get_axis_coords(self):
        return self._axis_coords

    def get_vedo_axes(self):
        return self._vedo_axes_dict

    def _gen_vedo_axes_grid(self, height: int, width: int, quads: int):
        if quads == 1:
            x_axis_shift = 0
            y_axis_shift = 0
        elif quads == 4:
            x_axis_shift = 0.5
            y_axis_shift = 0.5

        axs = dict(
            xtitle="x",
            ytitle="y",
            numberOfDivisions=height,
            xyAlpha=0.15,
            axesLineWidth=2,
            gridLineWidth=3,
            xyGridColor='black',
            xShiftAlongY=x_axis_shift,
            yShiftAlongX=y_axis_shift,
        )
        return axs

    def _gen_axis_coords(self, height: int, width: int, quads: int):
        if quads == 1:
            x_start = [0, 0, 0]
            x_end = [width, 0, 0]
            y_start = [0, 0, 0]
            y_end = [0, height, 0]
        elif quads == 4:
            midpoint_height = int(height/2)
            midpoint_width = int(width/2)
            x_start = [-midpoint_width, 0, 0]
            x_end = [midpoint_width, 0, 0]
            y_start = [0, -midpoint_height, 0]
            y_end = [0, midpoint_height, 0]
        pts = np.array([x_start, x_end, y_start, y_end])
        return pts

    def _gen_border_coords(self, height: int, width: int, quads: int):
        origin = [0, 0, 0]
        if quads == 1:
            tl = [0, height, 0]
            tr = [width, height, 0]
            br = [width, height, 0]
            bl = [0, 0, 0]

        elif quads == 4:
            midpoint_height = int(height/2)
            midpoint_width = int(width/2)
            tl = [-midpoint_width, midpoint_height, 0]
            tr = [midpoint_width, midpoint_height, 0]
            br = [midpoint_width, -midpoint_height, 0]
            bl = [-midpoint_width, -midpoint_height, 0]
        pts = np.array([origin, tl, tr, br, bl])
        return pts


my_triangle = RightAngleTriangle(5, 5)
my_grid = Grid(10, 10, 4)
print(my_grid.get_axis_coords())

vedo_plotter = Plotter(shape=(1, 1), pos=(0, 0), interactive=False)
vedo_plotter.show(my_triangle.gen_vedo_geometry(),
                  my_grid.gen_vedo_geometry(), axes=my_grid.get_vedo_axes(), interactive=True)
