label story_648_0:
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False
    $ renpy.choice_for_skipping()
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["648_0"]] + music_to_download["648_0"] + [background_images[l] for l in backgrounds_to_download["648_0"]])

    show bg babylon_day with black_fade_in
    pause 1.0
    play music "audio/map_babylon_intro.ogg" noloop
    queue music "audio/map_babylon_loop.ogg" loop

    mash_3 anger "We have reached the seventh domain!"
    tiamat_1 normal "Mash...?"
    tiamat_1 7 "Mash. Mash! And Master too!"
    tiamat_1 joy "Mother is so happy to see her children again!"
    tiamat_1 joy "What good and darling children."
    mash_3 shy "Y-yes..."
    merlin_2 joy "Suddenly, they're both like putty in her hands! Hmm, is this a bunrei of Divine Spirit Tiamat?"
    first_hassan_2 shout "......"
    lancelot_2 normal "RRRRrrrrrRRRRRRRRRRRRRrrrr!"
    sakata_kintoki_2 shy "That's right, Tiamat! At least try to read the mood a little here!"
    sakata_kintoki_2 sorrow "Breaking out the good mother moves in this tense atmosphere ain't hardly golden!"
    tiamat_1 normal "Are you sulking, Kintoki? Come over here."
    sakata_kintoki_2 shout "It ain't a matter of sulking───"
    sakata_kintoki_2 "aw man, she's got more power to drag me away than Shuten ever had!"
    sakata_kintoki_2 shy "Mmph."
    tiamat_1 joy "There, there. You're a good boy, Kintoki."
    lancelot_2 normal "RRRRrrrrrRRRRRrrrr!"
    $clear_scene()
    stop music fadeout 2.0
    scene black with black_fade_out
    show bg grail_mud with black_fade_in
    pause 1.0


    play music "audio/battle_babylon_intro.ogg" noloop
    queue music "audio/battle_babylon_loop.ogg" loop

    queen_draco_shadow_1 shadow "Quite a few, indeed..."
    queen_draco_shadow_1 shadow "A few morsels, indeed. Do not underestimate a mere bunrei or shadow, Tiamat."
    queen_draco_shadow_1 shadow "Very well. This once, I shall forgive you."
    queen_draco_shadow_1 shadow "There is no King of Babylon here this time. No need to manipulate a king,"
    queen_draco_shadow_1 "nor to devour any city of prosperity."
    queen_draco_shadow_1 shadow "All who have shown their faces are Heroic Spirits guided here by some incomprehensible miracle."
    queen_draco_shadow_1 shadow "How dull───"
    queen_draco_shadow_1 shadow "I share that sentiment as well."
    queen_draco_shadow_1 "Were I able to appear before my “foolish self” in the second domain,"
    queen_draco_shadow_1 shadow "I would tear off my uncle's head and play a game of catch with her..."
    queen_draco_shadow_1 shadow "But this is the domain entrusted to me. I never thought I would have to face all of you again."
    queen_draco_shadow_1 shadow "But all is well. The Master of Chaldea has arrived at last."
    queen_draco_shadow_1 shadow "The spare time and tedium ends now! I shall drink up every last one of you!"
    tiamat_1 shout "No, you won't! If you try to drink everything, Mother will be mad!"
    tiamat_1 shout "To protect Mash and Master, I will become a shield of dragon scales!"
    sakata_kintoki_2 joy "Sounds good! Then I'll be the blade!"
    sakata_kintoki_2 normal "And I'm gonna have to be an electric blade. I can hear the voices calling me."
    mash_3 6 "Voices...?"
    sakata_kintoki_2 normal "Yeah, but obviously not any of yours. They're more faint and weak."
    sakata_kintoki_2 normal "“There's too much bitterness to bear.”"
    sakata_kintoki_2 "That's what countless voices shouted the moment the world was burned."
    sakata_kintoki_2 normal "I wonder how many things they would've wanted to do?"
    sakata_kintoki_2 "A mom making dinner, a kid who wanted to play the day after."
    sakata_kintoki_2 normal "I've got no idea... It's enough to make me grind my teeth."
    sakata_kintoki_2 anger "Whoever doesn't understand how important all those things are..."
    sakata_kintoki_2 anger "I don't know what's between the ears of them!"
    sakata_kintoki_2 anger "Before you start talking about humanity's future, Draco,"
    sakata_kintoki_2 "I'm gonna smash your stupid nature back to normalcy!"
    sakata_kintoki_2 anger "For every day that's gone to waste since this place was burned to ash,"
    sakata_kintoki_2 anger "I'm gonna kick your ass for everyone that couldn't make the most of them!"
    sakata_kintoki_2 shout "I'm Kintoki, Sakata Kintoki. One of Raikou's Four Heavenly Kings who heard those sounds!"
    lancelot_2 shout "RRRRrrrRRRRRRRrr!"
    sakata_kintoki_2 shout "Let's go, buddy! Restrain the demons and smash the rakshasas!"
    sakata_kintoki_2 shout "Split the heaven and earth, tearing up space and Demon Beast Incarnadines with it!"
    sakata_kintoki_2 "Hell yeah, now here's the treasured blade of fiery lightning coming to kill you dead!"
    sakata_kintoki_2 shout "───The one and only Golden Spark!"
    queen_draco_shadow_1 shadow "Very good. Shout and defy me!"
    queen_draco_shadow_1 shadow "Entertain me by changing the flavor of your dying moments with all you can muster,"
    queen_draco_shadow_1 "human history!"



    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    #hide bg
    #$store.draw_background = False

