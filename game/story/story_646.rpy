label story_646_0:
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["646_0"]])

    $store.draw_big_spot = True

    nightingale_2 anger "Pathogenic bacterium again...?"
    nightingale_2 anger "Their extermination is truly quite an ordeal. There is no other way but to change the world."
    scathach_2 normal "Oh, don't say that. If we're overcome here, then there is no hope for the Human Order."
    scathach_2 normal "Besides, it doesn't appear such a surgical approach is necessary."
    scathach_2 joy "Look───the first responders are already here!"
    mash_3 anger "Master, we've reached the fifth domain!"
    mash_3 anger "Nightingale! Scathach!"
    sita_2 joy "I'm here as well, Mash!"
    mash_3 joy "Oh, Sita's here too!"
    merlin_2 joy "Hey, it's been a while since I've seen the three of you. Good to see you're all still doing well!"
    sita_2 joy "Yes, and you too, Merlin!"
    scathach_2 joy "Well, what do you think now, Florence Nightingale?"
    nightingale_2 joy "You appear to have been correct... Very well, we will settle for symptomatic treatment this time."
    sita_2 shout "Now, let us sally forth! Do not fear death nor pain!"
    sita_2 shout "For the Angel of Mercy is on our side!"
    sita_2 shout "The angel who hauls you up by the collar, no matter if you may be dying or on the way to Hell!"
    nightingale_2 joy "If it encourages you all, then I shall bear that moniker for now."
    nightingale_2 normal "Ahem..."
    nightingale_2 shy "Though, I must confess, I do find it rather embarrassing───"
    scathach_2 joy "Hahahahaha! Look, the Angel is blushing!"
    first_hassan_2 joy "Thou truly art a lovely flower. No wonder pagans mistook you for an angel."
    nightingale_2 9 "!?"
    nightingale_2 normal "The gentleman over there...this is the first time I've had the pleasure of meeting him."
    nightingale_2 normal "And yet I feel like I've seen him before somehow...why is that?"
    first_hassan_2 normal "Thou art the flower that grows alongside death. Therefore, thou mayest feel familiar with it."
    first_hassan_2 normal "But that is but an illusion."
    first_hassan_2 normal "Thy hands are for the sake of preserving life."
    nightingale_2 9 "O-of course... What a mysterious individual..."
    scathach_2 anger "───Now then, let us bring down this poor shade."
    scathach_2 anger "Poor fool with no idea what it truly is."

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False

