+++
title = "Dynamotivation Software Hub"
date = 2026-11-01
description = "A desktop launcher and toolbox for the Dynamotivation software on your device. It installs the latest versions, keeps an eye out for updates and brings everything to one place, in your operating system's own design."

[taxonomies]
software-categories = ["Application", "Utility", "Windows"]
programming-languages = ["Dart", "Flutter"]

[extra.hub]
exposed = true
targets = { windows = ["x64"] }

[extra]
# Graphic enrichment
project_title = "Dynamotivation Software Hub"
date_label = "First released"
logo = "https://assets.dynamotivation.com/files/projects/dynamotivation-software-hub/logo.webp"
logo_width = 512
logo_height = 512
infobox_images = [
    {
        path = "https://assets.dynamotivation.com/files/projects/dynamotivation-software-hub/logo.webp",
        imageWidthPx = 512,
        imageHeightPx = 512,
        description = "Dynamotivation Software Hub application icon",
        radius = "20%"
    }
]
screenshot_urls = []
same_as = ["https://github.com/Dynamotivation/dynamotivation-software-hub"]
operatingSystem = "Windows 10 or newer"
application_category = "UtilitiesApplication"
# release_notes = derived from data/releases.json (newest entry); do not set by hand
availability = "InStock"

# JSON-LD SEO for Software
license = "Freeware"
price_usd = 0
# No rating yet; an empty value keeps AggregateRating out of the JSON-LD
aggregate_rating = ""

# FAQ
questions = [
    {
        question = "What is the Dynamotivation Software Hub?",
        answer = "A launcher and toolbox for the Dynamotivation software packages installed on your device. One list shows everything the website publishes, with descriptions, versions and an update notice when something new is out."
    },
    {
        question = "Does it install software for me?",
        answer = "Yes. Every package arrives as a signed setup that installs for one user without asking for administrator rights, and the Hub opens it afterwards."
    },
    {
        question = "Does the Hub update itself?",
        answer = "Yes, through the same catalog it serves to you. When a newer version is available, pressing Update Hub downloads the new installer, verifies its checksum and restarts the Hub with it."
    },
    {
        question = "Does it run in the background?",
        answer = "Optionally. With the background setting on, closing the window keeps the Hub in the system tray, and it notices new versions about once an hour and tells you with a notification."
    },
    {
        question = "How does it respect my operating system?",
        answer = "The Hub is one frontend per operating system, using that system's own design language: Fluent on Windows, the Yaru design on Ubuntu. It follows dark and light mode, high contrast and reduced motion."
    },
    {
        question = "Is it private?",
        answer = "Yes. The Hub only reads the public catalog at dynamotivation.com. Nothing about you or your device is sent anywhere, and the cache it keeps is on your own disk."
    }
]
+++

{% infobox(title="Dynamotivation Software Hub") %}
{{ infobox_images() }}
<dl>
    <dt>Availability</dt>
    <dd>Available<br>Freeware on GitHub</dd>
    <dt>First release</dt>
    <dd>November 1, 2026</dd>
    <dt>Development environment</dt>
    <dd>Flutter</dd>
    <dt>Written in</dt>
    <dd>Dart</dd>
    <dt>Operating system(s)</dt>
    <dd>Windows</dd>
    <dt>Source code</dt>
    <dd><a href="https://github.com/Dynamotivation/dynamotivation-software-hub">GitHub</a></dd>
</dl>
{% end %}

***Dynamotivation Software Hub*** is a desktop launcher and toolbox for the software packages Dynamotivation publishes. Instead of hunting through releases pages, everything that is available sits in one list, with descriptions, versions, screenshots and a download for your platform. The Hub is freeware; the setups it offers are the same signed installers the website serves.

## Whatever the website lists

---

The catalog at dynamotivation.com is the single source. Software arrives in the Hub when the website publishes it, with its page, release notes and downloads; software that leaves the page fades out of the list. The list loads from a cache on disk first, so the Hub is usable offline and freshens up silently when the network is back.

## One place on your system

---

The Hub follows the design of your operating system: it looks at home on Windows 10 and 11, in light or dark mode, and honours high contrast and reduced motion where the system offers it. Everything works from the keyboard, too.

## Background updates

---

With *Keep running in background* on, the Hub sits in the system tray when you close its window. About once an hour it checks the catalog, and when a new version of any software appears it raises a notification. The Hub keeps itself up to date the same way: press *Update Hub*, it downloads and verifies the new installer and restarts with the new version. Everything it stages or caches it cleans up again.

## Availability

---

Download the signed Windows installer from [GitHub Releases](https://github.com/Dynamotivation/dynamotivation-software-hub/releases), or install any Dynamotivation software straight from the Hub once it is on the device. The first versions of the Hub shipped on November 1, 2026.
