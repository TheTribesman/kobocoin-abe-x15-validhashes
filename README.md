Kobocoin-Abe: a free block chain browser for Bitcoin-based currencies.
https://github.com/bitcoin-abe/bitcoin-abe

    Copyright(C) 2011,2012,2013 by Abe developers.
    Copyright 2014 by Matthew Mitchell
	Copyright 2015 by Leandro Machado
    License: GNU Affero General Public License, see the file LICENSE.txt.
    Portions Copyright (c) 2010 Gavin Andresen, see bct-LICENSE.txt.

Welcome to Kobocoin-Abe!
===============

This software reads the Kobocoin (KOBO) block file, transforms and loads the
data into a database, and presents a web interface similar to Bitcoin
Block Explorer, http://blockexplorer.com/.

Kobocoin-Abe draws inspiration from Kobocoin Block Explorer (BBE) and
BlockChain.info and seeks some level of compatibility with them but
uses a completely new implementation.

Installation
------------

Installation steps will be prepared here.

First of all you need your daemon running and install the python packages:

Step 1:
sudo apt-get install python-pip

Step 2:
sudo pip install construct scrypt pycrypto

Step 3:
sudo apt-get install dateutils

step 4:
Go to x15_hash and compile the x15 lib:
sudo python setup.py install

step5:
I suppose that you will install on MySQL, so let's create the database:

mysql -u root -p

Put your password for root and enter, you'll go to mysql Console, now do this commands:

create database abe;

CREATE USER 'abe'@'localhost' IDENTIFIED BY 'PASSWORD*';
NOTE: CHANGE THE PASSWORD FOR A PASSWORD OF YOUR CHOICE

grant all on abe.* to abe; 

step 5:
I suppose that you install on /home/explorer so let's do this:

cd /home/explorer/KobocoinExplorer

python -m python -m Kobocoin-Abe.abe --config /home/explorer/KobocoinExplorer/abe-load.conf

Now will load the blocks with some infos like this:
    block_tx 1 1
    block_tx 2 2
    ...
When finish, you need configure CGI, read the CGI GUIDE located here.


NovaCoin support depends on the ltc_scrypt module available from
https://github.com/CryptoManiac/bitcoin-abe (see README-SCRYPT.txt).

To use x15_hash you need apply your proper x15_hash function, for kobo just use
the x15_hash function provided on https://github.com/machado-rev/x15_hash_kobocoin

License
-------

The GNU Affero General Public License (LICENSE.txt) requires whoever
modifies this code and runs it on a server to make the modified code
available to users of the server.  You may do this by forking the
Github project (if you received this code from Github.com), keeping
your modifications in the new project, and linking to it in the page
template.  Or you may wish to satisfy the requirement by simply
passing "--auto-agpl" to "python -m Kobocoin-Abe.abe".  This option makes all
files in the directory containing abe.py and its subdirectories
available to clients.  See the comments in abe.conf for more
information.

Database
--------

For usage, run "python -m Kobocoin-Abe.abe --help" and see the comments in
abe.conf.

You will have to specify a database driver and connection arguments
(dbtype and connect-args in abe.conf).  The dbtype is the name of a
Python module that supports your database.  Known to work are psycopg2
(for PostgreSQL) and sqlite3.  The value of connect-args depends on
your database configuration; consult the module's documentation of the
connect() method.

You may specify connect-args in any of the following forms:

* omit connect-args to call connect() with no arguments

* named arguments as a JSON object, e.g.:
  connect-args = { "database": "abe", "password": "KOBOCOIN" }

* positional arguments as a JSON array, e.g.:
  connect-args = ["abe", "abe", "KOBOCOIN"]

* a single string argument on one line, e.g.:
  connect-args = /var/lib/abe/abe.sqlite

For JSON syntax, see http://www.json.org.

Slow startup
------------

Reading the block files takes much too long, several days or more for
the main KOBO block chain as of 2014.  However, if you use a persistent
database, Kobocoin-Abe remembers where it stopped reading and starts more
quickly the second time.

Replacing the Block File
------------------------

Kobocoin-Abe does not currently handle block file changes gracefully.  If you
replace your copy of the block chain, you must rebuild Kobocoin-Abe's database
or (quicker) force a rescan.  To force a rescan of all data
directories, run Kobocoin-Abe once with the "--rescan" option.

Web server
----------

By default, Kobocoin-Abe expects to be run in a FastCGI environment.  For an
overview of FastCGI setup, see README-FASTCGI.txt.

To run the built-in HTTP server instead of FastCGI, specify a TCP port
and network interface in abe.conf, e.g.:

    port 2750
    host 127.0.0.1  # or a domain name

Input
-----

To display Namecoin, NovaCoin, or any block chain with data somewhere
other than the default Bitcoin directory, specify "datadir" in
abe.conf, e.g.:

    datadir = /home/explorer/.namecoin

The datadir directive can include a new chain's basic configuration,
e.g.:

    datadir += [{
            "dirname": "/home/weeds/testnet",
            "chain":   "Weeds",
            "code3":   "WDS",
            "address_version": "o" }]

Note that "+=" adds to the existing datadir configuration, while "="
replaces it.  For help with address_version, please open doc/FAQ.html
in a web browser.

The web interface is currently unaware of name and proof-of-stake
transactions, but see namecoin_dump.py in the tools directory.

More information
----------------

Please see TODO.txt for a list of what is not yet implemented but
would like to be.

Forum thread: https://bitcointalk.org/index.php?topic=22785.0
Newbies: https://bitcointalk.org/index.php?topic=51139.0

Donations appreciated: 
1LeandroRqTJf4stf2uD3TeYDszenqNHfz (BTC)
FNbTYcs2xfFkrJT2eTzWDu15freq8ZJ8qK (KOBO)
