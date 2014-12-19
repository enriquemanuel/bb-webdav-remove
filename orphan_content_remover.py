import easywebdav
import logging, sys, argparse, gzip, os, datetime,socket

config = {}
courses = []

# main execution
# grabbing arguments from the command line
def main():
    parser = argparse.ArgumentParser(description='Remove Course Home Folders based on Course Id')
    # Configuring subparsers for actions
    parser.add_argument('-c', '--config', required=True,  help='Config File', type=str)
    parser.add_argument('-i', '--ids', required=True,  help='Course IDs File', type=str)

    args = parser.parse_args()
    # Set all the Vars
    return setVars(args)

# read and configure the variables from the arguments
# first I will read the arguments from the configuration file and instantiating in the global config
# then i will read the arguments from the course file and instantiating in the global courses file
def setVars(args):
    try:
        args.config
    except AttributeError:
        print "There is no config file that we could read. Please try again."
    else:
        if readConfig(args.config):
            try:
                args.ids
            except AttributeError:
                print "There is no course ids file that we could read. Please try again."
            else:
                if readCourseIds(args.ids):
                    global config
                    print config
                    #execute()

# function to read the file that contains all the configuration
# this comes from the config parameter and stores everything on a dictionary for easy access
# stores everything on the GLOBAL config dictionary
def readConfig(filename):
    with open(filename) as f:
        global config
        config = {}
        for line in f:
            if not str(line).startswith('#'):
                items = line.split(':', 1)
                config[items[0]] = items[1].rstrip('\n')
        #adding the default course path
        config['path'] = '/bbcswebdav/courses/'
        return 1


# function to read the file that contains all the list of course ids to delete
# this comes from the ids parameter and stores everything on a list to use in a for loop and deletion
# stores everything on the GLOBAL course list
def readCourseIds(filename):
    with open(filename) as f:
        global courses
        courses = []
        for line in f:
            if not str(line).startswith('#'):
                courses.append(line.rstrip('\n'))
        return 1


# function execute to read the values that were saved globally
# then it will initiate the webdav connection
# afterwards it will go over the list of courses in the for loop
# and delete all the courses path entirely
def execute():
    # loading global variables
    global config
    global courses

    # connecting to the webdav and instantiating the webdav variable
    webdav = easywebdav.connect(
        config['server'],
        username=config['username'],
        password=config['password'],
        protocol=config['protocol'])

    # navigating over the list of courses
    for courseid in courses:
        # removal of folders
        #webdav.delete( config['path'] + courseid )

        # go into the folder if we want to
        webdav.cd( config['path'] + courseid )


# start of the program
if __name__ == "__main__":
    main()
