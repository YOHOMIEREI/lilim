init -1 python:
    def set_spot_flag(which, flag, origx, origy):
        store.spot_dark = True
        store.big_spot_node = which
        
        next = spot_next[which]
        if next == None or next == True: # remove this for new chapter
            return

        #spot_show[which] = flag
        store.spot_zoom = next
        spot_settings["spot_moving"] = True
        spot_settings["spot_old_x"] = spot_coords[which][0]+idiff
        spot_settings["spot_old_y"] = spot_coords[which][1]+idiff
        spot_settings["spot_new_x"] = spot_coords[next][0]+idiff
        spot_settings["spot_new_y"] = spot_coords[next][1]+idiff

    def setup_at(which):
        next = spot_next[which]
        store.big_spot_node = which
        spot_settings["spot_old_x"] = spot_coords[which][0]+idiff
        spot_settings["spot_old_y"] = spot_coords[which][1]+idiff

    
    def start_spot_zoom(*args, **kwargs):
        store.spot_zooming = True
        renpy.restart_interaction()

    def stop_spot_move(*args, **kwargs):
        spot_settings["spot_old_x"] = spot_settings["spot_new_x"]
        spot_settings["spot_old_y"] = spot_settings["spot_new_y"]
        spot_settings["spot_moving"] = False
        renpy.play("sfx/node_appear.ogg")

    def finish_spot_zoom(*args, **kwargs):
        spot_show[store.spot_zoom] = True
        store.spot_zoom = ""
        store.spot_zooming = False
        renpy.restart_interaction()


define pause_game = True
define idiff = (130/2)
default draw_background = True

default spot_show = {
    "spot_10801": True,
    "spot_10802": False,
    "spot_10803": False,
    "spot_10804": False,
    "spot_10805": False,
    "spot_10806": False,
    "spot_10807": False,
    "spot_10808": False
}

default spot_zoom = ""
default spot_zooming = False
default spot_dark = False # during dialogue, deactivate buttons

default is_boss_map = False

default boss_map_dict = {}

default spot_next = {
    "spot_10801": "spot_10802",
    "spot_10802": "spot_10803",
    "spot_10803": "spot_10804",
    "spot_10804": "spot_10805",
    "spot_10805": "spot_10806",
    "spot_10806": "spot_10807",
    "spot_10807": "spot_10808",
    "spot_10808": None
}


default spot_coords = {
    "spot_10801": [636-idiff, 874-idiff], #強欲の都
    "spot_10802": [1318-idiff, 874-idiff], #傲慢の都
    "spot_10803": [410-idiff, 597-idiff], #怠惰の都
    "spot_10804": [1556-idiff, 606-idiff], #暴食の都
    "spot_10805": [569-idiff, 307-idiff], #嫉妬の都
    "spot_10806": [1370-idiff, 348-idiff], #憤怒の都
    "spot_10807": [984-idiff, 251-idiff], #色欲の都
    "spot_10808": [980-idiff, 592-idiff], #堕落文明食卓
}

default spot_names = {
    "spot_10801": "Capital of Greed",
    "spot_10802": "Capital of Pride",
    "spot_10803": "Capital of Sloth",
    "spot_10804": "Capital of Gluttony",
    "spot_10805": "Capital of Envy",
    "spot_10806": "Capital of Wrath",
    "spot_10807": "Capital of Lust",
    "spot_10808": "Banquet of Depraved Civilization"
}

default spot_settings = {
    "spot_new_x": 0,
    "spot_new_y": 0,
    "spot_old_x": spot_coords["spot_10801"][0]+idiff,
    "spot_old_y": spot_coords["spot_10801"][1]+idiff,
    "spot_moving": False,
    "marker_visible": True
}



## bouncing next icon
define next_x = 60
define next_y = 110

default draw_big_spot = False
default big_spot_node = "spot_10801"

transform next_icon_bounce:
    easeout 0.30 yoffset +14
    easein 0.34 yoffset 0
    repeat


### MAP TRANSFORMS
transform map_building_transform(offs):
    pause offs
    easein 2 alpha 0.6
    pause offs
    easein 2 alpha 1.0
    repeat

transform map_move_transform(offs, ps):
    pause ps
    ease 2 yoffset 30-offs
    #easein 4 alpha 0.0
    pause ps
    #easein 4 alpha 1.0
    ease 2 yoffset 0
    repeat

transform map_particle_transform(one, two):
    linear 0 alpha two
    ease 3 alpha one
    ease 3 alpha two
    repeat

transform map_pulse_transform:
    ease 2.8 alpha 0.5
    ease 2.2 alpha 1.0
    pause 0.5
    repeat

transform fast_move(oldx, oldy, newx, newy):
    function start_spot_zoom
    xpos oldx
    ypos oldy
    linear 0.8 xpos newx ypos newy
    function stop_spot_move
    block:
        easeout 0.30 yoffset +14
        easein 0.34 yoffset 0
        repeat

transform spot_zoom_in:
    yanchor 0.5 xanchor 0.5 
    zoom 0.0
    linear 0.75 zoom 1.0
    function finish_spot_zoom

## MAIN

