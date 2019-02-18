

user_list = [
    {'name': 'admin',
     'password': "password",
     'logged_in': False,
     'type': 'admin',
     'last_Logged_in_at': 'ddkd'},

]


def login():
    """Method to login user 
    
    Returns:
        [True] -- [For a succeful login]
    """

    username = username_prompt()
    password = password_prompt(username)
    if validate_username_password(username, password):
        print("Login success, Welcome {}".format(username))
        return True
    return login()


def validate_username_password(username, password):
    """Validate that a the user and password exists in the users list
    
    Arguments:
        username {[string]} -- [user you are trying to login ]
        password {[string]} -- [User password]
    
    Returns:
        [True] -- [For succees]
        [False] -- [For Failuere to validate]
    """

    for user in user_list:
        if user['name'] == username and user['password'] == password:
            user['logged_in'] = True
            return True
    print('Login error, user not found, please enter collect credentials')
    return False


def validate_user_name(username):
    """validation for the user name entered
    
    Arguments:
        username {[string]} -- [username ofr the user trying to login]
    
    Returns:
        [string] -- [if username passes the validation ]
    """
    username = username.strip()
    if len(username) < 3:
        print('Username should be 3 characters and above')
        username_prompt()
    return username


def username_prompt():
    """Prompt to prompt user to enter the user name 
    
    Returns:
        [string] -- [From the validation method]
    """

    username = input("Enter your Username:")
    return validate_user_name(username)


def password_prompt(username):
    """Prompts the user for the password
    
    Arguments:
        username {[string]} -- [Username ]
    
    Returns:
        [string ] -- [of the password from the validation method]
    """

    password = input("Enter password for {}:".format(username))
    return validate_password(password, username)


def validate_password(password, username):
    """Password validation 
    
    Arguments:
        password {string} -- [password of the user]
        username {[type]} -- [name , of the user to enter password for]
    
    Returns:
        [type] -- [description]
    """

    password = password.strip()
    if len(password) < 1:
        print('Password should be 1 character and above')
        password_prompt(username)
    return password



