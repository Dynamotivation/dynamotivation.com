+++
title = "Redmond Notepad"
date = 2026-07-25
description = "A version of the Windows notepad built with Avalonia for macOS and Linux, with tabs, find and replace, a status bar and encoding handling."

[taxonomies]
software-categories = ["Application", "Utility", "Upcoming", "Open Source", "macOS", "Linux", "Windows"]
programming-languages = ["C#", "XAML"]

[extra]
# Graphic enrichment
project_title = "Redmond Notepad"
date_label = "Announced"
logo = "https://assets.dynamotivation.com/files/projects/redmond-notepad/logo.svg"
infobox_images = [
    { path = "https://assets.dynamotivation.com/files/projects/redmond-notepad/logo.svg", imageWidthPx = 512, imageHeightPx = 512, description = "Redmond Notepad application icon", radius = "20%" }
]
screenshot_urls = []

# JSON-LD SEO for Software
operatingSystem = "macOS, Linux, Windows"
release_notes = "In development. Not yet released."
programming_language = "C#, XAML"
development_environment = "Avalonia UI, .NET"
license = "Open source, licence not yet finalised"
availability = "PreOrder"
application_category = "UtilitiesApplication"
price_usd = 0
#aggregate_rating = []

# FAQ
questions = [
    { question = "Does it have tabs?", answer = "Yes. Files open in a new tab by default, and you can change that in Settings to open them in a new window instead." },
    { question = "Does it keep my work if it closes unexpectedly?", answer = "It saves your open tabs and unsaved text as you work, so it can restore them after a crash. In Settings you can also choose to continue your previous session when Notepad starts." },
    { question = "Does it handle line endings and encodings like Windows notepad?", answer = "It reads CRLF, LF and CR line endings, detects the file's encoding (including byte order marks) and shows both in the status bar. A file is saved in the encoding it was opened with." },
    { question = "Can I print?", answer = "On macOS and Windows, yes, using the system's own print dialogs with Notepad's header and footer fields. Printing is not available on Linux yet." },
    { question = "Does it check spelling?", answer = "Yes, using the spell checker of your system, and you can switch it on or off per file type in Settings." },
    { question = "Can I download it?", answer = "Not yet. Nothing has been released." }
]

+++

{% infobox(title="Redmond Notepad") %}
{{ infobox_images() }}
<dl>
    <dt>Part of</dt>
    <dd><a href="/portfolio/software/port-redmond/">Port Redmond</a></dd>
    <dt>Availability</dt>
    <dd>In development</dd>
    <dt>Development Environment</dt>
    <dd>Avalonia UI<br>.NET</dd>
    <dt>Written in</dt>
    <dd>C#<br>XAML</dd>
    <dt>Operating system(s)</dt>
    <dd>macOS<br>Linux<br>Windows</dd>
    <dt>Source code</dt>
    <dd>Open source<br>Licence not finalised</dd>
</dl>
{% end %}

***Redmond Notepad*** is a version of the Windows notepad built with Avalonia for macOS and Linux. It is one of the first two applications in the [Port Redmond](/portfolio/software/port-redmond/) project, together with [Redmond Calculator](/portfolio/software/redmond-calculator/). It has tabs, find and replace, a status bar and encoding handling.

## Features

---

Plain text editing, with:

*   Tabs, and the option to open files in a new window instead
*   Find, find next and previous, replace, and go to line
*   Word wrap and zoom from 10% to 500%
*   A status bar with the cursor position, zoom level, line endings and encoding
*   CRLF, LF and CR line endings, and encoding detection that keeps byte order marks
*   Recovery of open tabs and unsaved text after a crash
*   A recent files list
*   Spell checking with your system's spell checker
*   Printing on macOS and Windows with header and footer fields
*   A light, dark or system theme and a choice of font

## Keyboard shortcuts

---

Redmond Notepad uses the Windows shortcuts on every system, with one change: replace is <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>H</kbd>, because <kbd>⌘</kbd> + <kbd>H</kbd> hides apps on macOS. On macOS the <kbd>Ctrl</kbd> key becomes <kbd>⌘</kbd>, so a new tab is <kbd>⌘</kbd> + <kbd>N</kbd>. In Settings you can keep <kbd>Ctrl</kbd> instead. Key names follow your keyboard language, so a German layout shows <kbd>Strg</kbd>.

## Status

---

Nothing has been released yet, and there is no download.
