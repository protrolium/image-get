# image-get
image scraping technique with python using chrome dev-tools har collection

## instructions

* open up chrome dev tools (Menu > More tools > Developer tools)
* go to network tab, refresh the page, wait for images to load (on some sites you may have to scroll down to the images for them to start loading)
* right click/ctrl click on any entry in the network log, select Copy > Copy All as HAR
* save into a file named source_har.har
* execute python script `$ python image-get.py` to obtain and print a new file of the parsed urls
* open up a terminal in same directory as text file, then: wget -i [that file]
