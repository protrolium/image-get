# image-get
image scraping technique with python using chrome dev-tools har collection

## instructions

* open up chrome dev tools (Menu > More tools > Developer tools)
* go to network tab, refresh the page, wait for images to load (on some sites you may have to scroll down to the images for them to start loading)
* right click/ctrl click on any entry in the network log, select Copy > Copy All as HAR
* open up JS console and enter: var har = [paste]
* (pasting could take a while if there's a lot of requests)
* paste the following JS code into the console
* copy the output, paste into a text file
* open up a terminal in same directory as text file, then: wget -i [that file]
