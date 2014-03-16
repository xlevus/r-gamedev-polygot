from babel import Locale
from babel.messages.catalog import Catalog
from babel.messages.pofile import write_po
import os
import sys

import unicodecsv as csv


for arg in sys.argv[1:]:
    in_csv = open(os.path.abspath(arg))

    reader = csv.DictReader(in_csv)
    _, filename = os.path.split(arg)
    filetype, _ = os.path.splitext(filename)

    LANGS = {}

    template = Catalog()

    for row in reader:
        _id = row.pop('STRING ID')
        desc = row.pop('DESCRIPTION')
        en = row.pop('en_US')

        template.add(en, auto_comments=[_id], user_comments=[desc])

        for l, string in row.iteritems():
            locale = Locale(l)

            po = LANGS.setdefault(l, Catalog(locale=l))
            po.add(en, string, auto_comments=[_id], user_comments=[desc])

    with open('templates/%s.pot' % filetype, 'w') as pofile:
        write_po(pofile, template)

    for locale, catalog in LANGS.iteritems():
        try:
            os.makedirs('%s' % locale)
        except OSError:
            pass

        with open('%s/%s.po' % (locale, filetype), 'w') as pofile:
            write_po(pofile, catalog)


