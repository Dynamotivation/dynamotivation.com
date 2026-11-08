+++
title = "Redmond Calculator"
date = 2026-11-08
description = "A version of the Windows calculator built with Avalonia and .NET, using the open-source Windows Calculator engine. Free, open source, with a signed installer for Windows."

[taxonomies]
software-categories = ["Application", "Utility", "Open Source", "Windows"]
programming-languages = ["C#", "XAML"]

[extra.hub]
exposed = true
targets = { windows = ["x64"], macos = [], linux = [] }

[extra]
# Graphic enrichment
project_title = "Redmond Calculator"
date_label = "First released"
logo = "https://assets.dynamotivation.com/files/projects/redmond-calculator/logo.avif"
logo_width = 256
logo_height = 256
infobox_images = [
    { path = "https://assets.dynamotivation.com/files/projects/redmond-calculator/logo.svg", imageWidthPx = 512, imageHeightPx = 512, description = "Redmond Calculator application icon", radius = "20%" }
]
screenshot_urls = ["https://assets.dynamotivation.com/files/projects/redmond-calculator/screenshot-standard.avif"]
same_as = ["https://github.com/Dynamotivation/port-redmond-calculator"]

# JSON-LD SEO for Software
operatingSystem = "Windows"
# release_notes = derived from data/releases.json (newest entry); do not set by hand
programming_language = "C#, XAML"
development_environment = "Avalonia UI, .NET"
license = "MIT"
availability = "InStock"
application_category = "UtilitiesApplication"
price_usd = 0
#aggregate_rating = []

# FAQ
questions = [
    { question = "Which modes does it have?", answer = "Standard, scientific, programmer, graphing and date calculation, plus unit converters for volume, length, weight, temperature, energy, area, speed, time, power, data, pressure and angle, and a currency converter." },
    { question = "Do the keyboard shortcuts match Windows?", answer = "Mostly. The shortcut list comes from the Windows Calculator's own definitions. On macOS the Ctrl key becomes Command, and a few shortcuts that clash with macOS (such as history, memory store and subtract) use a Shift or Alt variant on every system. In Settings you can switch Command back to Ctrl." },
    { question = "Does it need an account or an internet connection?", answer = "There are no accounts and calculations run locally. The only network use is currency rates. Each rate source stays off until you agree to it in Settings, and only the latest rate table is requested. The amounts and currencies you enter are not sent." },
    { question = "Where does the calculation engine come from?", answer = "From Microsoft's open-source Windows Calculator, which is included unmodified as a pinned Git submodule and used under its MIT licence. Redmond Calculator adds the Avalonia interface and the code that connects the two." },
    { question = "Can I download it?", answer = "Yes. The Windows installer (64-bit, Windows 10 version 1607 or newer) is on GitHub Releases and in the Dynamotivation Software Hub. macOS and Linux builds are not published yet; the source code is on GitHub under the MIT licence and can be built with the steps in its README." }
]

+++

{% infobox(title="Redmond Calculator") %}
{{ infobox_images() }}
<dl>
    <dt>Part of</dt>
    <dd><a href="/portfolio/software/port-redmond/">Port Redmond</a></dd>
    <dt>Availability</dt>
    <dd>Available</dd>
    <dt>Development Environment</dt>
    <dd>Avalonia UI<br>.NET</dd>
    <dt>Written in</dt>
    <dd>C#<br>XAML</dd>
    <dt>Operating system(s)</dt>
    <dd>Windows 10 or newer (64-bit)</dd>
    <dt>Source code</dt>
    <dd><a href="https://github.com/Dynamotivation/port-redmond-calculator">Open source</a><br>MIT licence</dd>
</dl>
{% end %}

***Redmond Calculator*** is a version of the Windows calculator built with Avalonia and .NET. It is one of the first two applications in the [Port Redmond](/portfolio/software/port-redmond/) project, together with [Redmond Notepad](/portfolio/software/redmond-notepad/). The calculation engine is the open-source code of Microsoft's Windows Calculator, included unmodified, and Redmond Calculator adds an interface modeled on the original.


## Features

---

The current version has:

*   Calculator modes
    *   Standard, scientific, programmer, graphing and date calculation.
*   Converters
    *   Volume, length, weight, temperature, energy, area, speed, time, power, data, pressure and angle, plus currency.
*   History and memory
    *   A history pane and a memory panel.
*   Currency rates
    *   Four sources to choose from: the European Central Bank, the Federal Reserve H.10 tables, the Bank of Canada and Frankfurter. The app only contacts a source after you agree to it in Settings.
*   Appearance
    *   A light, dark or system theme and a choice of font. On macOS the window corners and window buttons can follow either Windows or macOS styles.


## Keyboard shortcuts

---

The shortcut list comes from the Windows Calculator's own definitions, including the mode switches and memory keys. On macOS the <kbd>Ctrl</kbd> key becomes <kbd>⌘</kbd>. A few shortcuts that would clash with macOS, such as history, memory store and memory subtract, use a <kbd>Shift</kbd> or <kbd>Alt</kbd> variant on every system. In Settings you can switch <kbd>⌘</kbd> back to <kbd>Ctrl</kbd>. Key names follow your keyboard language, so a German layout shows <kbd>Strg</kbd>.


## Availability

---

The Windows installer (64-bit, Windows 10 version 1607 or newer) is signed and published on [GitHub Releases](https://github.com/Dynamotivation/port-redmond-calculator/releases), and the Dynamotivation Software Hub offers it too. There are no macOS or Linux installers yet. The source code is on [GitHub](https://github.com/Dynamotivation/port-redmond-calculator) under the MIT licence, and the README has build steps for macOS and Windows. It also runs on Linux.

{{ legal_notice(paragraphs=[
    "This is an unofficial, independent, open source project inspired by the Windows calculator.",
    "Windows, Windows Calculator and related names and artwork are copyright or trademarks of Microsoft Corporation. The calculation engine is Microsoft's open-source Windows Calculator code, used under its MIT licence.",
    "All rights are reserved by their respective copyright holders. This work is not affiliated with, endorsed by or sponsored by Microsoft."
]) }}
