import sys
import listparser, requests

if len(sys.argv) > 1:
	xml = sys.argv[1]
	opml = listparser.parse(xml)
	print('found %s feeds in %s' % (len(opml.feeds), xml))

	for feed in opml.feeds:
		req = requests.post("http://localhost:3000/channels", data={'url' : feed.url})
		print('[%s]' % req.status_code, feed.url)
else:
	print('no opml file specified.')