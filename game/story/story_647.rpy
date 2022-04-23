label story_647_0:
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["647_0"]] + music_to_download["647_0"] + [background_images[l] for l in backgrounds_to_download["647_0"]])

    show bg jerus_day with black_fade_in
    pause 1.0
    play music "audio/map_lostj_intro.ogg" noloop
    queue music "audio/map_lostj_loop.ogg" loop

    jacques_de_molay_1 20 "......"
    jacques_de_molay_1 normal "───I failed as a knight."
    jacques_de_molay_1 normal "Apostatized as a monk, expunged as a grandmaster."
    jacques_de_molay_1 anger "These regrets I harbor of having returned to ashes without achieving anything."
    jacques_de_molay_1 "How could I possibly stand to not resolve them here and now!?"
    jacques_de_molay_1 sorrow "P-please do not stop me, Lady Leonardo da Vinci!"
    da_vinci_2 normal "There, there. There, there. Calm down, calm down."
    jacques_de_molay_1 shout "How could I possibly remain calm!?"
    da_vinci_2 shout "Nevertheless, we can't have you charging the enemy all on your lonesome, can we!?"
    mash_3 6 "We've reached the sixth domain...but what's going on here!?"
    mash_3 anger "Da Vinci is restraining the Heroic Spirit Jacques de Molay!"
    okada_izou_1 normal "Hey there, Mash and the Chaldeans in tow! Do something about those idiots, will ya!?"
    okada_izou_1 9 "Heroes from all ages and places are gathering here, can't have them dying in vain now."
    medusa_1 sorrow "To think even Izou would say this to him...Molay truly is a pitiable man..."
    okada_izou_1 12 "What did you say!?"
    jacques_de_molay_1 shout "Please unhand me, Da Vinci!"
    jacques_de_molay_1 shout "This humiliation of mine shall be rectified here! To do so, I would stop at nothing!"
    mash_3 14 "Eh, umm───Heroic Spirit Molay, please calm yourself!"
    jacques_de_molay_1 shout "I would...!"
    first_hassan_2 sorrow "..."
    first_hassan_2 normal "O heathen..."
    first_hassan_2 normal "Is that truly resolve? Are foolhardiness and recklessness the virtues of thy god?"
    jacques_de_molay_1 sorrow "!!"
    jacques_de_molay_1 20 "I...I───"
    da_vinci_2 joy "Thank goodness! He's been attempting a charge and wouldn't listen to me."
    da_vinci_2 normal "In any case, I'm glad we somehow managed to stop him. Thank you, umm...Mister..."
    first_hassan_2 normal "Old Man of the Mountain. I am Hassan-i-Sabbah."
    da_vinci_2 shout "{i}That{/i} Old Man of the Mountain!? What an intimidating aura!"
    da_vinci_2 "As expected of one who became a legend in life, you truly are in a different league!"
    merlin_2 normal "I'm in total agreement. It's really convincing coming from the legendary genius herself."
    merlin_2 normal "As for our enemies in this domain...hmm, the Demon Beast Incarnadine and Shadow Servants!"
    merlin_2 normal "Just like the lineup from earlier."
    merlin_2 "And the Heroic Spirits who will miraculously stand against them are───"
    okada_izou_1 normal "That'll be me!"
    medusa_1 normal "I'm here too. Not yet, Izou. Not quite yet."
    okada_izou_1 sorrow "Rider, you think I'm a dog or something after all, is that it...?"
    georgios_3 joy "I am present as well!"
    georgios_3 "Much like Sir Molay, I too have come forth to rectify my sins in that Singularity!"
    georgios_3 anger "The Great Bewitching Queen who cants the Great Grail,"
    georgios_3 "in other words, the great evil spoken of in the Book of Revelation!"
    georgios_3 anger "In which case, thou art a dragon! I swear upon my Ascalon!"
    georgios_3 shout "I shall decapitate───one of those heads of yours!"
    cursed_arm_3 normal "We are present too! Unfit as we may be, we would like to offer our assistance───"
    first_hassan_2 normal "Cursed Arm, hast thou redressed some of thy hesitations in life?"
    cursed_arm_3 shout "Lord Founder!?"
    mata_hari_3 normal "Is something the matter, Hassan? You're shouting all of a sudden."
    cursed_arm_3 normal "N-n-n-n-n-no, I see."
    cursed_arm_3 "Seeing how the world is on the brink of destruction,"
    cursed_arm_3 "the Lord Founder's advent does make sense!"
    cursed_arm_3 normal "How auspicious. What great fortune───I shall savor the joy of fighting alongside you!"
    first_hassan_2 normal "Very well. Thou shalt endeavour as a Heroic Spirit."
    first_hassan_2 normal "Thou canst offer thy head after all is said and done with."
    cursed_arm_3 shout "U-understood!"

    $clear_scene()
    stop music fadeout 2.0
    show bg jerus_boss with Dissolve(2.0)
    pause 1.0

    jacques_de_molay_shadow_1 shadow "────────"
    play music "audio/jacques_intro.ogg" noloop
    queue music "audio/jacques_loop.ogg" loop
    jacques_de_molay_shadow_1 shadow "───Vermin swarming all over the place."
    jacques_de_molay_shadow_1 shadow "Very well then. Bring it on. I shall exterminate you as an Apostle of Lust."
    jacques_de_molay_shadow_1 shadow "I have partaken of the overflowing Great Grail!"
    jacques_de_molay_shadow_1 "Know that I have reached heights unachievable by common Heroic Spirits!"
    mash_3 anger "!"
    mash_3 anger "Magical energy levels, rising! Such a tremendous amount!"
    merlin_2 anger "This much magical energy despite that incomplete Saint Graph, huh!?"
    merlin_2 "Looks like we have a tough enemy on our hands!"
    jacques_de_molay_1 sorrow "Ugh...! I...I...!"
    whomst  "You shall triumph!"
    whomst  "You shall triumph! For!"
    whomst  "───For I and Chaldea stand by your side!"
    mash_3 6 "This voice is...!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    #$renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    #hide bg
    #$store.draw_background = False

