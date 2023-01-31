# seznat_archive
A tool that periodically archives the list of Czech judicial experts and court translators

The repo consists of two files: 

main.py - which downloads and labels the lists of Czech judicial experts and court translators in CSV format. Other formats can also be downloaded by editing the URLs (XML, JSON, XLS).

local.seznat.plist - a local launchd agent for MacOS which runs on the 1st day of every month @ 12:00 PM and downloads the given files. This allows for continual data gathering building a database for future research. For more information consult: https://www.launchd.info

Legal warnings:
The software is protected by a GNU General Public License v3.0. Consult the terms before use.
The judicial expert and court translator databases contain personal data. Any processing and use of the downloaded data must be done in accordance with personal data regulation, especially Regulation (EU) 2016/679 (GDPR). If in doubt, consult an attorney specialised in personal data protection law.
