+++
title = "All-Out Attack Generator"
date = 2021-09-05
description = "Make Persona-esque All-Out Attack finishers for free. Add your own characters and artwork, then export PNG sequences on any platform, or GIF and video on Windows."

[taxonomies]
software-categories = ["App", "Android", "Windows"]
programming-languages = ["GML"]

[extra.hub]
exposed = true
targets = { windows = ["x86"], macos = [], linux = [] }

[extra]
project_title = "All-Out Attack Generator"
date_label = "First released"
logo = "https://assets.dynamotivation.com/files/projects/all-out-attack-generator/logo.webp"
logo_width = 512
logo_height = 512
infobox_images = [
    {
        path = "https://assets.dynamotivation.com/files/projects/all-out-attack-generator/logo.webp",
        imageWidthPx = 512,
        imageHeightPx = 512,
        description = "All-Out Attack Generator logo",
        radius = "20%"
    }
]
screenshot_urls = []
same_as = ["https://github.com/Dynamotivation/All-Out-Attack-Generator"]
application_category = "DesignApplication"
release_notes = "Latest release (see the release notes below)."
availability = "InStock"


# JSON-LD SEO for Software
operatingSystem = "Windows, Android, Web browser"
programming_language = "GML (GameMaker Language)"
development_environment = "GameMaker Studio 1.4"
license = "Closed Source"
price_usd = 0
# No rating yet; an empty value keeps AggregateRating out of the JSON-LD
aggregate_rating = ""

# FAQ
questions = [
    {
        question = "What is the All-Out Attack Generator?",
        answer = "A free animation maker for Persona-esque All-Out Attack finishers. You add your own characters and kill splash artwork, and it renders the animated sequence for you."
    },
    {
        question = "Does it cost anything?",
        answer = "No, it is freeware. The source code is closed."
    },
    {
        question = "Is the All-Out Attack Generator available for download?",
        answer = "Yes. You can get the Windows (32-bit portable executable) and Android (APK) builds from GitHub Releases, or use the browser version online."
    },
    {
        question = "How many characters can I use?",
        answer = "You can use up to four images for the teammates and four for the enemies, plus the artwork for the final kill splash."
    },
    {
        question = "What can I export?",
        answer = "PNG sequences on every platform, a PNG strip on Android, and GIF or video on Windows. GIF and video export on Windows needs the optional FFmpeg and OpenH264 downloads."
    },
    {
        question = "Is it available in other languages?",
        answer = "Yes, thanks to community translations in German, Spanish and French."
    },
    {
        question = "What is the tech stack for All-Out Attack Generator?",
        answer = "GML (GameMaker Language), GameMaker Studio 1.4, exported to Windows (32-bit), Android and HTML5."
    }
]
+++

{% infobox(title="All-Out Attack Generator") %}
{{ infobox_images() }}
<dl>
    <dt>Availability</dt>
    <dd>Available<br>Freeware on GitHub</dd>
    <dt>Initial completion</dt>
    <dd>September 5, 2021</dd>
    <dt>Development environment</dt>
    <dd>GameMaker Studio 1.4</dd>
    <dt>Written in</dt>
    <dd>GML (GameMaker Language)</dd>
    <dt>Operating system(s)</dt>
    <dd>Windows (32-bit)<br>Android<br>Browser</dd>
    <dt>Source code</dt>
    <dd>Private<br>Closed Source</dd>
</dl>
{% end %}


***All-Out Attack Generator*** is a free animation maker by Dynamotivation for creating All-Out Attack animations in a Persona-esque style. Users bring their own characters and kill splash artwork, and it renders the animation they know from the game. It was first released in September 2021 for Windows and Android, and you can also use it in a browser.


## Development

---

