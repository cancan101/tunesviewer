import ParserBase
from common_ui import markup

class Parser(ParserBase.ParserBase):
    def addItem(self, title, author, duration, type, comment, releasedate,
            datemodified, gotourl, previewurl, price, itemid):
        """Adds item to media list."""
        item = [None,
                    markup(title, False),
                    author,
                    duration,
                    type,
                    comment,
                    releasedate,
                    datemodified,
                    gotourl,
                    previewurl,
                    price,
                    itemid]
        self.addItemHelper(item)