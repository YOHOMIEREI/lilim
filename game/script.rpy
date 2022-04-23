# The script of the game goes in this file.
# The game starts here.

default next_scene = None
default is_during_raid = False
default is_finished = False

label main_menu:
    return

label start:
    $ fade_in = Fade(0.0, 0.0, 1.0, color="#000")
    $ flash_black = Fade(1.0, 0.0, 0.0, color="#000")
    menu:
        system "Skip ahead?"
        "Skip to America":
            $store.spot_show = {
                "spot_10801": True,
                "spot_10802": True,
                "spot_10803": True,
                "spot_10804": True,
                "spot_10805": True,
                "spot_10806": False,
                "spot_10807": False,
                "spot_10808": False
            }
            $setup_at("spot_10805")
            $ clear_scene()
            $next_scene = "spot_10805"
            $ preloadImages(list(map_images.values()) + (list(map_images_boss.values()) if is_boss_map else list(map_images_before_boss.values())) + ["map_intro.ogg", "map_loop.ogg"])
            jump map_no_video
        
        "Skip to Babylon":
            $store.spot_show = {
                "spot_10801": True,
                "spot_10802": True,
                "spot_10803": True,
                "spot_10804": True,
                "spot_10805": True,
                "spot_10806": True,
                "spot_10807": True,
                "spot_10808": False
            }
            $setup_at("spot_10807")
            $ clear_scene()
            $next_scene = "spot_10807"
            $ preloadImages(list(map_images.values()) + (list(map_images_boss.values()) if is_boss_map else list(map_images_before_boss.values())) + ["map_intro.ogg", "map_loop.ogg"])
            jump map_no_video

        "Skip to Final Battle":
            $store.spot_show = {
                "spot_10801": True,
                "spot_10802": True,
                "spot_10803": True,
                "spot_10804": True,
                "spot_10805": True,
                "spot_10806": True,
                "spot_10807": True,
                "spot_10808": True
            }
            $setup_at("spot_10808")
            $store.is_boss_map = True
            $ clear_scene()
            $next_scene = False
            $ preloadImages(list(map_images.values()) + (list(map_images_boss.values()) if is_boss_map else list(map_images_before_boss.values())) + ["map_intro.ogg", "map_loop.ogg"])
            jump map_no_video

        "Start from the beginning":
            jump start_2
label start_2:
    $ clear_scene()
    system "Please report bugs to the Rayshift Discord server.\n{a=https://discord.gg/YTdcKAnGBn}https://discord.gg/YTdcKAnGBn{/a}"
    system "If you're running slow in Chrome, try Firefox instead, or make your browser window smaller."
    system "Turn on or off music in the menu."
    $ renpy.choice_for_skipping()
    $ clear_scene()

    
    with fade_in
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["intro"]] + [background_images[l] for l in backgrounds_to_download["intro"]])

    show bg grail_mud with black_fade_in
    play music "sfx/windy_ambience.ogg" fadein 2.0 loop

    queen_draco_1 joy "Welcome, Masters of Chaldea."
    queen_draco_1 normal "To this special performance I have prepared for you."
    queen_draco_1 joy "Here you can witness the final chapter unfold from your own abode."
    queen_draco_1 normal "Remember to save your game,\nusing the buttons at the bottom."
    queen_draco_1 shout "Now come, Master of Chaldea."
    queen_draco_1 shout "Your demise at the banquet of depraved civilization awaits!"

    $ renpy.choice_for_skipping()
    $ clear_scene()

    stop music fadeout 3.0
    scene black with black_fade_out
    pause 0.1

    
    with flash_black


    jump map

transform linear_fade(start, to, t):
    alpha start
    linear t alpha to

label map:
    $ preloadImages(list(map_images.values()) + (list(map_images_boss.values()) if is_boss_map else list(map_images_before_boss.values())) + ["map_intro.ogg", "map_loop.ogg"])
    $ play_video("video/LilimIntro.webm")

label map_no_video:
    $ clear_scene()
    $ flash = Fade(.30, 0, 4.0, color="#fff")


    $ renpy.choice_for_skipping()
    show screen map_main(_layer="map")
    scene

    play music "audio/map_intro.ogg" noloop
    queue music "audio/map_loop.ogg" loop

    $ renpy.force_autosave()
    call screen pause_screen with flash
    $ next_scene = _return
    jump post_flash

label menu_loop:
    $ preloadImages(list(map_images.values()) + (list(map_images_boss.values()) if is_boss_map else list(map_images_before_boss.values())))
    $ store.draw_big_spot = False
    $ store.draw_background = True

    $ flash2 = Fade(0, 1.0, 1.25, color="#000")
    with flash2

label menu_nofade_loop:

    $ store.spot_dark = False
    if renpy.music.get_playing() is not None:
        if not renpy.music.get_playing() == "audio/map_intro.ogg" and not renpy.music.get_playing() == "audio/map_loop.ogg":
            play music "audio/map_intro.ogg" noloop
            queue music "audio/map_loop.ogg" loop
    else:
        play music "audio/map_intro.ogg" noloop
        queue music "audio/map_loop.ogg" loop
    $ renpy.force_autosave()

    if is_finished:
        play sound "sfx/tap_full.ogg" noloop
        system "Thanks for playing!"
        system "If you want to read FGO Mobile (JP) in English, use:\n{a=https://github.com/rayshift/translatefgo}https://github.com/rayshift/translatefgo{/a}"
        system "Support us by joining our Discord server:\n{a=https://discord.gg/YTdcKAnGBn}https://discord.gg/YTdcKAnGBn{/a}"
        system "You can also support us by sharing this app with others!"
        system "See you again for LB6.5/7!"
        $store.is_finished = False
        $ clear_scene()
        $ renpy.choice_for_skipping()


    call screen pause_screen
    $ next_scene = _return

label post_flash:
    #if next_scene and next_scene == "spot_10808":
    #    captain_1 normal "This node hasn't been released yet.\nCheck back on the 21st!"
    #    system "(want to be notified on release? we have a discord server:\n{a=https://discord.gg/YTdcKAnGBn}https://discord.gg/YTdcKAnGBn{/a})"
    #    $clear_scene()
    #    jump menu_nofade_loop
    if next_scene and next_scene == "spot_10802":
        jump story_643_0
    elif next_scene and next_scene == "spot_10803":
        jump story_644_0
    elif next_scene and next_scene == "spot_10804":
        jump story_645_0
    elif next_scene and next_scene == "spot_10805":
        jump story_646_0
    elif next_scene and next_scene == "spot_10806":
        jump story_647_0
    elif next_scene and next_scene == "spot_10807":
        jump story_648_0
    elif next_scene and next_scene == "spot_10808":
        jump story_649_0
    else:
        jump story_642_0
    $ clear_scene()
    hide bg
    jump menu_loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

image bg blue_overlay = "ui/blue_overlay_dark.png"
define black_fade_out = Fade(2.0, 1.0, 0)
define black_fade_out_short = Fade(1.0, 1.0, 0)
define black_fade_in = Fade(0.0, 0, 2.0)
define black_fade_in_short = Fade(0.0, 0, 1.0)

transform fade_test(timet=1.0, x=960, z=0.80):
    alpha 0.00
    xcenter x yoffset 0
    easein timet alpha 1.00

transform fade_test_out(x=960, z=0.80):
    alpha 1.00
    xcenter x yoffset 0
    easein 2.0 alpha 0.00

transform LiveDissolve(spriteB, duration=2.0):
    DynamicImage(spriteB) with Dissolve(duration, alpha=True)