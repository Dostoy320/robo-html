#!/usr/bin/env python

import time
import sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from parsing import TextParsing
from html_parser import convertTxtToHTML


class MyHandler(PatternMatchingEventHandler):

    # Specify types of files to watch
    patterns = ["*.txt"]

    def process(self, event):
        """
        event.event_type
            'created' | 'modified' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        # For debug - <<<<<REMOVE>>>>>
        print event.src_path, event.event_type

        # Get the filename from the event to use as new filename in html_parser
        textparsing = TextParsing()
        filename = textparsing.get_file_name_from_path(event.src_path)

        convertTxtToHTML(filename)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')

    observer.start()
    print "Observer Started"
    print "Watching /%s." % args[0]

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        sys.exit("\nShutting Down Observer")

    observer.join()
