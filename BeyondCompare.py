import sublime, sublime_plugin, os, webbrowser, subprocess

fileA = fileB = None


def recordActiveFile(f):
    global fileA
    global fileB
    fileB = fileA
    fileA = f


class BeyondCompareCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        if os.path.exists("/usr/local/bin/bcompare"):
            if fileA != None and fileB != None:
                bCompareLocation = '/usr/local/bin/bcompare'
                cmd_line = str(bCompareLocation) + ' "' + str(fileA) + '" "' + str(fileB) + '"'
                print("BeyondCompare comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
                subprocess.Popen([str(bCompareLocation), str(fileA), str(fileB)])
                print("Should be open...")
            else:
                print("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
                sublime.error_message("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")

        else:
            commandLinePrompt = sublime.ok_cancel_dialog('Could not find bcompare.\nPlease install the command line tools.', 'Do it now!')
            if commandLinePrompt:
                new = 2 # open in a new tab, if possible
                url = "http://www.scootersoftware.com/support.php?zz=kb_OSXInstallCLT"
                webbrowser.open(url,new=new)
                bCompareInstalled = sublime.ok_cancel_dialog('Once you have installed the command line tools, click the ok button to continue')
                if bCompareInstalled:
                    if os.path.exists("/usr/local/bin/bcompare"):
                        if fileA != None and fileB != None:
                            bCompareLocation = '/usr/local/bin/bcompare'
                            cmd_line = str(bCompareLocation) + ' "' + str(fileA) + '" "' + str(fileB) + '"'
                            print("BeyondCompare comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
                            subprocess.Popen([str(bCompareLocation), str(fileA), str(fileB)])
                            print("Should be open...")
                        else:
                            print("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
                            sublime.error_message("You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")

                    else:
                        sublime.error_message('Still could not find bcompare. \nPlease make sure it exists at:\n/usr/local/bin/bcompare\nand try again')

                else:
                    sublime.error_message('Please try again after you have command line tools installed.')

            else:
                sublime.error_message('Please try again after you have command line tools installed.')


class BeyondCompareFileListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.file_name() != fileA:
            recordActiveFile(view.file_name())
