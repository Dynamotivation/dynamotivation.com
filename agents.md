This file provides guidelines to agents working on this repository.
The rules in here are "house rules" and should be followed at all times unless the user instructs otherwise. You are allowed to suggest breaking rules where it makes sense.

# Description
This repository contains the css, html templates, js and other assets for a website build using the zola static site generator.

# Repository structure
- `content/` contains the markdown files for the website, which are rendered into html by zola. They can contain front matter in TOML format, which is used to provide metadata and configuration for the page.
- `data/` contains json files which are used to provide data for the templates.
- `static/` contains static assets such as css, js and images. These are copied as-is to the output directory during the build process. This also allows for the creation of custom html pages outside of the templating system, which can be useful for soft redirects of moved urls and other edge cases.
- `templates/` contains the html templates used to render the pages. These can include macros and shortcodes, which are reusable components that can be included in the markdown files or other templates.

# Code guidelines
Any and all changes should be accomplished using the vast templating system in zola, consisting of templates, macros and shortcodes. Be mindful to not confuse it with full blown terra. The syntax is similar, in some areas even compatible. When unsure consult the zola documentation.
Changes should mainly consist of html, css and config changes. You are to avoid js wherever possible. There are lots of advanced CSS features that have reached baseline support already. When considering a feature, search the web for examples powered "using css only" or "without js". Consult MDD to confirm a features availability.
JS should only be used to enhance the experience.

# Design guidelines
The goal of this website is to be simple in terms of appearance with just the right amount of being fun and bubbly without looking either too bland or too corporate. Rounded corners and vibrant yet pastel colors are commonplace.
Always consult with existing CSS files. Especially consider the CSS root and properties.

When introducing new values into CSS, use properly named variables instead of magic numbers within the css file.
Reuse existing variables within a file where it makes sense.
Variables that are meant for a specific component should be placed just above it within the css file. If dark mode requires tweaking of said variable, add a dark mode media query override to it instead of introducing a second one specifically for dark mode.

Logo images specifically should have a large border radius as already present in the codebase, since they are meant to look like app icons.
Other elements should have smaller but consistent radii in proximity to each other and within a visual hierarchy of nested cards.

# Reviewing CSS
When asked to review CSS, make sure the above rules are followed. Suggest changes to better align the CSS with above presented ideas before applying them.

# Building and running
Always test your changes.
To test your changes make sure to run the ".\zola build" command. Never run ".\zola serve".
To make sure your changes are actually reflected, read the "public" directory which contains the build output.

# Moving and renaming markdown files
Moving and renaming markdown files affects the url of the page, which can lead to broken links.
1. Search the project for links to the old url and update them to point to the new url.
2. Make sure to also create a file in the "static/" directory with the same directory structure and name as the old url, which contains a redirect page. This way, any existing links to the old url will still work and redirect to the new page.
3. Rename the associated markdown, html and css files.
4. Verify the new link and the old link lead to the correct page.

## Redirect format for moved URLs
When creating a redirect for a moved URL, use this format to match existing redirects on the site:
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url=/new-url/" />
    <meta name="robots" content="noindex" />
    <script>
      window.location.replace('/new-url/');
    </script>
    <title>Redirecting…</title>
  </head>
  <body>
    <p>Redirecting to <a href="/new-url/">/new-url/</a></p>
  </body>
</html>
```

**Key elements:**
- **`window.location.replace()`**: Redirects the browser and replaces the old URL in browser history
- **`meta http-equiv="refresh"`**: Fallback for browsers with JavaScript disabled
- **`meta name="robots" content="noindex"`**: Prevents search engines from indexing the old URL, protecting SEO during the migration. This ensures search authority builds on the new URL only.

## Legal notices on software pages
Pages for fan works or works that imitate a third-party style end with the `legal_notice` shortcode. It renders the text from `data-text` attributes via CSS, so brand names in the notice are not indexed. Keep every notice in the same four parts:
1. Lead (shown bold): "This is an unofficial, fan-made {tool|work|port} inspired by X."
2. Rights holders: "X and related names, characters and artwork are copyright or trademarks of Y." Add one factual sentence only if true (for example, original games required, users supply their own images, components made from scratch).
3. "All rights are reserved by their respective copyright holders. This work is not affiliated with or endorsed by Y or YoYo Games."
4. Engine credit when built with GameMaker: "Powered by GameMaker: Studio 1.4 Engine, copyright YoYo Games."
Paragraphs cannot contain double quotes (use single quotes). Pages using it: AOA, Sonic Mania, Joins the Battle, Misfit Pack. The Port Redmond splash page takes the same paragraphs from a `legal_notice` array in its front matter and renders them through the same `shortcodes/legal_notice.html` template. The notice styles live in `static/css/sections/portfolio/software/legal-notice.css`, which both the standard software page and the splash page load.
