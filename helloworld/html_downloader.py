from urllib import request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        if request.urlopen(url).getcode() != 200:
            return None

        return request.urlopen(req).read()


