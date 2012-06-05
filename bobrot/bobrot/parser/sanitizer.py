# coding: utf-8
import re
from BeautifulSoup import BeautifulStoneSoup
import unicodedata

class Sanitizer(object):

    def replace_bad_characters(self, str):
        """
        Osetruje konverzi na utf-8 a prevadi html entity na utf-8 pismena
        """

        str = unicode(BeautifulStoneSoup(str,
                                         convertEntities=BeautifulStoneSoup.HTML_ENTITIES))
        str = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
        str = unicode(re.sub('[^\w\s-]', '', str).strip().lower())
        str = unicode(str.replace(' ', '-'))
        return str
  
