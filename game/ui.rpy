transform page_icon_transform:
    xpos 1710
    ypos 955
    ease 0.5 ypos 975
    ease 0.5 ypos 955
    repeat

transform loading_transform_in:
    xpos 1400
    ypos 875
    alpha 0.00
    easein 0.25 alpha 1.00

transform loading_bar_transform_in:
    xpos 0
    ypos 1020
    alpha 0.00
    easein 0.25 alpha 1.00

transform loading_transform_out:
    easein 0.1 alpha 0.00

image loading animated:
    "ui/loading_1.png"
    pause 0.5
    "ui/loading_2.png"
    pause 0.5
    "ui/loading_3.png"
    pause 0.5
    "ui/loading_4.png"
    pause 0.5
    repeat

image loading_bar = "ui/white_line.png"

init -1 python:
    def clear_scene():
        renpy.hide("page_icon", layer="screens")
        renpy.restart_interaction()

    def start_scene():
        renpy.windows.hide()

    def char_callback(event, **kwargs):
        if event == "show":
            renpy.hide("page_icon", layer="screens")
            renpy.restart_interaction()
        elif event == "slow_done" or event == "end":
            renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
            renpy.restart_interaction()

    def show_loading():
        renpy.show("loading animated", at_list=[loading_transform_in], layer="ontop")
        renpy.show("loading_bar", at_list=[loading_bar_transform_in], layer="ontop")
    def hide_loading():
        renpy.show("loading animated", at_list=[loading_transform_out], layer="ontop")
        renpy.show("loading_bar", at_list=[loading_transform_out], layer="ontop")

    def play_video(name):
        if not renpy.emscripten:
            renpy.movie_cutscene(name)
            return
        import emscripten
        emscripten.run_script("delete window._renpy_finished_video") # remove flag
        emscripten.run_script("play_video(\"" + name + "\")")
        while 1:
            cmd = emscripten.run_script_string("window._renpy_finished_video") # set when video is finished
            if len(cmd) == 0: # not been set yet
                if (renpy.pause(0.1)):
                    return # return if user clicks manually (i.e. video broke), otherwise loop
            else:
                emscripten.run_script("delete window._renpy_finished_video") # remove flag
                return

image page_icon = "ui/page_icon.png"