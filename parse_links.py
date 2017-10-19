# encoding=utf8

from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URL = (
    'http://python.org',
    'http://google.com'
)


def output(x):
    print '\n'.join(sorted(set(x)))


def simpleBS(url, f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))


def fasterBS(url, f):
    'fasterBS - use BeautifulSoup to parse only anchor tags'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parseOnlyThese=SoupStrainer('a')))


def htmlparse(url, f):
    'htmlparser() -use HTMLParse to parse anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)


def html5libparse(url, f):
    'html5libparse() - use htmllib to parse anchor tags'
    # urljoin 将url的相对路径转化为绝对路径
    output(urljoin(url, x.attributes['href']) for x in parse(f) if isinstance(x, treebuilders.simpletree.Element)
           and x.name == 'a')


def process(url, data):
    print '\n*** simple BS'
    simpleBS(url, data)
    data.seek(0)
    print '\n*** faster BS'
    fasterBS(url, data)
    data.seek(0)
    print '\n*** HTMLParser'
    htmlparse(url, data)
    data.seek(0)
    print '\n*** html5lib'
    html5libparse(url, data)


def main():
    for url in URL:
        f = urlopen(url)
        data = StringIO(f.read())
        soup = BeautifulSoup(data)
        # print soup.head
        print soup.a.get('title')
        # print data
        # prettify 将内容格式化输出
        # print BeautifulSoup(data).prettify()
        f.close()
        # process(url, data)

if __name__ == "__main__":
    main()

