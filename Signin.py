def signin(run):
    print('Welcome to the code club. Sign in with your code (no spaces)')
    usernamepassword = input('Username and password (everything together):')
    if usernamepassword == 'MagicMikesClubRickrollers1234567890':
        print('················')
        print('User and password ok')
        import webbrowser
        webbrowser.open_new('https://github.com/IBM-Deep-Thought/THEpage')
    else:
        print('Not accessible')