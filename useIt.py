import sublime
import sublime_plugin
import webbrowser


class useItCommand(sublime_plugin.TextCommand):

    """
    This will search a word or a selection.
    Default binding recommendation: "ctrl + alt + d"
    """

    def run(self, edit):
        word = self.view.substr(self.view.word(self.view.sel()[0].begin()))
        for region in self.view.sel():
            phrase = self.view.substr(region)
            search = 'http://caniuse.com/#search='
            if not region.empty():
                webbrowser.open_new_tab(search + phrase)
            else:
                webbrowser.open_new_tab(search + word)
