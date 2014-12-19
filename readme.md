## Blackboard Orphan Content Remover
The idea for this script is to allow the client to remove the orphan content on a course by course base with their own acknowledgement.

We don't take responsability for the problems that this script may occur and should be use at client discretion.

Requirements
-------------------------------
This script depends on two files:
* Config (Configuration) File
* ID (Course IDS) File

In order to execute it you need to have install on your system the [easywebdav](https://github.com/amnong/easywebdav) that can easily be install with pip or easy_install.

How to execute it
--------------------------------
Here is an example of execution

    python orphan_content_remover.py -c vars.txt -i courses.txt
We are invoking python since we have not defined it in the path, so you can use any version at your own will.

Features
-----------------------------
* This script is based solely on the idea to remove the course home folder that is sometimes present after performing a CRS_REMOVE procedure from Snapshot
* This script uses Blackboard own WebDav Functionality
* This script requires a System Admin username and password
* This script uses LDAP or RDBMS to connect to Blackboard and can't be used with any Identity Provider like Shibboleth or CAS
* We have added comment lines to the files using the # at the **start** of the line
* We don't go into the folders, we are just deleting them
* We are not listing the contents, again just deleting them.

Version 1.0
---------------------------
* We have not enabled verbosity 
* We have not enabled logging
* We are not validating if the course home folder exists, we are just trying to delete it
* We don't care if there is any content inside the course home folder

