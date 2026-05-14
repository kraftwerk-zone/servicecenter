"""
Nach mkdocs-static-i18n sortiert die Top-Level-Tabs alphabetisch nach Titel.
Hier die gewünschte Reihenfolge ohne Ziffern in den .pages-Titeln.

Locale-Index (*/index.md) wird aus der Tab-Navigation entfernt; Start-URLs leiten per JS weiter.
"""

from mkdocs.plugins import event_priority
from mkdocs.structure.pages import Page
from mkdocs.structure.nav import _add_parent_links, _add_previous_and_next_links, _get_by_type

_TOP_LEVEL_INDEX = frozenset(
    {
        "de/index.md",
        "en/index.md",
        "es/index.md",
        "it/index.md",
        "cs/index.md",
        "da/index.md",
    }
)

# Reihenfolge: FAQ → Handbücher/Manuals → ControlPanel → Tickets (pro Sprache bekannte Tab-Titel)
_TOP_LEVEL_ORDER = [
    # FAQ
    "Häufig gestellte Fragen",
    "Frequently Asked Questions",
    "Preguntas frecuentes",
    "Domande frequenti",
    "Často kladené otázky",
    "Ofte stillede spørgsmål",
    # Handbücher (mit/ohne .pages)
    "Handbücher",
    "Manuals",
    "02 Handbücher",
    # Control / Tickets (DE/EN + übersetzte .pages-Titel)
    "ControlPanel",
    "PanelDeControl",
    "PannelloDiControllo",
    "Ovládací panel",
    "Kontrolpanel",
    "Tickets",
    "Entradas",
    "Biglietti",
    "Vstupenky",
    "Billetter",
]


def _effective_top_title(item) -> str:
    return (item.title or "").strip()


def _top_level_sort_key(item):
    title = _effective_top_title(item)
    try:
        return (0, _TOP_LEVEL_ORDER.index(title))
    except ValueError:
        return (1, title.lower())


def _drop_top_level_locale_indices(items):
    out = []
    for item in items:
        if isinstance(item, Page) and item.file:
            uri = item.file.src_uri.replace("\\", "/")
            if uri in _TOP_LEVEL_INDEX:
                continue
        out.append(item)
    return out


@event_priority(-200)
def on_nav(nav, *, config, files):
    if not nav.items:
        return nav

    nav.items = _drop_top_level_locale_indices(nav.items)
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
    if nav.homepage is None and pages:
        nav.homepage = pages[0]

    return nav
