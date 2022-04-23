label story_644_0:
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["644_0"]])

    $store.draw_big_spot = True

    drake_2 normal "Feast upon the accumulated gold and riches, you say...?"
    drake_2 joy "Gold! Riches! I can't very well ignore those now, can I?"
    drake_2 joy "In all ages and cultures, such straightforward treasures have always been pillaged."
    drake_2 normal "In other words, this is our forté."
    drake_2 "You're gonna have to hand it all over, your life included, got it?"
    drake_2 normal "I am fully aware of how impudent I'm being here, having just arrived and all."
    drake_2 "But it is what it is, no? After all, we're pirates!"
    pirate_1 normal "Whew! Our big sis's super cool───!"
    drake_2 joy "Yeah, we'll do this as merrily as usual, you swabbies!"
    drake_2 joy "We'll do what we've always done, no matter who or what our enemy is!"
    drake_2 joy "We'll pillage and drink and raise hell!"
    pirates_1 normal "You can say that again, Boss! We're the crew of the Golden Hind!"
    pirates_1 normal "We'll follow you anywhere, sis!! Woo-hoo!!"
    merlin_2 shy "Woo-hoo! Playing along like this once in a while isn't too bad!"
    first_hassan_2 normal "......"
    mash_3 shy "W-woo-hoo! Captain Drake and her pirate crew are in good spirits!"
    mash_3 anger "A miracle's unfolding here too───there's more than one pirate galleon here, Master!"
    pirate_1 normal "Woah! There's another ship portside!"
    mash_3 6 "That's...the Queen Anne's Revenge!"
    drake_2 normal "Heh, is that so? So he's here too, is he?"
    drake_2 "A pain in the ass he may be, but you can count on him."
    drake_2 shout "Heeey, Teach! Can you hear me!? What'll it be?"
    blackbeard_3 joy "Hmph. The one who fells you shall be none other than I..."
    blackbeard_3 joy "I couldn't possibly let someone else take up that role, now can I───"
    atalante_1 normal "That's enough of that. Steer properly or else we'll end up ramming that pillar of flesh."
    blackbeard_3 shout "Fine, fine! Cat-ears here has a rough way of treating her captain!"
    blackbeard_3 anger "Alright, boyos! Keep pace with the ha──Drake's ship!"
    blackbeard_3 anger "Bold of you to steal a pirate's treasure!"
    blackbeard_3 "I don't care whether you're a demonic beast or a devil───"
    blackbeard_3 anger "Go and regret in hell ever having laid hands on this great pirate Blackbeard's treasure!"
    drake_2 joy "Well, well, looks like that oaf's all fired up! Listen up, boys, don't you dare fall behind!"
    drake_2 shout "If we end up crashing and burning before him,"
    drake_2 "you lot are gonna be scrubbing the head in hell for a lifetime!"
    pirates_1 normal "Aye-aye, big sis!"
    drake_2 shout "Cannons on the ready, Golden Hind!"
    blackbeard_3 shout "Prep those cannons, Queen Anne's Revenge!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False

