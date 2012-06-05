# coding: utf-8
import os

from bobrot.bobrot.parser.feed import Article, FeedMeta
from webstemmer.htmlparser3 import HTMLParser3
from difflib import SequenceMatcher
#from webstemmer.analyze import cluster

#from webstemmer.textcrawler import HTMLLinkFinder, wash_url

class ArticleParse(object):
    """
Refactoring na Downloader

    Ma za ukol vytvorit dva tasky.
        1) Na stazeni html at uz pomoci wgetu ci neceho jineho.
        2) Vytvorit task na parsovani stazeneho html

    """

    def __init__(self, project_path, article, feed_meta):
        assert isinstance(article, Article)
        assert isinstance(feed_meta, FeedMeta)

        self.project_path = project_path
        self.article = article
        self.feed_meta = feed_meta

    def call(self):
        self._wget()
        artdif = ArticleDiff.get_diff()
        return self.parse(self.get_filename())

    def _wget(self):
        wget_args = self.build_args()
        self._create_fs_structure(self.get_filename())

        os.system(' '.join(wget_args))


    def parse(self, filename):
        """
        Tato metoda spusti parser, ktery vrati clanek.
        V tuto chvili vola tridu ArticleExtract, viz. komentar u tridy
        """
        with open(filename, 'r') as file:
            data = file.read()

        return unicode(data.decode('utf-8', 'replace'))

    def build_args(self):
        args = [
            'wget',
            '%s' % self.article.url,
            '-O %s' % self.get_filename(),
            ' --convert-links'
        ]

        return args

    def get_filename(self):
        """
        Vrací absolutní cestu k souboru
        """
        return '/'.join([
            self.project_path, self.feed_meta.domain,
            self.feed_meta.created_as_string,
            '/html/'
            '%s.html' % self.article.title
        ])

    def _create_fs_structure(self, filename):
        """
        TODO toto presunout do samostatne tridy at se to da testovat
        filename je cela cesta k souboru vcetne adresarove struktury :]
        """
        parts = os.path.split(filename)
        try:
            os.makedirs(parts[0], mode=0770)
        except OSError:
            # Struktura jiz existuje
            pass

    def get_api_article(self):
        """
        Vrati instanci naplneneho bobrot.bobrot.parser.feed.Article
        """
        pass


class Extractor(object):
    """

    Tato trida dostava nazev html souboru a snazi se z nej dostat clanek/plaintext bez nadpisu (nadpis se bere z RSS feedu).
    Pro porovnani layoutu je treba nacist poslednich 10 clanku ze stranky
    """

    def get_plain_text(self, filename):
        """
        Funkce vraci plaintext clanku, jako parametr dostava absolutni cestu ke stazenemu html;
        wrapper pro _extract;

            @TODO: zjistuje jestli soubor existuje
        """
        self.filename = filename
        self.plaintext = self._extract()
        return self.plaintext

    def _extract(self):
        """
        Za pouziti ruznych metod (_webstemmer, statistiku, diff ...) vraci plaintext
        """


        pass

    def _webstemmer(self):
        """
        Doresit odkud se bude brat webstemmer, jestli ho dat do virtualenvu nebo predelat na model (nebo neco jinyho)
        Licence to umoznuje http://www.unixuser.org/~euske/python/webstemmer/#license
        """
        # webstemmer mi zatim nejako nefucka, nemuzu ho tady zavolat :(
        #ws = webstemmer.crow
        hp = HTMLParser3

        pass

class ArticleDiff(object):

    def diff_files(self,filepaths):
        """
        Dostane seznam cest k souborum z poslednimi 10ti clanky z domeny/RSS feedu
        """

        for filepath in filepaths:
            Article.content = self.get_diff()
        pass

    def get_diff(self,filepath1,filepath2):
        """
        Porovna dva soubory; diff -abBiwn file1 file2
        Vraci rozdil oproti file1, cili obsah file2 ; volat i file2 file1
        Zabalit do try a catch
        """
        self.file1 = open(filepath1, 'r').read()
        self.file2 = open(filepath2, 'r').read()

        # Asi volat ve forcyklu zrejme pro vice nez jeden soubor, pro porovnani s vice
        # tohle se odladi pozdeji
        self.diff_file1 = os.system(' '.join(build_diffcmd(self, self.file2, self.file2)))
        self.diff_file2 = os.system(' '.join(build_diffcmd(self, self.file1, self.file2)))

        # Vola systemovy html2text (podobne jako u diffu), vraci o neco lepsi vysledky
        self.text_file1 = os.system(' '.join(build_html2text(self, self.file1)))
        self.text_file2 = os.system(' '.join(build_html2text(self, self.file2)))

        #diff -abBwin file1.html file2.html | html2text -o -
        #varci slusny diff, zbavit se re.sub(s/(^[.*].JPG\|jpg))
        #doladit, bude delat problem u specialnich rubrik, koktejl atd.
        return self.file1

    def build_diffcmd(self, file1, file2):
        diffcmd = [
            'diff',
            '-abBiwn',
            '%s' % file1,
            '%s' % file2,
            '|',
            'html2text',
            '%s' % file,
            '-o -',
        ]
        return diffcmd

    def build_html2text(self, file):
        html2textcmd = [
            'html2text',
            '%s' % file,
            '-o -',
        ]
        return html2textcmd

    def build_args(self):
        pass