label story_643_0:
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["643_0"]])

    $store.draw_big_spot = True

    nero_2 sorrow "..."
    nero_2 sorrow "What am I doing here...?"
    nero_2 sorrow "Where am I? Just now, I was..."
    nero_2 sorrow "Perhaps I was in my chambers, or perhaps under some faraway skies───"
    nero_2 normal "In either case, I came to below a different sky altogether,"
    nero_2 "on a stage of convergence seemingly set up to determine the fate of the world."
    nero_2 normal "As one would expect, there is a lot I have yet to understand."
    nero_2 "What I do understand, however, is what needs to be done!"
    nero_2 shout "Namely, this situation requires us to fight! Mash! And Chaldea's Master!"
    mash_3 joy "Emperor Nero───!"
    nero_2 shout "I don't know the full extent of things, but this is what needs to be done."
    nero_2 "Can we presume that pillar-like thing is our enemy?"
    mash_3 6 "Y-yes! According to incoming communications from Chaldea,"
    mash_3 "its provisional name is Demon God Pillar Flauros! The second Demon Beast Incarnadine!"
    mash_3 14 "We fought it once before, in the second Singularity..."
    mash_3 "I don't suppose Your Highness would remember that...?"
    nero_2 shy "You'd be correct! Frankly, I must confess that I don't remember much at all!"
    nero_2 normal "But my soul remembers that I once fought beside you Chaldeans!"
    nero_2 joy "Thus, I shall brandish this blade of meteoric iron with all my being! As a fellow comrade-in-arms!"
    mash_3 joy "!"
    first_hassan_2 normal "..."
    merlin_2 normal "Take it all in, Old Man of the Mountain. This is what you'd call a miracle, isn't it?"
    merlin_2 normal "You know about Her Majesty the red emperor, I take it?"
    merlin_2 normal "The living person, keeping their karmic destiny concealed within their body,"
    merlin_2 "who they met in that Singularity."
    merlin_2 normal "They borrowed the Saint Graph of the very same existence, etched into the Throne,"
    merlin_2 "and ultimately charged headfirst into battle."
    merlin_2 joy "Fufufu, amazing, amazing! That's two or three miracles achieved by this point, isn't it!?"
    merlin_2 joy "Just how many impossibilities will be overturned!? Truly beautiful!"
    merlin_2 joy "At the end of the headache that young woman endures───"
    merlin_2 "The Beast of Love will be hard pressed!"
    first_hassan_2 normal "......"
    first_hassan_2 normal "If the founder of the seven hills were here, he'd say it."
    merlin_2 normal "Hm?"
    first_hassan_2 shout "───Rome! Just that one word!"
    first_hassan_2 normal "Miracles in times of crisis. Fraternity owing itself to the battlefield."
    first_hassan_2 normal "These things are all part of {rb}romance{/rb}{rt}Rome{/rt}───that's what he'd say."

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False

