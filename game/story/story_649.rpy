label story_649_0:
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["649_0"]] + music_to_download["649_0"] + [background_images[l] for l in backgrounds_to_download["649_0"]])

    show bg lilim_1 with black_fade_in
    show beast_vis_1_big normal at fade_test
    pause 1.0
    play music "audio/draco_pre_intro.ogg" noloop
    queue music "audio/draco_pre_loop.ogg" loop

    beast_vis_1_big "Hnn───"
    beast_vis_1_big "You remain unbroken in spite of this ugly showing. You continue to struggle in the face of such desolation."
    show beast_vis_1_big joy
    beast_vis_1_big "And that is fine. For this is how you ought to be."
    show beast_vis_1_big 0
    beast_vis_1_big "Though it may be a feat the other Beasts are incapable of achieving, the “Human Order Annihilation” is little more than the main dish."
    beast_vis_1_big "A delicacy it may be, but not one I haven't tasted multiple times before."
    beast_vis_1_big "I have long since grown tired of its taste. I have but one desire that brings me joy───"
    show beast_vis_1_big joy
    beast_vis_1_big "That swell of splendor blessed by the masses. In the midst of the filth of greed that envelops the heavens,"
    show beast_vis_1_big 7
    beast_vis_1_big "a pitiful gem continues to shine regardless. To grasp it within my fingers."
    noah_qmark_3 silhouette "I swear, you and Draco are cut from the same cloth."
    noah_qmark_3 "Well, I suppose it's to be expected, since we're talking about the real thing and its aspect."
    noah_qmark_3 silhouette "However───it's precisely because you continue to lounge around like that!"
    noah_qmark_3 silhouette "That you snatch defeat from the jaws of victory like this!"
    mash_3 joy "This voice is...!"
    noah_3 normal "Of course! Who else but me would appear gallantly as a comrade in this place and time!"
    noah_3 shout "Chieftain of the survivors of the Great Flood, heir to the eldest survivor Utnapishtim!"
    noah_3 shout "The fair youth of salvation, Noah!"
    noah_3 "I have traversed the sea of blood, alongside the radiance of Zohar!"
    noah_3 joy "That said, I'm not much of a fighter."
    noah_3 "In exchange, I've brought a special helping hand along for a ride!"
    merlin_2 joy "Here it comes! You did it! Now that's what I'm talking about!"
    arthur_qmark_2 silhouette "Merlin..."
    arthur_qmark_2 silhouette "There's a lot I'd like to ask you, Merlin."
    arthur_qmark_2 silhouette "Why are you here in this world? Why did you send me to that distant world all alone?"
    arthur_qmark_2 silhouette "But I shall refrain for now. I've been informed of everything by Rider, Noah!"
    mash_3 anger "You're───"
    arthur_qmark_2 silhouette "It would seem I've barely made it in time."
    arthur_qmark_2 "Pleased to make your acquaintance, Chaldean Master of this world."
    arthur_qmark_2 silhouette "And Mash Kyrielight of this world! I am───"
    arthur_qmark_2 silhouette "I am one who hunts the Beast. The wanderer on a journey across the many worlds."
    arthur_qmark_2 normal "───My True Name is Arthur Pendragon!"
    mash_3 6 "!"
    mash_3 6 "Arthur Pendragon! The King of Knights sung of in Britain's legends, the Red Dragon!"
    arthur_2 anger "When L and R are both present, so too will S and G manifest under either sky..."
    arthur_2 anger "Everything is in accordance with Merlin's prophecy."
    arthur_2 "I have traversed many a world for this moment."
    arthur_2 8 "Know that the Holy Sword of the Planet will not let you escape───even if we are worlds apart."
    arthur_2 shout "That avarice! That pride!"
    arthur_2 shout "I shall close the curtains on them on this very day, at this very moment, at this very place!"
    arthur_2 shout "───Beast VI, Sodom's Beast!"



    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause(2.0)
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    #hide bg
    #$store.draw_background = False

