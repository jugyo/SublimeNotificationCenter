# Requirements:
#
# * terminal-notifier (gem install terminal-notifier)
#
# Usage:
#
#     view.run_command("notify", {"title": "foo", "message": "bar"})
#

import subprocess
import sublime, sublime_plugin

def notify(title='', message=''):
  subprocess.check_call(['terminal-notifier', '-title', title, '-message', message, '-activate', 'com.sublimetext.2'])

class NotifyCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    notify(title=args["title"], message=args["message"])
