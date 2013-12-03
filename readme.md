Run with your opml file as first argument.

The script sends a POST request to the Micro-reader for each url so it will be slow, this is to keep it independent of Micro-reader.

Remember to change localhost url in the script if you're running Micro-reader on a remote machine.

Requires "listparser" and "requests" libraries, available trough pip.