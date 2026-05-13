"""
Nach mkdocs-static-i18n sortiert die Top-Level-Tabs alphabetisch nach Titel.
Hier die gewünschte Reihenfolge ohne Ziffern in den .pages-Titeln.
"""

from mkdocs.plugins import event_priority
from mkdocs.structure.pages import Page
from mkdocs.structure.nav import _add_parent_links, _add_previous_and_next_links, _get_by_type

# Reihenfolge: zuerst DE-Bereiche, dann EN; unbekannte Titel zuletzt A–Z.
_TOP_LEVEL_ORDER = [
    "Startseite",
    "Häufig gestellte Fragen",
    "Handbücher",
    "ControlPanel",
    "Tickets",
    "Home",
    "Manuals",
]


def _effective_top_title(item) -> str:
    """Titel für Sortierung (Start-/Home-Seite: zuverlässig über src_uri, nicht is_homepage)."""
    if isinstance(item, Page) and item.file:
        uri = item.file.src_uri.replace("\\", "/")
        if uri == "de/index.md":
            return "Startseite"
        if uri == "en/index.md":
            return "Home"
    return (item.title or "").strip()


def _top_level_sort_key(item):
    title = _effective_top_title(item)
    try:
        return (0, _TOP_LEVEL_ORDER.index(title))
    except ValueError:
        return (1, title.lower())


@event_priority(-200)
def on_nav(nav, *, config, files):
    if not nav.items:
        return nav

    nav.items.sort(key=_top_level_sort_key)

    pages = _get_by_type(nav.items, Page)
    for page in pages:
        page.previous_page = None
        page.next_page = None
    _add_previous_and_next_links(pages)
    _add_parent_links(nav.items)

    nav.pages[:] = pages
    nav.homepage = None
    for page in pages:
        if page.is_homepage:
            nav.homepage = page
            break

    return nav
