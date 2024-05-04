import bpy

class OBJECT_OT_clean_unparent(bpy.types.Operator):
    """Remove vertex group and unparent from armature"""
    bl_idname = "as.clean_unparent"


    bl_label = "Remove vertex group and unparent from armature"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):
        for ob in context.selected_objects:
             if ob.type == 'MESH':
              for x in ob.vertex_groups:
                 ob.vertex_groups.remove(x)

        return {'FINISHED'}


class PANEL_PT_alumscripts_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "opacity.settings"
    bl_space_type = 'VIEW_3D'
    bl_label = "Alum Scripts"
    bl_region_type = "UI"
    bl_category = "Item"


    def draw(self, context):
        layout = self.layout

        box = layout.box()                             
        col = box.column(align = True)
        col.label(text="Alum scripts")

        row = col.row(align=True)
        #row.scale_y = 2.0
        #row1=row.split(align=True)
        #row1.scale_x=0.50
        #row1.scale_y=2.0
        row.operator("as.clean_unparent", text = "Clean and unparent")
        row = col.row(align=True)

                                
                                

classes = (
    OBJECT_OT_clean_unparent,
    PANEL_PT_alumscripts_panel
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