label story_648_1:
    # loading screen
    $ preloadImages (loading_images["10807"] + music_to_download["648_1"])
    # music
    play music "audio/draco_pre_intro.ogg" noloop
    queue music "audio/draco_pre_loop.ogg" loop
    show bg loading_07 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["648_1"]] + [background_images[l] for l in backgrounds_to_download["648_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts
    show bg grail_mud with black_fade_in
    pause 1.0

    gilgamesh_2 shout "───Some bewitching queen this Draco is!"
    gilgamesh_2 sorrow "A mere husk whose contents rest on the throne. Worthless."
    merlin_2 joy "Wow. Could he be...?"
    sakata_kintoki_2 joy "It's you...!"
    mash_3 joy "King Nebuchadnezzar! N-no...!"
    tiamat_1 normal "Gilgamesh the 2.5th!"
    tiamat_1 sorrow "The aura seems different...it's changed? Maybe it's his hairstyle?"
    tiamat_1 7 "Maybe it's...the declaration to join us as an ally!?"
    tiamat_1 joy "Thank you. Mother is so glad."
    tiamat_1 joy "I want to hug you tightly as thanks... Will you come here?"
    gilgamesh_2 sorrow "What is that form? Why has the Divine Spirit Tiamat shrunken so?"
    gilgamesh_2 shy "But first thing's first..."
    gilgamesh_2 anger "What did you say when you saw me?"
    mash_3 normal "U-uhm..."
    lancelot_2 normal "RrrrRRrr?"
    sakata_kintoki_2 normal "Right, right. Tiamat called him Gilgamesh the 2.5th."
    sakata_kintoki_2 shy "(Mm...)"
    sakata_kintoki_2 shy "(She didn't get it wrong, did she? I know that Nebuchadnezzar was the 2.5th.)"
    merlin_2 sorrow "Huh? What?"
    first_hassan_2 sorrow "Gilgamesh the 2.5th is what was said."
    gilgamesh_2 anger "!"
    gilgamesh_2 shout "...!"
    gilgamesh_2 shout "That. What is the meaning of Gilgamesh the 2.5th!?"
    gilgamesh_2 shout "Be quick, concise, and convincing in your explanation!"
    gilgamesh_2 shy "Now, the 2nd. That at least would be pleasant."
    gilgamesh_2 "It's not as though that's beyond the realm of understanding."
    gilgamesh_2 shout "But───what is this 2.5th to mean?"
    tiamat_1 normal "Huh."
    tiamat_1 7 "Huh? What?"
    tiamat_1 sorrow "The familiar feeling of this Saint Graph,"
    tiamat_1 "its body and soul...you don't suppose this is..."
    tiamat_1 7 "The real one?"
    mash_3 6 "!"
    sakata_kintoki_2 shout "(So Tiamat did get it all wrong!?)"
    gilgamesh_2 shout "What is this reaction about, you mongrels!?"
    gilgamesh_2 "What is the meaning of calling me the real one!?"
    enkidu_2 joy "Hahahahaha. This is kind of amusing."
    gilgamesh_2 shout "Not for me!"
    enkidu_2 joy "Gil, if you care so much, why don't you just use one of your Noble Phantasms?"
    gilgamesh_2 shout "Nonsense! To think I would use my Noble Phantasm of omniscience for such a trifle!?"
    gilgamesh_2 anger "What am I to say to Siduri in the underworld if I disgraced myself so───"
    enkidu_2 normal "Oh, were you planning to pass through the underworld on your way back?"
    enkidu_2 "Since when did you find fault with Siduri's lecturing?"
    gilgamesh_2 joy "Hmph...I have no objection to one that proves itself necessary."
    gilgamesh_2 "And she has never volunteered advice out of turn."
    enkidu_2 joy "Sure, whatever you say."
    gilgamesh_2 shout "Enkidu!"
    stop music fadeout 2.0
    queen_draco_shadow_1 shadow "..."
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 1.0
    play music "audio/draco_intro.ogg" noloop
    queue music "audio/draco_loop.ogg" loop
    queen_draco_shadow_1 shadow "──My, my. And now comes the last mouthful."
    queen_draco_shadow_1 shadow "You act out a comedy before me, the Beast's retainer."
    queen_draco_shadow_1 "In mere seconds, you will find repentance in a pool of your own blood."
    queen_draco_shadow_1 shadow "Cry out in agony and beg forgiveness."
    queen_draco_shadow_1 shadow "Moan in despair and pray for salvation in death."
    queen_draco_shadow_1 shadow "I deny all things. I shall devour your souls whole."
    queen_draco_shadow_1 shadow "That which is sin stirs to form the finest wine."
    queen_draco_shadow_1 "Its tastes are terrors and agonies continuing without end."
    queen_draco_shadow_1 shadow "How can the world of mere Heroic Spirits, mere imitations of Divine Spirits,"
    queen_draco_shadow_1 "or even that of the King of Heroes even compare?"
    queen_draco_shadow_1 shadow "So long as you are human, you cannot stand against my reason."
    queen_draco_shadow_1 "You can but merely bow down."
    gilgamesh_2 joy "Call me Gilgamesh the Sage-King, not the King of Heroes."
    gilgamesh_2 normal "This is a Saint Graph well-suited for a mongrel of your ilk, Draco."
    gilgamesh_2 normal "I shall quickly and brilliantly settle matters with you,"
    gilgamesh_2 "before addressing the issue of “Gilgamesh the 2.5th”."
    gilgamesh_2 joy "Now come────I can taste without end the mud brought forth by prosperity."
    queen_draco_shadow_1 shadow "You dare───"
        


    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_648_4:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["648_4"]] + [background_images[l] for l in backgrounds_to_download["648_4"]] + music_to_download["648_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 1.0
    show bg babylon_day with black_fade_in

    play music "audio/map_babylon_intro.ogg" noloop
    queue music "audio/map_babylon_loop.ogg" loop
    $ renpy.choice_for_skipping()
    
    mash_3 anger "Confirmed annihilation of Bewitching Queen Draco's incomplete Saint Graph!"
    tiamat_1 shout "It's because she made mother furious! Hmph!"
    tiamat_1 shout "And an angry mother is strong. Tee-hee."
    enkidu_2 joy "Fufu. How cute of you, mother."
    tiamat_1 shout "Ahem!"
    gilgamesh_2 sorrow "Don't ahem me, dear sweet goddess Tiamat. I'm asking you what Gilgamesh 2.5 even means."
    tiamat_1 sorrow "Ohh, what overbearing pressure...leave this to your mother and go on ahead!"
    merlin_2 normal "I think it's best if we actually take her advice. Look there!"
    mash_3 anger "Y-yes. The final gate at the end of the domain───it's opening up!"
    tiamat_1 joy "Do your best! Mother will be here praying for your safety!"
    sakata_kintoki_2 joy "This is the final great golden decisive showdown! Do me a solid and give it your best shot!"
    lancelot_2 normal "(RRRRRrrrrrRRRRRR)"
    mash_3 joy "Understood!"
    mash_3 anger "Mash Kyrielight and her Master will now go beyond the final gate...!"
    mash_3 anger "And reach the throne!"

    $clear_scene()
    stop music fadeout 2.0
    scene black with black_fade_out
    show bg lilim_1 with black_fade_in
    pause 1.0

    merlin_2 normal "Well, the final battle is upon us. Are you ready?"
    first_hassan_2 normal "───"
    merlin_2 normal "It goes without saying, eh? We've gone beyond the gate now───"
    mash_3 shout "The magical energy quantity is immeasurable...it's First-Class Planetary Grade!"
    merlin_2 anger "The throne is in sight. I see, so the one seated there is the true Great Bewitching Queen."
    merlin_2 anger "Deceiving “Chaldea” by mimicking the seven Singularities and linking many worlds together,"
    merlin_2 anger "and as nourishment for maturation,"
    merlin_2 "the wishes of the “saviors who brought salvation unto the world”───"
    merlin_2 anger "The Evil of Humanity who amassed the “wishes” of countless Chaldeas,"
    merlin_2 "each in parallel worlds, within the Grail and drank from it."
    merlin_2 anger "Class Beast. The Sixth Beast."
    merlin_2 anger "Or perhaps I should put it this way───Beast VI, the true form of Sodom's Beast."

    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.pause(1.0, hard=True)
    $ play_video("video/BeastReveal.webm")

    show beast_vis_1_big normal at fade_test(2.0)
    pause 2.0
    beast_vis_1_big "..."
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 1.5
    play music "audio/lilim_battle_intro.ogg" noloop
    queue music "audio/lilim_battle_loop.ogg" loop

    show beast_vis_1_big 0
    beast_vis_1_big "Precisely. My Authority of the Beast is Nega-Messiah. I am the one who ridicules, slaughters and consumes the Savior."
    show beast_vis_1_big normal
    beast_vis_1_big "Cherishing the “wishes of the masses” is fine and all, but it provides no nourishment whatsoever."
    show beast_vis_1_big 0
    beast_vis_1_big "The Chaldea who vanquished the First Beast in this universe. And its Master. You who exist in a multitude of worlds."
    beast_vis_1_big "The only “wish” that will suffice in growing my horns is the wish to “save the world”."
    show beast_vis_1_big sorrow
    beast_vis_1_big "It is for this reason that the Singularities exist, that the Holy Grail War exists. Your “battles” were succulent indeed."
    mash_3 14 "Then...the very act of competing for the Holy Grail results in Beast VI's growth...!?"
    show beast_vis_1_big normal
    beast_vis_1_big "Correct. As a result, you lot have reached this realm."
    beast_vis_1_big "The graveyard of many prosperities. A banquet table adorned by the rot of many Human Orders."
    beast_vis_1_big "This realm isn't just “the end of some history”. It prophesies the end of your human history."
    beast_vis_1_big "───In other words, this is a fate written in stone that your world will reach in a few years from now."
    show beast_vis_1_big 0
    beast_vis_1_big "I am the one who savors that end. For fruits are best savored when they are on the verge of rotting."
    beast_vis_1_big "You have no cause to defy me, given that you have beheld the future. O Earthlings, perish before my fangs."
    beast_vis_1_big "You have my gratitude too. You did well “getting this far” once more."
    show beast_vis_1_big normal
    beast_vis_1_big "Chaldea may have raised me, but it is an inevitability of the Human Order to beckon the apocalypse."
    beast_vis_1_big "For Beasts are weak, and alone they cannot scar the world."
    beast_vis_1_big "Only you humans are capable of destroying the world."
    beast_vis_1_big "This repulsive scenery is what the masses desired."
    beast_vis_1_big "I am merely a Beast revelling in it. This outcome is one not even I can change."
    show beast_vis_1_big 0
    beast_vis_1_big "So hold your heads high. That desire has led to the completion of humanity's extermination here."
    mash_3 12 "The desire of the masses... To find greater enjoyment. To live in greater comfort."
    mash_3 12 "Born from this inclination of humanity's is the self-ruination that lies at the end of prosperity."
    mash_3 anger "I understand that. It is an inevitability of life. So───that in itself is not evil."
    mash_3 anger "I understand that it's not evil."
    show beast_vis_1_big normal
    beast_vis_1_big "───Is that so? Then what is evil to you?"
    mash_3 anger "People's lives. Their feelings. Their memories. The ones who ridicule these are evil."
    mash_3 anger "If this scenery lies at the end of the Human Order,"
    mash_3 "then we shall continue to move forward, seeking it."
    mash_3 shout "However!"
    mash_3 shout "I will not accept you, you who treat those as mere amusements!"
    mash_3 shout "Beast VI! Beast of Calamity!"
    mash_3 shout "At a place elsewhere, at a Chaldea that is not our own,"
    mash_3 shout "“someone” fought until the very end! To not lose to them, this “Chaldea” here will defeat you!"
    merlin_2 joy "───!"
    show beast_vis_1_big sorrow
    beast_vis_1_big "──────!"
    merlin_2 joy "───Wonderful. Oh, how wonderful, stargazing knight!"
    merlin_2 joy "That's right, I'm sick and tired of that inevitable end!"
    merlin_2 joy "After all, it takes a sourpuss to think the end can happen anytime so long as it's a happy ending!"
    merlin_2 normal "I happen to be rather greedy. Far greedier than any Master here in this Holy Grail War."
    merlin_2 joy "I have no wish to see the end! I want to see a happiness that lasts forever and ever!"
    show beast_vis_1_big normal
    beast_vis_1_big "I see───So we are incompatible existences after all, Beast of the Planet."
    merlin_2 normal "Woah there, don't say any more than that. I still haven't told a single soul about that yet."
    merlin_2 anger "Well then, we both know where the other is coming from!"
    merlin_2 "It's time for us irreconciliable archenemies to settle our differences!"
    merlin_2 shout "Our enemy is Beast VI/S!"
    merlin_2 anger "The incarnation of decadency───"
    merlin_2 "that which continues to gaze upon the unsightliest of things───"
    merlin_2 "in the unsightliest of worlds!"
    #show beast_vis_1_big anger
    first_hassan_2 "The Evening Bell's moment draws near. Do not fall behind, child!"
    mash_3 shout "Understood!"
    mash_3 shout "───Roger that, Master. Commencing anti-Beast combat!"

    $store.is_boss_map = True

    
    $ clear_scene()
    $ renpy.choice_for_skipping()
    pause 2.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop