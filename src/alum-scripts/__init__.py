# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>


bl_info = {
    "name": "Alum scripts",
    "author": "Alumx",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "3D View > Sidebar > Misc",
    "warning": "",
    "description": "Assortment of scripts I made for my own personal use",
    "wiki_url": "https://github.com/Alumx/Alum-scripts",
    "doc_url": "https://github.com/Alumx/Alum-scripts",
    "tracker_url": "https://github.com/Alumx/Alum-scripts",
    "category": "3D View",
}

from . import alum_scripts

def register():
    alum_scripts.register()

def unregister():
    alum_scripts.unregister()

if __name__ == "__main__":
    register() 