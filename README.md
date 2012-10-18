NotificationCenter
========

You can notify a message from Sublime Text 2 at any time.

## Installation

    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    $ git clone https://github.com/jugyo/SublimeNotificationCenter.git NotificationCenter

## Requirements

[terminal-notifier](https://github.com/alloy/terminal-notifier):

    $ gem install terminal-notifier

## Usage

In Console (<code>ctrl + \`</code>) or your plugin:

    view.run_command("notify", {"title": "foo", "message": "bar"})

Key Binding: `command + e, n`
