Polygot
=======

A gettext version of: 
http://www.reddit.com/r/gamedev/comments/20ketu/introducing_polyglot_an_open_google_doc_with/

To-do
-----

 0. License?
 1. Fork it
 2. Build Scripts
 3. Fill out all the metadata in the .po and .pot files.
 4. Refresh data

Rebuilding everything
---------------------

Included is a small python script `csv2po.py` it requires the packages `unicodecsv` and `babel`.

After downloading each of the sheets as csv on the google doc, you'll need to update the headers to match
their ISO locale codes. E.g. ::

    STRING ID,DESCRIPTION,en_US,en_GB,fr,fr_CA,es,de,it,pt_PT,ru

Then, you'll want to run csv2po.py and it'll dump everything out into .po and .pot files. e.g. ::

    python csv2po.py src_csv/menu.csv src_csv/errors.py src_csv/gameplay.csv

