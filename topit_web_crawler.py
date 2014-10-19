#@PydevCodeAnalysisIgnore
#Auto download first n=10 pages thumbnails of topit.me, do not use this program maliciously
import urllib
import re,os
from urllib import urlretrieve
def get_href_list(urlStr):
    hrefCmp = re.compile("""[src|date-original]="(http://[f|i][\w|\d]\d*.to.*?jpg)\"""")  #ok
    return hrefCmp.findall(urlStr)

def save_img_place(local_path):
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    return local_path

def getImages(myurl,save_place):
    imgSum = 0
    badImg = 0
    urlStr = urllib.urlopen(myurl).read()
    href_list=get_href_list(urlStr)
    save_drive=save_img_place(save_place)
    for href in href_list:
            print href
            imageName = href[href.rindex("/")+1:]
            try:
                urllib.urlretrieve(href, os.path.join(save_drive,imageName))
                imgSum += 1
                print imageName + "    OK"
            except :    #default
                print "cannot download this image: "+imageName
                #print href
    print "Success: ",imgSum

if __name__ == "__main__":
    for i in range(10):
     imgurl = "http://www.topit.me/?p="+str(i)
     getImages(imgurl,"E:\\img_thumbnail_topit")
     print "finish"