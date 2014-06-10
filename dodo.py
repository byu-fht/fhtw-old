def task_install():
    """install """
    return {
        'actions': ['python app.py build','cp htaccess build/.htaccess','rsync -rav --delete build/* zappala@fhtw.byu.edu:/var/www/fhtw.byu.edu'],
        }
