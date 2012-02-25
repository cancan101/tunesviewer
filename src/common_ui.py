'''
Created on Feb 25, 2012

@author: alex
'''
import gtk
import logging
import glib

def start(program, arg):
    """
    Runs a program in the background.
    """
    import subprocess
    try:
        logging.debug(program + str(arg))
        # program may be something like program -a -b, so split spaces to args:
        subprocess.Popen(program.split(" ") + [arg])
        logging.debug("Execution of %s completed." % program)
    except Exception as e:
        logging.info(str(e))
        msg = gtk.MessageDialog(None, gtk.DIALOG_MODAL,
                    gtk.MESSAGE_ERROR,
                    gtk.BUTTONS_CLOSE,
                    "Error starting %s\n%s" % (program, e))
        msg.run()
        msg.destroy()
        
def openDefault(filename):
    """
    Opens file/url in the system default opener.
    """
    start("xdg-open", filename)
    

def markup(text, isheading):
    """
    Gives markup for name - for liststore.
    """
    if isheading:
        return "<u><i>%s</i></u>" % (glib.markup_escape_text(text))
    else:
        return glib.markup_escape_text(text)