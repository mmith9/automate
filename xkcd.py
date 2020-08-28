
import requests, bs4, os



next_url="https://xkcd.com/1/"


while next_url:
    res = requests.get(next_url)
    res.raise_for_status()
    xkcd = bs4.BeautifulSoup(res.text, 'html.parser')

    comic_elems=xkcd.select("#comic > img")
    if len(comic_elems)>0:
        #downoad image
        comic_img_attr=comic_elems[0].attrs["src"]
        comic_img_url="http:"+comic_img_attr
        print(f"downloading from {next_url} a {comic_img_url}")
        res=requests.get(comic_img_url)
        res.raise_for_status()
        #save image to disc
        comic_filename=os.path.basename(comic_img_attr)
        print(f"saving file {comic_filename}")
        comic_file=open(os.path.join("xkcd",comic_filename),"wb")
        for iter in res.iter_content(100000):
            comic_file.write(iter)
        comic_file.close()
    else:
        print("Error, no comic found on page")
        next_url=""

    next_elems=xkcd.select("#middleContainer > ul:nth-child(4) > li:nth-child(4) > a")
    if len(next_elems)>0:
        if next_elems[0].attrs["href"]=="#":
            next_url=""
        else:
            next_url="http://xkcd.com"+next_elems[0].attrs["href"]
    else:
        next_url=""