label story_644_1:
    # loading screen
    $ preloadImages (loading_images["10803"] + music_to_download["644_1"])
    # music
    play music "audio/map_okeanos_intro.ogg" noloop
    queue music "audio/map_okeanos_loop.ogg" loop
    show bg loading_03 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["644_1"]] + [background_images[l] for l in backgrounds_to_download["644_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg stormy_seas_2 with black_fade_in
    pause 1.0

    mash_3 anger "Incoming message from Chaldea!"
    mash_3 "It seems like the reconstructed cannon has successfully been materialized!"
    merlin_2 joy "Oh, we can use this! Well aren't you capable of some interesting things?"
    merlin_2 normal "Taking Chaldea's records of the Golden Hind and materializing it in a fluid etheric mass, hm?"
    merlin_2 normal "Hmm. I see, I see."
    drake_2 normal "Eh?"
    drake_2 sorrow "This cannon...looks an awful lot like ours, don't it?"
    drake_2 sorrow "Is it from the same gunsmith? Or could it...no, it couldn't be."
    pirate_1 normal "Haah, haah, haah...Cap'n, all our gunports're full up."
    pirate_1 normal "Don't look like we're missin' any."
    drake_2 normal "Well, don't that beat all? Seriously takes a load off my mind."
    drake_2 normal "It's a pain in the ass havin' to keelhaul your own crew before a battle."
    pirate_1 normal "Heh. Don't have to tell me!"
    merlin_2 normal "..."
    merlin_2 normal "Hey Mash, Master of Chaldea. Something just occurred to me."
    merlin_2 normal "If you taught the 21st-century definition of copy protection and piracy to these genuine pirates..."
    merlin_2 joy "What do you think would──mmmph."
    mash_3 14 "P-p-please excuse me, Merlin, but please shut up for now!"
    mash_3 14 "We really don't need you to go down that train of thought...!"
    first_hassan_2 sorrow "... (reads the mood and keeps quiet.)"

    $clear_scene()
    show bg boss_03 with Dissolve(2.0)
    pause 1.0

    drake_2 shout "Hey, what are you fussin' about over there?"
    heracles_1 shout "(RRRRRRRrrrrrrrrrrRRRRRRRRRR)"
    drake_2 shout "Gah, my ears! Wait, was that the legendary hero himself!?"
    drake_2 joy "Sorry about that! I'd be a damned fool to turn down help from you!"
    medea_lily_1 shout "I am here as well! This time, I too shall offer my support!"
    pirates_1 normal "!?"
    pirates_1 normal "Aaaaah! The wiiiiitch!"
    medea_lily_1 sorrow "Ah..."
    medea_lily_1 normal "Um, no! It's okay! For whatever reason, I don't have that intense desire this time,"
    medea_lily_1 normal "and because Lord Jason has asked me and Heracles to take care of you,"
    medea_lily_1 joy "both Heracles and I are on your side!"
    heracles_1 shout "(RRRRRRRrrrrrrrRRRRRRR)"
    drake_2 normal "Well, well. Looks like we're gonna get along."
    drake_2 normal "All right! We've got the legendary Argonauts on our side!"
    drake_2 shout "Now this is what I'm talkin' about! Listen up, you dogs!"
    drake_2 "Don't underestimate her just because she looks like a princess!"
    drake_2 shout "Little Miss Witch here is one of the original pirates!"
    drake_2 "She went on the hunt for the first hidden treasure!"
    drake_2 shout "There's no room for poor manners here──and of course, the rudest thing you can do is lose!"
    pirates_1 normal "AYE-AYE, CAP'N! AYE AYE, MISS WITCH!"
    medea_lily_1 shy "U-um...I'll do my best!"
    blackbeard_3 sorrow "Ooh, seems like they're getting fired up over there. Gettin' kind of jealous."
    atalante_1 normal "Are you displeased with me, Captain?"
    blackbeard_3 shout "Oh no no no no no, not at all! Now let's get rolling!"
    drake_2 shout "Hey! Don't let Teach and his crew steal all the glory!"
    first_hassan_2 shout "───Demon Beast Incarnadine, offer up thy head!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_644_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["644_4"]] + [background_images[l] for l in backgrounds_to_download["644_4"]] + music_to_download["644_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    show bg boss_03_full with black_fade_in
    pause 1.5
    play sound "sfx/desummon.ogg"
    scene black with wipedown
    pause 2.0
    show bg calm_seas with black_fade_in

    play music "audio/map_okeanos_intro.ogg" noloop
    queue music "audio/map_okeanos_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
    merlin_2 joy "The Third Demon Beast Incarnadine has been silenced!"
    blackbeard_3 joy "Whew. Ended up taking this just a wee bit seriously."
    blackbeard_3 "Surely there's no need to even mention who the MVP is!"
    atalante_1 normal "That would be Heracles. Although that skull man's skill with a greatsword is a sight to behold."
    atalante_1 normal "I certainly would not call it uncontested, you know?"
    blackbeard_3 normal "..."
    atalante_1 normal "What's wrong, Teach?"
    blackbeard_3 sorrow "No, I'm...actually depressed right now, please leave me be..."
    atalante_1 normal "?"
    drake_2 joy "Not too shabby, Teach! Quite daring by your standards, I'd say!"
    drake_2 joy "I like it. Where'd you learn to steer like that?"
    blackbeard_3 sorrow "Hey, hag...! Where do you get off spitting lines like that at a man when he's down!?"
    drake_2 anger "Who the hell are you calling a hag?"
    blackbeard_3 shout "───Blegh."
    mash_3 14 "Oh! Blackbeard got...flattened...!"
    merlin_2 joy "Ahahahaha. How nice, it almost makes me want to rest on my laurels."
    merlin_2 normal "But we've got to press forward. Mash, Master."
    first_hassan_2 normal "───Let us be off."
    drake_2 normal "Woah, are you going already? I guess I've got to give at least one gun salute."
    drake_2 joy "Stay safe, Chaldeans!"
    medea_lily_1 joy "Take care!"
    pirates_1 normal "Make sure to stay alive, you hear me!? ───See ya later!"
    
    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop