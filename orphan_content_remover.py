import easywebdav
import logging, sys, argparse
import requests

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
        print("There is no config file that we could read. Please try again.")
    else:
        if readConfig(args.config):
            try:
                args.ids
            except AttributeError:
                print("There is no course ids file that we could read. Please try again.")
            else:
                if readCourseIds(args.ids):
                    global config
                    
                    execute()

# function to read the file that contains all the configuration
# this comes from the config parameter and stores everything on a dictionary for easy access
# stores everything on the GLOBAL config dictionary
def readConfig(filename):
    #filen = os.path.join(os.path.dirname(p), [path2], [...])
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

# python recipe
# taken from: http://code.activestate.com/recipes/577058/
# this is a simple yes or no question
def query_yes_no(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


# function execute to read the values that were saved globally
# then it will initiate the webdav connection
# afterwards it will go over the list of courses in the for loop
# and delete all the courses path entirely
def execute():
    # loading global variables
    global config
    global courses

    # need to build sanity check
    # send confirmation to client
    if query_yes_no('Are you sure you want to delete **' + str(len(courses)) + '** course(s)?: '):
        # connecting to the webdav and instantiating the webdav variable
<<<<<<< HEAD
        print 'Thanks for your confirmation. We will start deleting the courses now.'
=======
        print('Thanks for your confirmation. We will start deleting the courses now.')
>>>>>>> FETCH_HEAD
        webdav = easywebdav.connect(
            config['server'],
            username=config['username'],
            password=config['password'],
            protocol=config['protocol'])

        # navigating over the list of courses
        for courseid in courses:
            # removal of folders
            webdav.delete( config['path'] + courseid )

            # go into the folder if we want to
            #webdav.cd( config['path'] + courseid )
    else:
        # safe exiting
<<<<<<< HEAD
        print 'Thanks for your confirmation. We are not deleting anything now.'
=======
        print('Thanks for your confirmation. We are not deleting anything now.')
>>>>>>> FETCH_HEAD

# start of the program
if __name__ == "__main__":
    main()
