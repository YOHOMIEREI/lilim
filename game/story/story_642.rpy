label story_642_0:
    $ renpy.choice_for_skipping()
    #show bg blue_overlay at linear_fade(0.0, 0.8, 0.08)
    $ preloadImages([chara_sprites[k] for k in sprites_to_download["642_0"]])

    $store.draw_big_spot = True
    
    mash_3 normal "───We've reached the hostile Singularity."
    mash_3 normal "It's just as Chaldea predicted, this Singularity is structurally a miniature world———"
    mash_3 "a conceptual universe."

    mash_3 normal "A microscale model case of the universe, so to speak..."
    mash_3 normal "The fact that there is only one life form present within this universe is of particular note."
    mash_3 anger "The Beast of Calamity. The Evil of Humanity which manifests in civilizations that have"
    mash_3 "reached their height of prosperity and are now past their transitional period. Beast VI."

    mash_3 anger "Our operational objective is the annihilation of Beast VI."
    mash_3 "We will hereby commence the Last Order!"

    merlin_qmark_2 silhouette "───Woah there! Looks like I've made it in the nick of time once again."
    merlin_qmark_2 silhouette "Last Order, now that's a weighty phrase. Yes, that's the spirit!"
    mash_3 6 "!"
    merlin_qmark_2 normal "If this battle is to be the final one, then it will truly be the climax of this journey."
    merlin_qmark_2 joy "And in that case, that leaves me no choice but to cheer you on from the front row!"
    merlin_qmark_2 joy "After all, your journey is one that I, Merlin, have acknowledged!"
    mash_3 joy "───Merlin!"
    merlin_2 joy "Hey there, long time no see!"
    merlin_2 joy "I am glad to see you are doing well, Mash Kyrielight and Master of Chaldea."
    mash_3 joy "Yes, Merlin! No..."
    mash_3 joy "Lady Merlin of another world! It's been a while!"
    merlin_2 normal "Yes, yes. Now there's a good look and a solid voice!"
    merlin_2 normal "You did well to stay true to yourself without bending or breaking,"
    merlin_2 "in spite of the harsh journeys you have experienced."

    merlin_2 joy "I am in awe of that brilliance. So much, in fact, that I ran all the way here on foot!"
    merlin_2 joy "Now then, I'll be helping you out even more than last time!"
    mash_3 joy "Thank you very much! This is very reassuring, isn't it, Senpai?"
    merlin_2 normal "Oh, one more thing."
    merlin_2 joy "Fufufufufufufu."
    merlin_2 joy "This is going to be a sight to behold. (Grinning)"
    mash_3 6 "?"
    merlin_2 joy "(Smiling)"
    merlin_2 joy "───I'm not the only one who came here today!"
    $ clear_scene()
    $ renpy.choice_for_skipping()
    $renpy.music.stop(fadeout=2.0)
    scene black with black_fade_out
    hide bg
    $store.draw_background = False