label story_649_1:
    # loading screen
    $ preloadImages (loading_images["10808"] + music_to_download["649_1"])
    # music
    play music "audio/beastvis_intro.ogg" noloop
    queue music "audio/beastvis_loop.ogg" loop
    show bg loading_08 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["649_1"]] + [background_images[l] for l in backgrounds_to_download["649_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg lilim_2 with black_fade_in
    show beast_vis_1_big normal at fade_test
    pause 1.0

    first_hassan_2 normal "──────"
    first_hassan_2 normal "O beast of depravity. O dragon who partakes of filth from the golden grail."
    first_hassan_2 "The sound of that bell───"
    first_hassan_2 sorrow "Nay. The radiance of that star."
    first_hassan_2 "Have you witnessed it once more? With those gleaming childlike eyes of yours."
    beast_vis_1_big "───To think you would address me in that manner. You haven't changed, old man."
    show beast_vis_1_big 0
    beast_vis_1_big "Oh, I see it well enough... Radiant even in the midst of this foulness."

    first_hassan_2 normal "───That will do. O Knight of the Holy Sword, tis thy turn."
    arthur_2 joy "Yes!"
    arthur_2 shout "───{rb}Thirteenth seal, release{/rb}{rt}Seal Thirteen{/rt}! ───{rb}Round Table decision, start{/rb}{rt}Decision Start{/rt}!"
    merlin_2 anger "Two Grand Heroic Spirits plus the Knight of the Holy Sword,"
    merlin_2 "a Beast slayer who traverses the worlds."
    merlin_2 anger "The end is in sight. The Chaldea that you have preyed upon so many times now,"
    merlin_2 anger "will bare their fangs at you right at the very end! Go on, grumble and protest!"
    show beast_vis_1_big anger
    beast_vis_1_big "───Hmph. What a loathsome succubus you are."
    show beast_vis_1_big normal
    beast_vis_1_big "Mash Kyrielight. O stargazing knight."
    beast_vis_1_big "You claimed you would not avert your eyes from this future. That you would only fight against the evil that I am."
    show beast_vis_1_big 0
    beast_vis_1_big "I hereby ask of that pitifully innocent heart of yours."
    beast_vis_1_big "You said yourself that everything has an end."
    beast_vis_1_big "That much is true. However───"
    show beast_vis_1_big normal
    beast_vis_1_big "When all of creation disappears, who will be there to witness that end?"
    mash_3 6 "That's───"
    mash_3 sorrow "...that is..."

    $ clear_scene()
    $ renpy.choice_for_skipping()
    show beast_vis_1_big at fade_test_out
    pause 2.0
    hide beast_vis_1_big
    show bg final_boss with Dissolve(2.0)
    pause 2.0

    beast_vis_1_big "Yes. That is the epitome of sorrow. The epitome of anguish."
    beast_vis_1_big "I am the Evil that was born to deliver that sorrow."
    beast_vis_1_big "The Human Order, human history."
    beast_vis_1_big "You lot speak of it as though it were something of great importance."
    beast_vis_1_big "There is truth to those claims."
    beast_vis_1_big "After all, it has the strength to resist me right up to the very end like this."
    beast_vis_1_big "Since I possess magical energy of the First-Class Planetary Grade,"
    beast_vis_1_big "I am already an existence far above the likes of you."
    beast_vis_1_big "Then...it is none other than I,"
    beast_vis_1_big "who feasted upon the most prosperous city that reached the extremity of civilization,"
    beast_vis_1_big "who can lusciously savor it more than anyone else, down to the very last drop, no?"
    mash_3 6 "!"
    mash_3 14 "T-then, you're..."
    mash_3 14 "Out of curiosity───"
    mash_3 shout "The world───"
    beast_vis_1_big "What an inelegant way of phrasing it. Here's how you put it into words beautifully:"
    beast_vis_1_big "Desire!!"
    beast_vis_1_big "My greed and avarice! That is to say, I wish to “savor and consume more”!"
    beast_vis_1_big "Behold an Evil of Humanity,"
    beast_vis_1_big "the driving force behind the development of civilizations and their downfall!"
    beast_vis_1_big "Rejoice, children of Chaldea!"
    beast_vis_1_big "The world shall disappear now at the hands of my dearly insatiable gluttony!"
    beast_vis_1_big "And at the very end, in a barren, lifeless void, I shall proclaim thus:"
    $ clear_scene()
    pause 1.5
    beast_vis_1 sorrow "───“What a wonderful meal.”"
    mash_3 shout "!!"
    mash_3 shout "Right... Right, Master! We have to stop her!"
    mash_3 shout "Right here! Right now!"


    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 3.0
    pause 2.0
    scene black with black_fade_out
    $renpy.pause(1.0, hard=True)
    $ play_video("video/BeastSplash.webm")
    
    pause 2.0
    hide bg

default gender = "f"

label story_649_6:
    $ randomnum = renpy.random.randint(1,2)
    $ store.gender = "f" if randomnum == 1 else "m"
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["649_6"]] + [background_images[l] for l in backgrounds_to_download["649_6_" + gender]] + music_to_download["649_6"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.pause(1.0, hard=True)
    $ play_video("video/BeastDeath.webm")
    pause 1.0
    show bg ruins_day with black_fade_in

    play music "audio/ending_intro.ogg" noloop
    queue music "audio/ending_loop.ogg" loop
    $ renpy.choice_for_skipping()

    mash_3 6 "We...we did it..."
    mash_3 joy "We did it, Senpai! Yes, yes! We...!"
    mash_3 joy "...vanquished Beast VI/S...!"
    mash_3 joy "Last Order, completed! As of this moment, the Grand Order has concluded!"
    merlin_2 joy "Mash! Master!"
    merlin_2 joy "You did great, well and truly!"
    merlin_2 normal "I never even imagined that you would triumph without a single casualty."
    merlin_2 sorrow "I thought we'd lose one of you, like we did against the First Beast."
    merlin_2 normal "But it would seem my fears were unfounded."
    merlin_2 normal "That's a relief. After all, there is no Cath Palug in this world───"
    mash_3 normal "...?"
    merlin_2 normal "It's complicated, and you're better off not knowing about it anyway."
    merlin_2 normal "You'll soon be forgetting what you heard just now. I'm sorry. And thank you."
    merlin_2 joy "Let's celebrate, for starters! Thanks to your efforts, the Human Order of this world is saved!"
    first_hassan_2 normal "Hmm. The annihilation of the Human Order may have been averted, however..."
    merlin_2 normal "However?"
    first_hassan_2 normal "Gaze upon what lies behind you."
    merlin_2 joy "Heh, you're not going to scare me that easily───Oh."
    arthur_2 anger "Merlin..."
    merlin_2 sorrow "H-hey there, if it isn't my beloved Arthur! You're acting all tense, what's gotten into you?"
    arthur_2 shout "That's not the problem here! You've been playing up the recluse angle, Merlin!"
    arthur_2 shout "But if you can come out just like that,"
    arthur_2 "then there's no reason for me to continue wandering the worlds alone───"
    merlin_2 shout "A-www! You're putting me on the spot here!"
    merlin_2 joy "I was watching Mash and Master's journey,"
    merlin_2 "and while it may have been a harsh one it seemed fun nonetheless,"
    merlin_2 "and that's how it is!"
    arthur_2 shout "Because it seemed fun!?"
    arthur_2 anger "Ok...listen up Merlin. You know,"
    arthur_2 anger "I've been travelling the worlds in accordance with your prophecy,"
    arthur_2 "searching for L and R at that Chaldea from far away───"
    arthur_2 8 "There I kept awaiting the continuation of the prophecy, for portents of S and G. And yet..."
    arthur_2 shout "You intervened, an intervention unprophesied and unplanned. Just because it seemed fun!?"
    merlin_2 shout "Waahh, save me, Noah!"
    noah_3 joy "No, you reap what you sow. Go break a leg!"
    merlin_2 shout "Ugh~!"
    mash_3 anger "Incoming message from Chaldea───it says that our retrieval process is underway!"
    mash_3 13 "Yes... Well, unfortunate as it may be, this is where we bid you farewell."
    first_hassan_2 normal "Fear not, for fate already binds us."
    noah_3 normal "This need not necessarily be the final farewell."
    noah_3 "The same applies for those Heroic Spirits you have encountered in the Singularities thus far."
    noah_3 joy "We'll meet again someday! When the time comes!"
    mash_3 13 "Yes..."
    merlin_2 joy "Head home now, both of you. Hold your heads high."
    merlin_2 "After all, this is your momentous triumphant return!"
    mash_3 joy "Yes!"
    merlin_2 normal "Oh, that's right───I have one piece of good news for you."
    merlin_2 normal "The condition outside the Chaldea base appears to be in a once-in-a-year state right now."
    merlin_2 joy "That is to say, the blizzard has subsided! You really shouldn't miss this chance!"
    mash_3 6 "!"
    mash_3 joy "Then───is the sky really...?"
    merlin_2 normal "A special, blue sky."
    mash_3 joy "From our era, our Earth───"
    merlin_2 joy "(Smiling)"
    mash_3 joy "Yes... Yes! Master!"
    mash_3 joy "Let's go see that blue sky of ours!"
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.pause(1.0, hard=True)
    $ flash_white = Fade(2.0, 1.0, 2.0, color="#FFF")
    $ flash_white_slow = Fade(5.0, 1.0, 2.0, color="#FFF")
    transform sky_scroll_up():
        pause 9.0
        easeout 16 offset (0, 1180)

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    if gender == "f":
        show bg ending_f at sky_scroll_up with flash_white
    else:
        show bg ending_m at sky_scroll_up with flash_white
    play music "audio/credits.ogg" noloop
    $renpy.pause(14.0)
    scene white with flash_white_slow

    image creditscroll:
        alpha 0.0
        Text("{color=#000}Lilim Harlot{/color}")
        anchor (0.5, 0.0)
        pos (0.5, 0.5)
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 3.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Original Story: DELiGHTWORKS{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 5.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Translation:  zaszc\n                   Gaius\n                   fumei\n                   Porkslope\n                   Yusuke{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 5.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Development: Neo (Rayshift.io){/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Testing: MaxAkito{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Music & Artwork: DELiGHTWORKS{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Ending Song: milet「Prover」{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Made with renpy 7.5 and caffeine.\n\nSource code now available on GitHub ({a=https://github.com/rayshift/lilim-harlot}rayshift/lilim-harlot{/a}).{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 5.0
        linear 1.0 alpha 0.0

        Text("{color=#000}This is a fanmade app.\n\nAll rights reserved by the original copyright owners.{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

        Text("{color=#000}Thank you for playing.{/color}")
        xalign 0.5
        yalign 0.5
        linear 1.0 alpha 1.0
        pause 6.0
        linear 2.0 alpha 0.0

    show creditscroll
    pause 65
    hide creditscroll
    scene black with black_fade_out

    $play_video("video/LilimEnding.webm")
    $store.is_boss_map = False

    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 2.0
    $store.is_finished = True
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop