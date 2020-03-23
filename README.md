# Repo-Auto-Pull
A Script made to pull files from a repo every [amount] of hours.

I made this script for my FiveM Server so it would pull the updated files every 6 hours.
The Timer can be removed and the script can be added to your start.bat which would look something like this: 
```
cd /d C:\myServer\cfx-server-data
python autopull.py 
Stop (like ctrl+c) autopull.py after 90s
C:\myServer\run.cmd +exec server.cfg
```
The ```Stop (like ctrl+c) autopull.py after 90s``` allows for the files to pulled from the REPO.

This script can be used for any application, Allowed many developers to upload to your REPO and the new version being updated on your server every [amount] of hours

