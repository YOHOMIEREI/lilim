# Lilim Harlot

FGO Arcade visual novel made in [renpy 7.5](https://github.com/renpy/renpy). Available to play at (https://rayshift.io/lilim-harlot/).

<img src="https://i.imgur.com/7SeNglB.jpeg" />

## Assets
Images and sound protected under copyright are not included within this repository, you must source your own images, backgrounds, music and sound effects. This repository is intended for reference only and without these files you will not be able to run the game.

## Licence
The engine code is MIT licenced. The story text (anything in game/story folder) is our translation and may not be reproduced without permission. For example, you may use the code to make your own story or translation, but cannot build this app with our translation and publish it yourself. If copying portions of story text into forums please credit us (Rayshift translation team) and/or link the app.

## Building
1. Download renpy and renpyweb if you wish to build for web. 7.5 (7.4-nightly as of writing) is supported.
2. Add your own assets and story. `image_map_processed.py` contains a reference for images and music for the final FGO arcade singularity.
3. As of May 2022 renpy does not have video support for web applications. This can be worked around with some patches (`00-WebBuilder.patch`, `01-Index.patch`) to a couple of renpy engine files - you will need to apply these manually to your version of renpy.
