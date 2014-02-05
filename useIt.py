import sublime_plugin
import re
import webbrowser

# Outside pattern compilation to have better performance for multi
# selection
CLEAN_CSS_PATTERN = re.compile(r'([a-z-]+)', re.IGNORECASE)
BASE_URL = 'http://caniuse.com/#search='


class UseItCommand(sublime_plugin.TextCommand):
    """
    This will search a word or a selection.
    Default binding recommendation: "ctrl + alt + d"
    """

    def run(self, edit):
        for region in self.view.sel():
            # Get the start point of the region of the selection
            point = region.begin()
            scope = self.view.extract_scope(point)
            search = self.view.substr(scope)

            # Clean the selection on css syntax
            if "/CSS" in self.view.settings().get('syntax'):
                re_search = CLEAN_CSS_PATTERN.search(search)
                if re_search:
                    search = re_search.group()
            print(webbrowser._tryorder)
            print(webbrowser._browsers.items())
            webbrowser.open_new_tab(BASE_URL + search)
