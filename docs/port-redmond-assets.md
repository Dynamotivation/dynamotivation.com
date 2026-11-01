# Port Redmond — assets

All artwork is served from the assets repository at
`https://assets.dynamotivation.com/files/`, following the existing
`files/projects/<slug>/` convention.

## In place

| Asset | Path on the CDN |
| --- | --- |
| Redmond Calculator icon | `files/projects/redmond-calculator/logo.svg` (and `.png`) |
| Redmond Notepad icon | `files/projects/redmond-notepad/logo.svg` (and `.png`) |
| Redmond Calculator screenshot | `files/projects/redmond-calculator/screenshot-standard.jpg` |
| Shared placeholder mark | `files/site/placeholder/iconBackground.svg`, `iconForeground.svg` |

The icons and the screenshot come from the application repositories
(`port-redmond-calculator`, `port-redmond-notepad`). They are original
artwork and genuine screenshots of the Avalonia builds, so they can ship.

The placeholder mark is the icon an unannounced project uses before its own
artwork exists. It was dropped when media moved to the CDN and has been
restored here, since it is a site-wide asset rather than a one-off.

## Still outstanding

**A Redmond Notepad screenshot.** The banner is built to hold more than one
window, but only Calculator has been photographed. Adding
`files/projects/redmond-notepad/screenshot-<name>.jpg` and a second entry in
the `shots` list of `content/portfolio/software/port-redmond.md` is all that
is needed; the banner reflows on its own.

**A Port Redmond mark of its own.** The umbrella page currently borrows the
shared placeholder icon for its grid card. The applications imitate Windows;
the project itself does not, so its mark is the one place the project gets to
look like its own thing.

Neither gap is caught by the pre-commit hook, because both are real assets
rather than files carrying the placeholder token. They have to be remembered.

## Screenshot requirements

For consistency with the Calculator shot already in place:

- Shot on Windows, so a visitor can compare against what they already use
- Dark theme, matching the existing one
- Windowed, never full screen — the window chrome is the evidence
- No personal data: no real file names, paths or account names
- Shot at 2× and downscaled, never upscaled
