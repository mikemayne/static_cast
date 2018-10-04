import sublime
import sublime_plugin


class static_castCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for region in view.sel():
			if not region.empty():
				# Get the selected text
				s = view.substr(region)
				s = "static_cast<>({})".format(s)
				# Replace the selection with transformed static_cast<>(text)
				view.replace(edit, region, s)
				# TODO: move cursor into <>