label story_643_1:
    # loading screen
    $ preloadImages (loading_images["10802"] + music_to_download["643_1"])
    # music
    play music "audio/map_septem_intro.ogg" noloop
    queue music "audio/map_septem_loop.ogg" loop
    show bg loading_02 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["643_1"]] + [background_images[l] for l in backgrounds_to_download["643_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg rome_night with black_fade_in
    pause 1.0

    nero_2 sorrow "Ggh...! A migraine, now of all times...!"
    boudica_2 sorrow "Ah, jeez. Don't just rush on ahead like that. We're relying on you for leadership, you know."
    nero_2 joy "Oh, Boudica!"
    nero_2 joy "Ah yes...I remember now. You were my enemy once."
    nero_2 joy "The dreaded warlord who once stood against my Rome, fighting alongside me now!"
    boudica_2 normal "Looks like it. I was your enemy once upon a time, but some things happened and, well, y'know."
    boudica_2 "Now, take a look."
    boudica_2 joy "The greatest allied army in history awaits your command, and so do the generals leading it!"
    caesar_2 joy "Hah hah hah hah! This time we meet not in opposition, but as comrades!"
    caesar_2 joy "Narrowly escaping the grasp of his beloved Cleopatra,"
    caesar_2 "here to behold the skill of the fifth Emperor,"
    caesar_2 joy "Julius Caesar has come to conquer! Rejoice, all of you!"
    caligula_2 anger "Ooooooooh...!! Rome...immortal...Demon Beast Incarnadine...DESTROY...!"
    caligula_2 shout "DESTROOOOOOY!!"
    nero_2 shout "Uncle!? And Lord Caesar!"
    caesar_2 shout "And we are not alone!"
    caesar_2 "O Heroic Spirits who have devoted yourselves to the training of the Divine Ancestor!"
    caesar_2 shout "Come forth!"
    $clear_scene()
    show bg boss_02 with Dissolve(2.0)
    pause 1.0

    leonidas_i_2 shout "Nwaaaaaaaaaah! My body is rejuvenated through the strength of your war cries!"
    leonidas_i_2 shout "Lancer, Leonidas I! Reporting for duty!"
    mash_3 joy "King Leonidas...!"
    leonidas_i_2 normal "Sparta's patron god is Ares, also known as Mars!"
    leonidas_i_2 "And now, I have received the tutelage of his son, the Divine Ancestor!"
    leonidas_i_2 normal "Truly, I am the god of war made manifest!"
    leonidas_i_2 joy "Allow me to lend you his power, O Fifth Emperor of Rome!"
    nero_2 shout "King Leonidas of Sparta! You too would side with me...!"
    nero_2 sorrow "Wait a minute. Who is this Divine Ancestor you keep mentioning?"
    lord_el_melloi_ii_2 normal "You don't know...? Well, you should."
    mash_3 normal "!"
    nero_2 anger "The alliance's strategist! Your name was..."
    lord_el_melloi_ii_2 normal "Zhuge Liang. Well, it's Lord El-Melloi II at present."
    lord_el_melloi_ii_2 normal "To those of you from the Human Security Organization Chaldea,"
    lord_el_melloi_ii_2 "I will tell you the truth as a mage of the Clock Tower."
    lord_el_melloi_ii_2 normal "I don't know about the other domains, but as for this one..."
    lord_el_melloi_ii_2 normal "Many of the Heroic Spirits gathered here have temporarily manifested"
    lord_el_melloi_ii_2 "with the assistance of Rome's Divine Founder."
    nero_2 sorrow "Th-that..."
    lord_el_melloi_ii_2 shout "The father of Rome. You might know him better as Romulus, the Founding King."
    lord_el_melloi_ii_2 shout "Or as he is now, Romulus-Quirinus."
    lord_el_melloi_ii_2 "Son of the war god, and one of the three supreme deities of Rome!"
    nero_2 shout "!!!"
    altera_2 normal "The war god has my respect. If his son commands so, then I shall heed his words."
    altera_2 normal "So, I too have come."
    altera_2 normal "Rome has spoken. All of you are good civilization."
    altera_2 normal "And Nero. Emperor Nero. You..."
    altera_2 joy "Because you were kind to me in that distant sky..."
    altera_2 normal "I shall protect you this time... The me here and now shall destroy the Demon Beast Incarnadine."
    mash_3 6 "Altera! The Heroic Spirit of Destruction!"
    mash_3 "Otherwise known as King Atilla, the Scourge of God!"
    nero_2 shout "...!"
    nero_2 shout "Aaaah, I don't know how much more I can take!"
    nero_2 sorrow "T-the Divine Ancestor would lend his power to me!? To Chaldea!?"
    nero_2 sorrow "I don't understand this at all!"
    nero_2 sorrow "I don't understand..."
    nero_2 shout "But despite that! Right now, all of Rome is within my grasp!"
    nero_2 shout "As the Divine Ancestor once said to his father, the god of war!"
    nero_2 "There is enough light in mankind to nurture a heart that loves all!"
    nero_2 anger "History is rife with that which denies it to be the case."
    nero_2 "And so we behold the dread form of the Demon Beast Incarnadine!"
    nero_2 anger "This would stop us in our tracks? How laughable."
    nero_2 shout "Even the Age of Gods must come to an end."
    nero_2 "Once, our very own Roman Empire proved that to be true!"
    nero_2 shout "The Age of Man is the Age of Romance!"
    merlin_2 normal "(Seriously...?)"
    first_hassan_2 normal "..."
    nero_2 normal "Man loves his fellow man..."
    mash_3 normal "Love───"
    boudica_2 normal "......"
    nero_2 shout "That is what I dream of! That is what Rome is!"
    nero_2 shout "Thus I declare! Advance! And conquer!"
    nero_2 shout "Our arms pave the way for all! Our love shall one day reach the heavens themselves!"
    roman_army  "UUUUUUUUUURAAAAAAAAH! HAIL THE DIVINE ANCESTOR! HAIL EMPEROR NERO CLAUDIUS!"
    nero_2 shout "!?"
    boudica_2 shout "That's the thousands of soldiers supporting you."
    boudica_2 "They swear allegiance neither to Alliance nor Empire, but to Rome itself."
    roman_army  "HAIL THE EMPEROR! HAIL, OUR NERO CLAUDIUS!"
    nero_2 joy "Yes...yes...!"
    nero_2 shout "Don your crimson and gold! I and Rome promise you glory and victory!"
    nero_2 anger "This Beast shall know by what means it falls."
    nero_2 anger "And it shall see that even if this band of despair envelops the sky,"
    nero_2 "that light shall never fade."
    nero_2 anger "My abominable migraine has vanished! I see clearly now!"
    nero_2 shout "Let the decisive battle begin!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_643_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["643_4"]] + [background_images[l] for l in backgrounds_to_download["643_4"]] + music_to_download["643_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    show bg boss_02_full with black_fade_in
    pause 1.5
    play sound "sfx/desummon.ogg"
    scene black with wipedown
    pause 2.0
    show bg rome_dusk with black_fade_in

    play music "audio/map_septem_intro.ogg" noloop
    queue music "audio/map_septem_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
    mash_3 anger "The second Demon Beast Incarnadine has been silenced!"
    altera_2 joy "Yes...we sync well together. As expected of an emperor."
    nero_2 joy "You certainly seem to be used to it, too."
    nero_2 "It almost feels like this isn't the first time we've been in battle together!"
    lord_el_melloi_ii_2 normal "It has the same level of power as the thing"
    lord_el_melloi_ii_2 "that caused my apprentice's Holy Lance to go crazy..."
    lord_el_melloi_ii_2 joy "Certainly, you've endured it well."
    merlin_2 normal "Amazing... You actually survived the pull of the Beast."
    merlin_2 joy "She truly is an impressive emperor. Or rather, that's what humanity is all about."
    merlin_2 "That's the way it should be!"
    nero_2 normal "?"
    merlin_2 normal "Well then, let's go!"
    first_hassan_2 normal "───This way to the third domain."
    nero_2 shout "Mash, Master of Chaldea! Head on!"
    nero_2 joy "My Roman legion and I will take care of this area. You may go forth."
    nero_2 joy "This world will never end, for all roads lead to our seven hills!"
    nero_2 shout "Forward! Conquer!"
    nero_2 shout "Our steps will open up the Rome of tomorrow!"
    mash_3 anger "Yes!"
    
    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop