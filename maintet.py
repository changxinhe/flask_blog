from flask import request, render_template, Flask

from application import create_app

#app = Flask(__name__)
app =create_app()



if __name__ == '__main__':
    app.run(
        port = 80
    )



