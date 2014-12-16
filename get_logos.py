#!/usr/bin/python

# Portion dealing with spritesheet creation modified from 
# http://oranlooney.com/make-css-sprites-python-image-library/ by Oran Looney.

import urllib, os, csv
from PIL import Image

def download_photo(img_url, filename):
    try:
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd() + '/pngs/'
            file_path = "%s%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            print filename + " failed to download"
            return False    
    except:
        print 'error while downloading ' + filename
        return False
    return True

with open('teams.csv', mode='rU') as infile:
    reader = csv.reader(infile)
    #row[6] is si's cdn id for each team. row[3] is flair css class
    teams = dict((row[6],row[3]) for row in reader)

base_url = 'http://cdn-png.si.com//sites/default/files/teams/basketball/cbk/logos/'
extension = '_30.png'

if not os.path.exists('pngs'):
    os.makedirs('pngs')

for team in teams:
    #print('%s%s%s' % (base_url, team, extension))
    download_photo('%s%s%s' % (base_url, team, extension), team+".png")

iconMap = []
for key, value in teams.iteritems():
    iconMap.append([value, key+'.png'])

images = [Image.open('pngs/'+team+'.png') for team in teams]
image_width, image_height = images[0].size
master_height = image_height
#seperate each image with 15 px of whitespace
master_width = ((image_width+15) * len(images) - 15)
master = Image.new(
    mode='RGBA',
    size=(master_width, master_height),
    color=(0,0,0,0))  # fully transparent

#print "created."

for count, image in enumerate(images):
    location = (image_width+15)*count
    #print "adding %s at %d..." % (iconMap[count][1], location),
    master.paste(image,(location,0))
    #print "added."
#print "done adding icons."

#print "saving master.png...",
master.save('logos.png')
#print "saved!"


cssTemplate = '''a[href="/%s"]:before,
.flair-%s:before {
    background-position: -%dpx 0;
    opacity: 1.0;
}
'''

#print 'saving logos.css...'
iconCssFile = open('logos.css' ,'w')
for count, pair in enumerate(iconMap):
    cssClass, filename = pair
    location = (image_width+15)*count
    iconCssFile.write( cssTemplate % (cssClass, cssClass, location) )
iconCssFile.close()
#print 'created!'