label story_647_1:
    # loading screen
    $ preloadImages (loading_images["10806"])
    # music
    #play music "audio/map_lostj_intro.ogg" noloop
    #queue music "audio/map_lostj_loop.ogg" loop
    show bg loading_06 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["647_1"]] + [background_images[l] for l in backgrounds_to_download["647_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg jerus_boss with black_fade_in
    pause 1.0

    medjed_1 shout "Pay close attention! And now, behold!"
    medjed_1 shout "For this is the advent of splendor! The splendor of Pharaoh Ozymandias!"
    ozymandias_3 shy "Hahahahahahahahahahahahahahahaha!"
    ozymandias_3 "Your supreme Pharaoh just happened to be passing by!"
    ozymandias_3 shy "And by complete coincidence, also passing by in the form of Amon-Ra!"
    ozymandias_3 joy "On a pleasure cruise, that is!"
    ozymandias_3 anger "But what is this? The knight who was in charge of guiding the pilgrims on their travels..."
    ozymandias_3 6 "That is only one shadow, and furthermore, only one Demon Beast Incarnadine."
    ozymandias_3 shout "To be afraid of such minor pests is a complete farce!"
    ozymandias_3 "Have you forgotten when you opposed my majesty, wretch!?"
    mash_3 joy "Pharaoh Ozymandias! No, Amon-Ra!"
    jacques_de_molay_1 17 "...!"
    medjed_1 shout "Bask in the Pharaoh's splendor! How long shall you wallow in your dejection!?"
    medjed_1 normal "If you can open your eyes, then stand and take up your sword."
    medjed_1 normal "He has allowed you especially to stand alongside his radiant majesty and do battle."
    jacques_de_molay_1 10 "Your concern is well appreciated..."
    jacques_de_molay_1 anger "For mine is the shield of faith───my oaths, unshakable and unbreakable."
    jacques_de_molay_1 shout "I believe, here and now, that it will never crack again! So swear we of the Knights Templar!"
    first_hassan_2 normal "......"
    merlin_2 joy "Oh Hassan, do I hear a small chuckle from you?"
    merlin_2 "Have you come to empathize with your one-time nemesis?"
    first_hassan_2 normal "It seems that not merely the tongue,"
    first_hassan_2 "but the observation of the extradimensional Magus of Flowers is too quick to judge."
    merlin_2 joy "Trying to tell me I'm misunderstanding things? Fair enough, I'll leave it there."
    jacques_de_molay_shadow_1 shadow "──────Tsk."
    jacques_de_molay_shadow_1 shadow "Don't get cocky just from recruiting a pseudo-Demon God Pillar."
    jacques_de_molay_shadow_1 "That thing falters in comparison to the Holy Grail..."
    jacques_de_molay_shadow_1 shadow "I am secure in its power, in its inexhaustible magic energy!"
    jacques_de_molay_shadow_1 shadow "I am...!"
    first_hassan_2 normal "Hold thy tongue, lest it speak your last will."
    first_hassan_2 "If thou art a shadow, speak only the truth when nearing your death."
    jacques_de_molay_shadow_1 shadow "What's that...? My desires are no falsehood...!"
    jacques_de_molay_1 shout "I won't let you have your way. By my life and my regrets, you will be stopped here!"
    jacques_de_molay_1 shout "───Say your prayers, my hideous shadow!"


    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_647_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["647_4"]] + [background_images[l] for l in backgrounds_to_download["647_4"]] + music_to_download["647_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 1.0
    show bg desert with black_fade_in

    play music "audio/map_lostj_intro.ogg" noloop
    queue music "audio/map_lostj_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
    mash_3 anger "───Hostile Shadow Servant destroyed. The Demon Beast Incarnadine has been silenced!"
    da_vinci_2 joy "We did it! Good job, everybody!"
    ozymandias_3 shy "Victory should come as no surprise! Who else but I could have ascended to your aid?"
    ozymandias_3 normal "Hmph, but that Da Vinci girl's form is rather beautiful in itself."
    medjed_1 4 "Oh, Lord Ozymandias. You've returned to your normal Saint Graph?"
    ozymandias_3 joy "Do not be so formal, Nitocris. This is the proper form for a celebration and mopping-up."
    medjed_1 normal "Y-yes!"
    cursed_arm_3 normal "───Lady Mash, Master of Chaldea, leave the rest to us."
    cursed_arm_3 normal "Please go ahead while the gates of the domain are open!"
    mata_hari_3 joy "Don't give in before you reach the end. May fortune be with you!"
    jacques_de_molay_1 joy "God's blessings on your path to conquest, Mash and Master of Chaldea!"
    mash_3 joy "Yes! Let's go, Master...!"
    merlin_2 anger "We have to be prepared for more than just Demon Beast Incarnadines in the next domain."
    first_hassan_2 shout "───Let us conquer them all."

    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop