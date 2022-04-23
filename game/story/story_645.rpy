label story_645_0:
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["645_0"]])

    $store.draw_big_spot = True

    mordred_2 sorrow "Yeah... There's an end to everything."
    mordred_2 sorrow "That majestic castle, shining proudly, will collapse."
    mordred_2 "Those armored knights bearing arms will die all the same too."
    mordred_2 anger "Even the world will end someday."
    mordred_2 "But not at the hands of a Demon Beast Incarnadine. Not at all."
    mordred_2 anger "The end of the world ain't a lousy spectacle like this without a soul to attend to it."
    mordred_2 anger "On the contrary, it's the end for you bastards. You've already had your fill, haven't you?"
    mordred_2 shout "Then it's the end for you. I'll put you out of your misery!"
    mash_3 anger "...!"
    mash_3 anger "We've reached the fourth domain! Mordred has already commenced her assault!"
    mash_3 anger "However───"
    merlin_2 anger "There are two Demon Beast Incarnadines here. A twin type one, more specifically."
    merlin_2 anger "One of them's the Control Tower and the other one's the assault apparatus."
    merlin_2 anger "You can't afford to waste your magical energy carelessly."
    merlin_2 "Of the two, you'll need to accurately strike at the Control Tower."
    mordred_2 shout "Shut it! Who the hell are you!?"
    mordred_2 shout "I just have to pulverize both of them!"
    tamamo_no_mae_2 sorrow "Oh, I wonder about that."
    tamamo_no_mae_2 "It's a coin toss as to whether you're wasting your time if you charge in recklessly, you know?"
    mordred_2 normal "So you mean there's a fifty-fifty chance that I'll hit the jackpot?"
    mash_3 joy "Mordred, Tamamo-no-Mae!"
    mordred_2 joy "Hey, Mash! The Chaldean Master's along for the ride too, eh!?"
    merlin_2 joy "(Grinning)"
    mordred_2 normal "Hm."
    mordred_2 anger "You're...not Merlin...are you...?"
    mordred_2 anger "That floweriness makes you feel kind of similar..."
    mordred_2 sorrow "But you're a woman and all───"
    merlin_2 joy "Ahahahahaha!"
    merlin_2 joy "Close but no cigar! I'm not that person you're familiar with, I'm Merlin from a different timeline."
    merlin_2 joy "Needless to say, I'm not male. Although I am the Magus of Flowers───"
    merlin_2 joy "Your flowery big sis who's been cheering you on this whole time as you strived for your ideals!"
    mordred_2 shout "Huh?"
    tamamo_no_mae_2 normal "Let's think of her as a relative of Merlin's, shall we?"
    tamamo_no_mae_2 normal "Nonetheless, Mash and the Master of Chaldea. It's been a while,"
    tamamo_no_mae_2 joy "and you've made quite a few new companions───"
    merlin_2 joy "Fufu."
    first_hassan_2 normal "..."
    tamamo_no_mae_2 joy "It would appear you've become acquainted with quite a lot of heavy hitters."
    tamamo_no_mae_2 "After all, they both qualify for the position of Grand."
    tamamo_no_mae_2 shout "And...eh?"
    tamamo_no_mae_2 shout "T-that person there! With the skull!"
    tamamo_no_mae_2 shout "He's not just qualified for the seat of Grand! He's already a Grand Heroic Spirit!"
    first_hassan_2 normal "I am indeed, O Radiant Tail Of The Heavens."
    first_hassan_2 "I am the Old Man of the Mountain, Hassan-i-Sabbah."
    tamamo_no_mae_2 shout "Mikon! C-could it be that you're the founder!?"
    merlin_2 joy "Indeed he is! After all, this battle is the climax!"
    merlin_2 joy "Where all worthy Heroic Spirits assemble!"
    mordred_2 normal "Hah. I don't know what you're babbling on about,"
    mordred_2 "but looks like you're some bigwig or something."
    mordred_2 "I'll fight alongside you and we'll see if you're all that."
    mordred_2 normal "We've got two enemies. One's the head and the other's like an extension of its hand."
    mordred_2 shout "That simplifies matters! We'll keep hitting and striking them!"
    mordred_2 shout "I'll say it again───we just have to pulverize the both of them!!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False

label story_645_1:
    # loading screen
    $ preloadImages (loading_images["10804"] + music_to_download["645_1"])
    # music
    play music "audio/map_london_intro.ogg" noloop
    queue music "audio/map_london_loop.ogg" loop
    show bg loading_04 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["645_1"]] + [background_images[l] for l in backgrounds_to_download["645_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg foggy_london with black_fade_in
    pause 1.0


    artoria_2 normal "──────Exactly so."
    artoria_2 normal "You speak truthfully, O Nameless Knight."
    mordred_2 shout "!"
    mash_3 6 "That's───"
    artoria_2 normal "I am but another what-if of myself, from beneath a different sky."
    artoria_2 normal "One that springs from holding the Holy Lance, on the verge of apotheosis,"
    artoria_2 normal "yet clinging to the slimmest of chances of remaining myself."
    artoria_2 normal "The possibility of retaining my identity while wielding the power of the Lance."
    artoria_2 "The possibility of accepting the curse of the Grail."
    artoria_2 sorrow "A version of myself unable to act as a king, as my nature is that of the storm."
    artoria_2 normal "That...is what I am."
    artoria_2 normal "Nothing more than a storm which ravages that which lies before me."
    mordred_2 shout "I have heard your words! Father──no, Storm King, leader of the Wild Hunt!"
    mordred_2 shout "You're the one who destroys everything! Even me!"
    mordred_2 "And especially those two Demon Beast Incarnadines!"
    artoria_2 anger "No. Today all that lies before me is the head of that beast."
    artoria_2 anger "I am blind to any Heroic Spirits attempting to save the world───"
    artoria_2 "Holy Lance, removing restraints."
    first_hassan_2 joy "Oh...?"
    merlin_2 joy "Hahahahaha! Behold, the light of the tower that anchors the ends of the world!"
    merlin_2 joy "You don't see this every day! Too bad for you, Beast VI!"
    merlin_2 joy "It's just too bad we're only at one of the heads, and not at the main body!"
    $clear_scene()
    stop music fadeout 1.0
    show bg foggy_london_2 with ImageDissolve(im.Tile("blindstile.png"), 1.25, 8)
    play music "audio/demon_pillar_intro.ogg" fadein 1.0 noloop
    queue music "audio/demon_pillar_loop.ogg" loop
    pause 1.0
    mordred_2 sorrow "..."
    tamamo_no_mae_2 sorrow "Mordred?"
    mordred_2 sorrow "Like this? On this battlefield? What a sick joke. Am I supposed to be thankful for this?"
    mordred_2 shout "Welp, it's gone so far it's actually refreshing! I'm finally fighting alongside Father!"
    mordred_2 shout "And we're finally on the same wavelength: just trash everything in front of us!"
    mordred_2 joy "If this is a dream, it's a freakin' amazing one! I'm gonna enjoy this to its fullest!"
    jack_2 normal "Are you happy to be with your Mummy?"
    mordred_2 normal "Yeah, I sure am."
    mordred_2 shout "Wait───that's my Father, not my mom!"
    jack_2 joy "(All smiles)"
    mordred_2 shout "Hey──you're Jack! What, have you manifested as our ally now?"
    mordred_2 joy "That's great! This doesn't happen a lot, so let's go smash some faces together!"
    jack_2 joy "Yeah!"
    mordred_2 shout "Now, let's rock and rooooooll!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_645_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["645_4"]] + [background_images[l] for l in backgrounds_to_download["645_4"]] + music_to_download["645_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    show bg boss_04_full with black_fade_in
    pause 1.5
    play sound "sfx/desummon.ogg"
    scene black with wipedown
    pause 2.0
    show bg clear_london with black_fade_in

    play music "audio/map_london_intro.ogg" noloop
    queue music "audio/map_london_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
    mash_3 anger "Fourth Demon Beast Incarnadine, patterns A and B have both been silenced!"
    mordred_2 sorrow "What...that's it?"
    mordred_2 sorrow "Aw man, what a letdown. I thought I'd finally be able to run amok with Father."
    mordred_2 normal "Ah, whatever. Was still a good fight."
    jack_2 joy "Yeah!"
    mash_3 joy "Yes!"
    tamamo_no_mae_2 normal "Well, I suppose. Speaking comparatively, of course."
    merlin_2 normal "Yep, yep."
    artoria_2 normal "..."
    first_hassan_2 normal "..."
    mordred_2 anger "Sheesh. Those two sure aren't happy."
    mordred_2 normal "Thanks, Mash. You too, Master of Chaldea."
    mordred_2 normal "Why I'm still here, or why records of what happened before are still around..."
    mordred_2 normal "I don't really get it at all, but I'm sure it's because of you two."
    tamamo_no_mae_2 joy "Why are you making it sound so final!? We aren't done here yet, you know!"
    tamamo_no_mae_2 normal "We'll take charge of this domain now, so please go on ahead."
    tamamo_no_mae_2 normal "And please be careful. The trials ahead will be just as taxing, or even more so──"
    jack_2 normal "They're strong, but that's okay. You can do it."
    mash_3 anger "Yes...!"
    merlin_2 normal "That's right. Even should a strong enemy block our way,"
    merlin_2 normal "that wouldn't stop Mash and Master's pace, would it?"
    merlin_2 joy "You guys know exactly what I mean, don't you? Fufufufu!"
    mordred_2 normal "Yeah, sure do..."
    tamamo_no_mae_2 normal "Well, so it goes. But be on your guard all the same!"
    artoria_2 normal "──Farewell."
    first_hassan_2 normal "──Mm."
    mash_3 joy "We're off! Now...let's keep going, Senpai!"
    
    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop