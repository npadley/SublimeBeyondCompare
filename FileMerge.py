import sublime, sublime_plugin, os, webbrowser, subprocess

fileA = fileB = None


def recordActiveFile(f):
    global fileA
    global fileB
    fileB = fileA
    fileA = f


class FileMergeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        if os.path.exists("/usr/bin/opendiff"):
            if fileA != None and fileB != None:
                OPENDIFF = '/usr/bin/opendiff'
                cmd_line = str(OPENDIFF) + ' "' + str(fileA) + '" "' + str(fileB) + '"'
                print("FileMerge comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
                subprocess.Popen([str(OPENDIFF), str(fileA), str(fileB)])
                print("Should be open...")
            else:
                print("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
                sublime.error_message("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")

        else:
            GOTHERE = sublime.ok_cancel_dialog('Could not find opendiff.\nPlease download and install Xcode', 'Do it now!')
            if GOTHERE:
                new = 2 # open in a new tab, if possible
                url = "https://developer.apple.com/xcode/download"
                webbrowser.open(url,new=new)
                XCODEINSTALLED = sublime.ok_cancel_dialog('Once you have installed Xcode, click the ok button to continue')
                if XCODEINSTALLED:
                    if os.path.exists("/usr/bin/opendiff"):
                        if fileA != None and fileB != None:
                            OPENDIFF = '/usr/bin/opendiff'
                            cmd_line = str(OPENDIFF) + ' "' + str(fileA) + '" "' + str(fileB) + '"'
                            print("FileMerge comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
                            subprocess.Popen([str(OPENDIFF), str(fileA), str(fileB)])
                            print("Should be open...")
                        else:
                            print("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
                            sublime.error_message("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")

                    else:
                        sublime.error_message('Still could not find opendiff. \nPlease make sure it exists at:\n/usr/bin/opendiff\nand try again')

                else:
                    sublime.error_message('Please try again after you have Xcode installed')

            else:
                sublime.error_message('Please try again after you have Xcode installed')


class FileMergeFileListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.file_name() != fileA:
            recordActiveFile(view.file_name())