label story_646_1:
    # loading screen
    $ preloadImages (loading_images["10805"] + music_to_download["646_1"])
    # music
    play music "audio/map_america_intro.ogg" noloop
    queue music "audio/map_america_loop.ogg" loop
    show bg loading_05 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["646_1"]] + [background_images[l] for l in backgrounds_to_download["646_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg america_night with black_fade_in
    pause 1.0

    cu_chulainn_alter_1 normal "Wait."
    cu_chulainn_alter_1 normal "This is my prey, Master."
    scathach_2 shout "...!"
    mash_3 6 "Master, look! It's..."
    mash_3 shout "───The Mad King, Cú Chulainn Alter. Our final enemy in the Fifth Singularity!"
    mash_3 6 "But he doesn't appear hostile towards us now. What's going on!?"
    scathach_2 normal "Even you showed up...I have to say, even I didn't expect this."
    scathach_2 normal "A miracle may be occurring, but how dare you stir from your throne."
    cu_chulainn_alter_1 normal "It's only natural that after a defeat, the loser goes over to the winner's side."
    cu_chulainn_alter_1 normal "Forcing your own way through without letting others do the same is just hypocrisy."
    cu_chulainn_alter_1 normal "Even if it's through mutual hate or simply killing each other, bonds once made can't be broken."
    cu_chulainn_alter_1 normal "At the very least I can do what I'm supposed to. That's all."
    cu_chulainn_alter_1 joy "I told you already, that shadow is my prey."
    scathach_2 sorrow "I see... Well then, for now I will refrain from asking why."
    scathach_2 normal "But how do you think Medb would feel about this?"
    scathach_2 normal "After all, she created you to rule over that Singularity."
    scathach_2 normal "Would she be pleased or displeased to see you doing this?"
    cu_chulainn_alter_1 normal "Who knows... She could be mad or happy."
    scathach_2 normal "!"
    scathach_2 joy "Yeah. It sure seems that way."
    scathach_2 anger "Well...sorry to hold you up, O Mad King of Shadows!"
    cu_chulainn_alter_shadow_1 shadow "──────────"    
    scathach_2 shout "Now, on to the extended final battle of the second American Civil War!"
    scathach_2 "I wish all you great heroes here good hunting!"
    karna_2 normal "Naturally..."
    arjuna_2 normal "Of course..."
    arjuna_2 normal "Karna... Did you ever think a day like this would come?"
    arjuna_2 normal "Not just that we would fight as partners───together..."
    arjuna_2 normal "But that we would do so in order to save something."
    karna_2 sorrow "I knew it would come someday, but I did not know when."
    karna_2 sorrow "I thought it might take one or two thousand years,"
    karna_2 "until the moon and sun washed away our feelings..."
    arjuna_2 joy "You're right. Who would have thought it would come so soon!"
    arjuna_2 joy "───But this is fine..."
    arjuna_2 anger "I'll suppress my feelings of hatred and competitiveness with you."
    arjuna_2 sorrow "For now..."
    karna_2 joy "Is that so? If anything, I was rather looking forward to our rivalry here."
    arjuna_2 anger "───What?"
    scathach_2 shout "Don't be so hasty, Arjuna! Karna merely wants to compete with you here!"
    scathach_2 normal "Isn't that right?"
    karna_2 sorrow "Yes... It appears I misspoke."
    arjuna_2 normal "───I see."
    scathach_2 sorrow "In this world, your desire to clash with each other may not come to pass."
    scathach_2 normal "But just endure for now. And continue to do so as we move on."
    arjuna_2 normal "Queen of the Land of Shadows. I may not understand what you say..."
    arjuna_2 normal "But I shall agree for now. Therefore, Karna,"
    arjuna_2 normal "I'll express my hatred and jealousy towards you through exceeding your body count!"
    arjuna_2 shout "Now, ready your spear!"
    karna_2 joy "Of course. And you nock your arrows, Arjuna."
    cu_chulainn_alter_shadow_1 shadow "RRRRRRRRrrrrrrrRRRRRRRRR!"
    scathach_2 anger "Hah!"
    cu_chulainn_alter_1 shout "───Come!"
    mash_3 shout "Demon Beast Incarnadine incoming, along with hostile Shadow Servants!"


    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_646_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["646_4"]] + [background_images[l] for l in backgrounds_to_download["646_4"]] + music_to_download["646_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 1.0
    show bg dustbowl_town with black_fade_in

    play music "audio/map_america_intro.ogg" noloop
    queue music "audio/map_america_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
 
    mash_3 anger "───Hostile Shadow Servant, annihilated! The fifth Demon Beast Incarnadine has been silenced!"
    scathach_2 joy "Good..."
    nightingale_2 anger "The pathogen has been excised. However, it is little more than symptomatic treatment."
    nightingale_2 anger "We may have succeeded in opening the gate of this domain,"
    nightingale_2 "but we are far from a curative treatment."
    nightingale_2 anger "Now then, hurry along. Should you dawdle, the gate will close once more."
    nightingale_2 shout "But first of all, we must excise the real pathogen───the root cause!"
    merlin_2 shout "How much do you even know!?"
    merlin_2 "Is this shrewdness a trait unique to those with a high level of Madness Enhancement?"
    merlin_2 anger "In any case, she's right. Let's hurry up, Mash. You too, Master of Chaldea!"
    sita_2 joy "Go on ahead! And please be careful!"
    arjuna_2 normal "The path has been paved. You are free to press forward!"
    karna_2 joy "───Go now, keep moving forward!"
    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop