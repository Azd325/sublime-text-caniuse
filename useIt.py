import sublime 
import sublime_plugin

import sys
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
        s = sublime.load_settings("Can I Use.sublime-settings")
        default_browser = s.get('default_browser', '')

        if not default_browser and sublime.platform() == 'windows':
            default_browser = 'windows-default'

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


            browser = webbrowser.get(default_browser)
            browser.open_new_tab(BASE_URL + search)