label story_642_1:
    # loading screen
    $ preloadImages (loading_images["10801"] + music_to_download["642_1"])
    # music
    play music "audio/map_orleans_intro.ogg" noloop
    queue music "audio/map_orleans_loop.ogg" loop
    show bg loading_01 with black_fade_in
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["642_1"]] + [background_images[l] for l in backgrounds_to_download["642_1"]])
    $ renpy.choice_for_skipping()
    $renpy.show("page_icon", at_list=[page_icon_transform], layer="screens")
    $renpy.restart_interaction()
    pause
    $clear_scene()
    scene black with black_fade_out
    hide bg

    # scene starts

    show bg field_01_dusk with black_fade_in

    first_hassan_qmark_2 silhouette "───Understood."
    first_hassan_qmark_2 silhouette "For starters, we advance and crush the first Demon Beast Incarnadine."
    mash_3 6 "You're...?"
    merlin_2 normal "Didn't I just tell you? I'm not the only one who came rushing over."
    merlin_2 joy "He is the one who wanders the boundary of death!"
    merlin_2 joy "The “Old Man of the Mountain”, a title passed down in the shadows of history."
    merlin_2 "He is the first and greatest of them all, the black mask of death!"

    merlin_2 joy "His True Name is Hassan-i-Sabbah───"
    merlin_2 joy "One of the Heroic Spirits who claims the\n{rb}Station of the Crown{/rb}{rt}Grand seat{/rt}, fated to hunt Beasts,"
    merlin_2 "summoned here through the Decisive Magecraft: Heroic Spirit Summoning."
    merlin_2 joy "The Grand Assassin himself!"
    first_hassan_2 normal "I am naught but a phantom that writhes in the dark..."
    first_hassan_2 normal "Yet now the Evening Bell tolls. Let us go."
    mash_3 normal "The Evening Bell───"
    merlin_2 joy "“The fateful moment is upon us! I shall lend you my strength as a special favor”,"
    merlin_2  "is what he's trying to say!"
    first_hassan_2 normal "..."
    first_hassan_2 normal "I shall be your guide. This way."
    mash_3 6 "Ah!"
    mash_3 joy "Look, senpai! In the wake of the Old Man of the Mountain's advance..."
    merlin_2 shy "The fluttering petals of magical energy are beautiful, huh? Fufufufufu."
    merlin_2 "Sorry, but that's my handiwork."
    merlin_2 shy "If we're going to be guiding you anyway,"
    merlin_2 "I figured an easily understandable approach would be better."
    first_hassan_2 anger "You needn't bother yourself. You need not adorn their deaths with flowers."
    merlin_2 normal "Come now, don't say that. We're fellow Grands after all, aren't we?"
    first_hassan_2 normal "So says the pseudo-fairy who has ignored her {rb}Station of the Crown{/rb}{rt}Grand seat{/rt} to act as she pleases."
    merlin_2 joy "Whatever could you mean by that?"
    mash_3 normal "(I wonder what they're talking about?)"
    merlin_2 normal "Now then, about the first Demon Beast Incarnadine───"
    merlin_2 shout "Shaving off magical energy of this scale all on our own is going to prove rather troublesome."
    merlin_2 "Not to mention there's seven of these!"
    merlin_2 normal "Or so I thought, however..."
    merlin_2 joy "It looks like someone already beat us to the punch. Look over there, Mash!"
    mash_3 6 "!?"
    $clear_scene()
    show bg castle_01_night with blinds
    pause 1.0
    kiyohime_2 shout "Uncle! Uncle Vlad, please go easy now, umm!"
    vlad_iii_1 normal "I have every intention of holding back───"
    vlad_iii_1 joy "But you're doing a fine job evading my Noble Phantasm. Keep it up."
    kiyohime_2 shout "Uncle!?"
    elisabeth_1 shout "Wow, uncle Vlad's merciless! Wowowowowow."
    elisabeth_1 sorrow "Won't he end up Bey'ing us too? Are you sure this is okay?"
    carmilla_1 normal "There is no way Lord Vlad would blunder like that."
    carmilla_1 normal "More importantly, we should provide support."
    carmilla_1 "We will exterminate the first Demon Beast Incarnadine here."
    elisabeth_1 shout "Fine, fine! Let's do this───Boe~!"
    mash_3 joy "...!"
    mash_3 joy "Master, Master! Those people are...!"
    mash_3 joy "The Servants who stood against us in the first Singularity!"
    mash_3 joy "They're all attacking the Demon Beast Incarnadine in unison───"
    $clear_scene()
    show bg boss_01 with Dissolve(2.0)
    pause 1.0
    jeanne_darc_2 normal "Yes... This is undoubtedly a miracle."
    jeanne_darc_2 normal "What you see before you are “Heroic Spirits” as they should have been!"
    jeanne_darc_2 anger "We, existences engraved in the history woven by man,"
    jeanne_darc_2 "were meant to stand with the Human Order."
    jeanne_darc_2 anger "Now that we are free from the yoke of the Holy Grail's distortion and curse───"
    jeanne_darc_2 anger "We shall unite our forces to aid you, Chaldea!"
    marie_2 joy "Yes, yes! This time, we can all get along and have a party!"
    marie_2 joy "Vive la France, Master!"
    marie_2 joy "I'm glad I got to greet you again!"
    mash_3 joy "Jeanne! Marie!"
    martha_2 normal "Rather rowdy for a party...oh, I see. So that's how it is."
    martha_2 joy "We are to hold a grand banquet on this triumphant day!"
    deon_2 shout "As you command, Your Highness!"
    deon_2 "I shall bear the banner of the royal family's fleur-de-lis at this party!"
    deon_2 anger "O Demon Beast Incarnadine, inauspicious red flower of evil."
    deon_2 "You have no place in the banquet of the Human Order!"
    phantom_2 joy "Dance, dance, Demon Beast Incarnadine. Dance the Danse Macabre before us───"
    amadeus_2 joy "Oh, the Phantom appears to be in good spirits. Now there's a rare sight!"
    amadeus_2 shy "And Maria appears much the same to me. Is there even a need to take this seriously then?"
    mash_3 joy "Amadeus!"
    amadeus_2 shy "Hello, milady. We meet again. It would appear I have made it in time for the final performance."
    mash_3 joy "Yes!"
    jeanne_alter_2 shy "I'm here too, you know...? Why am I on your side?"
    gilles_de_rais_2 joy "Oh, Jeanne. Puffing up those beautiful cheeks of hers...could it be that she is sulking?"
    gilles_de_rais_2 joy "Do you wish to stand against Chaldea, even after your second summoning as an Apostle of Lust?"
    jeanne_alter_2 shout "Shut it! I'll immolate you!"
    mash_3 joy "...!"
    mash_3 joy "Master...everyone came rushing over to this final battle."
    mash_3 shout "We cannot afford to fall behind either!"
    mash_3 "Commencing anti-Demon Beast Incarnadine combat!"
    $ clear_scene()
    $ renpy.choice_for_skipping()
    
    pause 1.0
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg

label story_642_6:
    $ preloadImages ([chara_sprites[k] for k in sprites_to_download["642_4"]] + [background_images[l] for l in backgrounds_to_download["642_4"]] + music_to_download["642_4"])
    $ clear_scene()
    $ renpy.choice_for_skipping()
    show bg boss_01_full with black_fade_in
    pause 1.5
    play sound "sfx/desummon.ogg"
    scene black with wipedown
    pause 2.0
    show bg castle_01_night with black_fade_in

    play music "audio/map_orleans_intro.ogg" noloop
    queue music "audio/map_orleans_loop.ogg" loop
    $ renpy.choice_for_skipping()
    jeanne_darc_2 normal "The path has been cleared! Please, keep moving forward, don't look back!"
    merlin_2 anger "The first Demon Beast Incarnadine has been silenced!"
    merlin_2 "I'd love for us to take a break, but we don't have time. I'm sorry."
    merlin_2 shout "Both of you, let's move onto the next one!"
    mash_3 anger "Understood!"
    first_hassan_2 normal "This way───follow me."
    elisabeth_1 joy "Get it together, you hear me!?"
    elisabeth_1 "There'll be hell to pay if you give up halfway through!"
    jeanne_darc_2 normal "Best of luck!"
    marie_2 joy "Vive la France!"

    $ clear_scene()
    $ renpy.choice_for_skipping()
    stop music fadeout 2.0
    scene black with black_fade_out
    hide bg
    pause 1.0


    scene
    jump menu_loop