The project started after [Mix and Jam](https://www.youtube.com/watch?v=TyJJmlnoJX8) recreated the All-Out Attack effect in Unity. The effect has such a distinctive look that it made a good excuse to try real 3D in GameMaker, beyond simple plane projections.

The animation opens with a mirror breaking into shards, so those shards had to be real 3D elements. Work started around June or July, and the 3D was working by mid-August 2019. Then the project went quiet for a long while. Writing custom UI components with arbitrary sizes, lengths and translations, while targeting HTML5 for the first time, turned out to be difficult. Version 1.0.0 finally shipped on September 5, 2021.

The menus use a toned down style of *P5*.

<div class="blogVideoList blogVideoList-side-by-side">
{{ blog_video(
    url="TyJJmlnoJX8",
    title="Mix and Jam recreating the All-Out Attack effect in Unity",
    description="Mix and Jam's episode recreating the All-Out Attack effect in Unity, which inspired the project."
) }}
{{ blog_video(
    url="n6sGM67Qxcw",
    title="The Daphinator creating a custom All-Out Attack",
    description="The Daphinator's video on creating a custom All-Out Attack animation."
) }}
</div>


## Challenges

---

During the development of *All-Out Attack Generator* a few challenges arose:

*   Fly-in math for a fully customizable splash screen
    *   The fly-ins had to work wherever the artwork is placed, the layering had to hold up, and performance had to stay smooth. Texture assets scale to each device.
*   Faking the light shimmer of the original
    *   A texture is UV-projected across four tiles to recreate the shimmer.
*   Sprite outlines
    *   Drawing sprites repeatedly, offset by a few pixels per axis, produced jagged edges. Now the sprites are padded so the border still fits the texture page, and a shader draws the outline. It is derived from a Gaussian blur with the alpha pass stripped and the output forced to white, followed by a second pass for softer edges. Dynamotivation wrote the shader without any prior knowledge of GLSL.
*   Custom UI components and the first HTML5 export
    *   Flexible sizes, lengths and translations on the web target caused the long pause in development.


## Features

---

Here is what the latest version can do:

*   Character uploads
    *   Add up to four images for the teammates and four for the enemies.
*   Kill splash artwork
    *   An arranger editor places the artwork and sets how it flies in.
*   Settings
    *   Optimization options, anti-aliasing and a non-red color scheme. The original runs at 30 fps, while the generator can export 60 fps with interpolation.
*   Exporting
    *   PNG sequences everywhere, a PNG strip on Android, and GIF and video on Windows. The Windows GIF and video export needs the optional FFmpeg and OpenH264 downloads.
*   Languages
    *   Translations in German, Spanish and French, thanks to the community members who made them.


## Availability

---

You can get the Windows and Android builds as freeware from [GitHub Releases](https://github.com/Dynamotivation/All-Out-Attack-Generator/releases), or use the [browser version](https://dynamotivation.github.io/All-Out-Attack-Generator-Web/) online. The source code is private. A revival of the project is planned, and it is meant to stay cross-platform.

A big thank you to [The Daphinator](https://www.youtube.com/@TheDaphinator) for featuring the generator in a [YouTube Short](https://www.youtube.com/shorts/xIT_cD-Xh30) and in the [full video](https://www.youtube.com/watch?v=n6sGM67Qxcw) shown above.


## Lessons Learned

---

Making *All-Out Attack Generator* taught Dynamotivation plenty beyond the tool itself:

*   How to design a themed menu from a game's design language
*   How to handle translation of software
*   How to use 3D in GameMaker beyond simple plane projections
*   How to export video on Windows, including compiling FFmpeg and building C code with a non-Microsoft toolchain

{{ legal_notice(paragraphs=[
    "This is an unofficial, fan-made tool inspired by the All-Out Attack animation and menu style of Persona 5.",
    "Persona, Persona 5 and related names, characters and artwork are copyright or trademarks of ATLUS and SEGA. All assets were made from scratch and recreated by eye, by hand. Users supply their own character images.",
    "All rights are reserved by their respective copyright holders. This work is not affiliated with or endorsed by ATLUS, SEGA, or YoYo Games.",
    "Powered by GameMaker: Studio 1.4 Engine, copyright YoYo Games."
]) }}
