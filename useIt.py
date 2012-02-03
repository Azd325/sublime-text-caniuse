import sublime
import sublime_plugin
import webbrowser


class useItCommand(sublime_plugin.TextCommand):

    """
    This will search a word or a selection.
    Default binding recommendation: "ctrl + alt + d"
    """

    def run(self, edit):
        if len(self.view.file_name()) > 0:
            word = self.view.substr(self.view.word(self.view.sel()[0].begin()))
            for region in self.view.sel():
                phrase = self.view.substr(region)
                search = 'http://caniuse.com/#search='
                if not region.empty():
                    webbrowser.open_new_tab(search + phrase)
                else:
                    webbrowser.open_new_tab(search + word)
        else:
            pass

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
