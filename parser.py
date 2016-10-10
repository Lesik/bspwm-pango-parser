#!/usr/bin/env python3

import sys
from yattag import Doc

COLOR_MONITOR_FG="#8dbcdf"
COLOR_MONITOR_BG="#333232"
COLOR_FOCUSED_MONITOR_FG="#b1d0e8"
COLOR_FOCUSED_MONITOR_BG="#144b6c"
COLOR_FREE_FG="#737171"
COLOR_FREE_BG="#333232"
COLOR_FOCUSED_FREE_FG="#000000"
COLOR_FOCUSED_FREE_BG="#504e4e"
COLOR_OCCUPIED_FG="#a7a5a5"
COLOR_OCCUPIED_BG="#333232"
COLOR_FOCUSED_OCCUPIED_FG="#d6d3d2"
COLOR_FOCUSED_OCCUPIED_BG="#504e4e"
COLOR_URGENT_FG="#f15d66"
COLOR_URGENT_BG="#333232"
COLOR_FOCUSED_URGENT_FG="#501d1f"
COLOR_FOCUSED_URGENT_BG="#d5443e"

usebg = True
def new_workspace(workspace, fg, bg):
    with tag('span', foreground=fg):
        text("    ")
        text(workspace)
        text("    ")
        if usebg:
            doc.attr(background=bg)

for line in sys.stdin:
    doc, tag, text = Doc().tagtext()

    # prophylactic check whether output starts with "W" in case
    # something went really wrong (e.g. bspc/bspwm not installed)
    if line.startswith("W"):
        line = line[1:]
        for item in line.split(':'):
            if item.lower().startswith("m"):
                # it's a monitor, ignore for now
                pass
            if item.lower().startswith(tuple("fou")):
                # it's a workspace
                state, workspace = item[0], item[1:]
                if state == 'f':
                    # free workspace
                    new_workspace(workspace, COLOR_FREE_FG, COLOR_FREE_BG)
                elif state == 'F':
                    # focused free workspace
                    new_workspace(workspace, COLOR_FOCUSED_FREE_FG, COLOR_FOCUSED_FREE_BG)
                elif state == 'o':
                    # occupied workspace
                    new_workspace(workspace, COLOR_OCCUPIED_FG, COLOR_OCCUPIED_BG)
                elif state == 'O':
                    # focused occupied workspace
                    new_workspace(workspace, COLOR_FOCUSED_OCCUPIED_FG, COLOR_FOCUSED_OCCUPIED_BG)
                elif state == 'u':
                    # urgent workspace
                    new_workspace(workspace, COLOR_URGENT_FG, COLOR_URGENT_BG)
                elif state == 'U':
                    # focused urgent workspace
                    new_workspace(workspace, COLOR_FOCUSED_URGENT_FG, COLOR_FOCUSED_URGENT_BG)
            if item.lower().startswith(tuple("ltg")):
                # it's a layout, state or flag, ignore for now
                # later this could show cool FontAwesome icons, e.g. fullscreen
                pass

        # stdout.write only writes after finishing getting input, use print instead
        #sys.stdout.write(doc.getvalue())
        print(doc.getvalue())
