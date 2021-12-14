# https://gist.github.com/tobek/a17fa9101d7e28ddad26
#  * open up chrome dev tools (Menu > More tools > Developer tools)
#  * go to network tab, refresh the page, wait for images to load (on some sites you may have to scroll down to the images for them to start loading)
#  * right click/ctrl click on any entry in the network log, select Copy > Copy All as HAR
#  * open up JS console and enter: var har = [paste]
#  * (pasting could take a while if there's a lot of requests)
#  * paste the following JS code into the console
#  * copy the output, paste into a text file
#  * open up a terminal in same directory as text file, then: wget -i [that file]
 

import json
from haralyzer import HarParser, HarPage

# Download the .har file from Developer tools(roughly the same as your operations), and we can parse it offline.
# Even if we have many image files to be download, it will not take too much time to wait to paste.
with open('source_har.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data["entries"]
image_urls = []

for entry in data:
    if entry["response"]["content"]["mimeType"].find("image/") == 0:
        image_urls.append(entry["request"]["url"])
     
# Save the URL list to a text file directly.
with open('target_link.txt', 'w') as f:
    for link in image_urls:
        f.write("%s\n" % link)