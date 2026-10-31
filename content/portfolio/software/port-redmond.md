+++
title = "Port Redmond"
date = 2026-07-25
description = "A project to make versions of the Windows Calculator and Notepad for macOS and Linux. In development and not yet released."

# Custom splash template. A page's own `template` always wins over the
# `page_template` set by the parent section, so this one page opts out of the
# wiki layout while every other software project keeps it.
# This must stay a top-level key: Zola ignores `template` inside [extra].
template = "sections/software/port-redmond.html"

[taxonomies]
software-categories = ["Application", "Suite", "Upcoming", "Open Source", "Windows", "macOS", "Linux"]
programming-languages = ["C#", "XAML"]

[extra]
project_title = "Port Redmond"
alternate_name = "Port Redmond Project"
date_label = "Announced"
logo = "https://assets.dynamotivation.com/files/site/placeholder/iconBackground.svg"
infobox_images = []
screenshot_urls = []

# JSON-LD SEO for Software
operatingSystem = "macOS, Linux, Windows"
release_notes = "In development. Not yet released."
programming_language = "C#, XAML"
development_environment = "Avalonia UI, .NET"
license = "Free and open source"
availability = "PreOrder"
application_category = "UtilitiesApplication"
price_usd = 0
#aggregate_rating = []

# ---- Page content ----
# The whole page is built from the fields below. There is no markdown body:
# this is a splash page rather than an article, so adding an application or a
# platform difference is an edit here rather than in HTML.

tagline = "Calculator and Notepad for macOS and Linux, in development."
lede = "Port Redmond is an attempt to make a few everyday Windows apps available on macOS and Linux with a familiar layout."
intro = "The Windows Calculator and Notepad only run on Windows. Port Redmond builds versions of them with Avalonia and .NET so they can run on macOS and Linux. Redmond Calculator reuses the calculation engine of Microsoft's open-source Windows Calculator. Neither app has been released yet."
legal_notice = [
    "This is an unofficial, independent, open source project inspired by the Windows applications it brings to macOS and Linux.",
    "Windows and related names and artwork are copyright or trademarks of Microsoft Corporation.",
    "All rights are reserved by their respective copyright holders. This work is not affiliated with, endorsed by or sponsored by Microsoft."
]

shots = [
    { image = "https://assets.dynamotivation.com/files/projects/redmond-calculator/screenshot-standard.jpg", alt = "Redmond Calculator in standard mode" },
]

claims = [
    { title = "Familiar layout", body = "The interface is modeled on the Windows apps, so the layout looks familiar." },
    { title = "Window style options", body = "On macOS the Calculator can use macOS or Windows window corners and window buttons. Both are set in Settings." },
    { title = "Shortcuts", body = "The Calculator uses the Windows shortcuts. On macOS the Ctrl key becomes Command, and a setting switches it back." },
    { title = "No sign-in", body = "The Calculator has no accounts. It only goes online for currency rates, and only after you agree to it." },
]

differences = [
    { platform = "macOS, compared with Windows", rows = [
        { from = "Window buttons on the right", to = "Window buttons on the left (optional)" },
        { from = "Rounded Windows 11 corners", to = "macOS rounded corners (optional)" },
        { from = "Ctrl shortcuts, such as Ctrl + C and Ctrl + V", to = "Command shortcuts, such as Command + C and Command + V (can be switched back to Ctrl)" }
    ] },
]

apps = [
    { name = "Redmond Calculator", page = "/portfolio/software/redmond-calculator/", icon = "https://assets.dynamotivation.com/files/projects/redmond-calculator/logo.svg", summary = "Standard, scientific, programmer, graphing and date modes, plus unit and currency converters." },
    { name = "Redmond Notepad", page = "/portfolio/software/redmond-notepad/", icon = "https://assets.dynamotivation.com/files/projects/redmond-notepad/logo.svg", summary = "Plain text editing with find and replace, a status bar and encoding handling." },
]

# Also feeds the FAQ structured data inherited from the software page template.
questions = [
    { question = "What is Port Redmond?", answer = "A project to make versions of the Windows Calculator and Notepad that run on macOS and Linux." },
    { question = "Which applications are there?", answer = "Redmond Calculator and Redmond Notepad. Each has its own page." },
    { question = "Can I download it yet?", answer = "No. Nothing has been released. The source code of both apps is public on GitHub." },
    { question = "Does it cost anything?", answer = "No. The apps are free. The Calculator is under the MIT licence. The Notepad repository does not have a licence file yet." },
    { question = "Do I need an account?", answer = "The Calculator has no accounts. Its only network use is currency rates, and each rate source needs your consent first." },
    { question = "Does it run on Linux?", answer = "Yes. Both apps run on macOS and Linux." },
    { question = "Why not run the Windows versions?", answer = "The Windows versions are made for Windows. Redmond Calculator reuses the calculation engine of Microsoft's open-source Windows Calculator and adds a new Avalonia interface, so that it can run on other systems." },
    { question = "Do the keyboard shortcuts work?", answer = "In the Calculator, yes. It uses the Windows shortcuts, and on macOS the Ctrl key becomes Command, which you can change in Settings. The Notepad page describes its own shortcuts." },
    { question = "Are these official Microsoft applications?", answer = "No. Port Redmond is an independent project with no connection to Microsoft." },
    { question = "When will it be finished?", answer = "There is no date. Both apps are still in development." }
]

+++