screen pause_screen:   
    for spot in spot_show.keys():
        if spot_show[spot]:
            imagebutton:
                xpos spot_coords[spot][0]
                ypos spot_coords[spot][1]
                xysize (110, 110)
                background Null()
                hover map_images[spot + "_h"]
                idle Null()
                #action [Function(set_spot_flag, spot, False, spot_coords[spot][0], spot_coords[spot][1]), Return()]
                action [Play("sound", "sfx/tap_full.ogg"), Function(set_spot_flag, spot, False, spot_coords[spot][0], spot_coords[spot][1]), Return(spot)]

    # spot marker
    showif not spot_settings["spot_moving"] and spot_settings["marker_visible"]:
        add "next_icon" at next_icon_bounce:
            pos(spot_settings["spot_old_x"]-next_x, spot_settings["spot_old_y"]-next_y)
    elif spot_settings["spot_moving"] and spot_settings["marker_visible"]:
        add "next_icon" at fast_move(spot_settings["spot_old_x"]-next_x, spot_settings["spot_old_y"]-next_y, spot_settings["spot_new_x"]-next_x, spot_settings["spot_new_y"]-next_y)
            #pos(636-next_x, 874-next_y)

screen map_main:
    $store.boss_map_dict = map_images_boss if store.is_boss_map else map_images_before_boss
    if store.draw_background:
        add store.boss_map_dict["bg_base_back"]
        add store.boss_map_dict["bg_crystal"] at map_pulse_transform:
            pos(753, 358)
        add store.boss_map_dict["bg_obj_01"] at map_building_transform(0.4):
            pos(637,208)
        add store.boss_map_dict["bg_obj_03"] at map_building_transform(0.7):
            pos(588,375)
        add store.boss_map_dict["bg_obj_05"] at map_building_transform(0.2):
            pos(583,621)
        add store.boss_map_dict["bg_obj_06"] at map_building_transform(0.8):
            pos(1189,459)
        add store.boss_map_dict["bg_obj_08"] at map_building_transform(0.5):
            pos(1089,266)
        add store.boss_map_dict["bg_obj_09"] at map_building_transform(0.3):
            pos(1002,735)
        add store.boss_map_dict["bg_particle"] at map_building_transform(0):
            pos(488, 231)

        add store.boss_map_dict["bg_obj_10"] at map_move_transform(1, 0.9):
            pos(641, 17)
        add store.boss_map_dict["bg_obj_11"] at map_move_transform(4, 0.4):
            pos(302, 285)
        add store.boss_map_dict["bg_obj_12"] at map_move_transform(2, 0.5):
            pos(1227, 58)
        add store.boss_map_dict["bg_obj_13"] at map_move_transform(3, 0.2):
            pos(780, 946)
        
        if not store.is_boss_map:
            add map_images_before_boss["bg_hand"]:
                pos(268,125)

        add store.boss_map_dict["bg_obj_14"] at map_move_transform(8, 0.2):
            pos(459, 326)
        add store.boss_map_dict["bg_obj_15"] at map_move_transform(5, 0.7):
            pos(1463, 623)
        add store.boss_map_dict["bg_obj_16"] at map_move_transform(3, 0.1):
            pos(1456, 322)
        
        add store.boss_map_dict["fg_particle"] at map_particle_transform(0.0, 0.75)
        add store.boss_map_dict["fg_particle_flip"] at map_particle_transform(0.75, 0.0)

        for spot in spot_show.keys():
            if spot_show[spot] and not spot_dark and (not store.is_boss_map or spot == "spot_10808"):
                image map_images["label_" + spot]:
                    pos(spot_coords[spot][0]-46, spot_coords[spot][1]+130)
    

            if spot_zoom == spot and spot_zooming and not spot_dark:
                add map_images[spot + "_h"] at spot_zoom_in:
                    pos(spot_coords[spot][0] + idiff, spot_coords[spot][1] + idiff)

            if store.is_boss_map and spot != "spot_10808":
                if spot_show[spot] and not spot_dark:
                    imagebutton:
                        xpos spot_coords[spot][0]
                        ypos spot_coords[spot][1]
                        xysize (110, 110)
                        background map_images[spot]
                        hover map_images[spot + "_h"]
                        idle Null()
                        action NullAction()
                        at transform:
                            alpha 0.5

                if spot_show[spot] and spot_dark:
                    imagebutton:
                        background map_images[spot + "_h"]
                        hover Null()
                        idle Null()
                        pos(spot_coords[spot][0], spot_coords[spot][1])
                        action [Play("sound", "sfx/tap_denied.ogg")]
                        xysize(110, 110)
                        at transform:
                            alpha 0.5
            else:
                if spot_show[spot] and not spot_dark:
                    imagebutton:
                        xpos spot_coords[spot][0]
                        ypos spot_coords[spot][1]
                        xysize (110, 110)
                        background map_images[spot]
                        hover map_images[spot + "_h"]
                        idle Null()
                        action NullAction()

                if spot_show[spot] and spot_dark:
                    imagebutton:
                        background map_images[spot + "_h"]
                        hover Null()
                        idle Null()
                        pos(spot_coords[spot][0], spot_coords[spot][1])
                        action [Play("sound", "sfx/tap_denied.ogg")]
                        xysize(110, 110)

        if draw_big_spot:
            add "ui/blue_overlay_dark.png" at linear_fade(0.0, 0.8, 0.08)
            add map_images[big_spot_node + "_b"] at linear_fade(0.0, 0.8, 0.08):
                pos(600, 315)
                xsize 300
                ysize 300
            add map_images["label_" + big_spot_node] at linear_fade(0.0, 0.8, 0.08):
                pos(600, 315+300)
                xsize 300
                ysize 300/(228/46)

image next_icon = "ui/next_icon.png"