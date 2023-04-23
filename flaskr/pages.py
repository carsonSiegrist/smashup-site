from flask import render_template, request
from flaskr import backend

backend = backend.Backend() #Create backend object

def make_endpoints(app):
    #TODO make endpoints 
    @app.route('/')
    def main():
        return render_template("main.html", title = "Home")
    
    @app.route('/allRandom', methods=['POST', 'GET'])
    def allRandom():
        if request.method == 'GET': #User opened page
            return render_template("allRandom.html", title="All Random", decks = None)
            
        elif request.method == 'POST': #User requested decks
            playerCount = int(request.form["playerCount"])
            decks = backend.allRandom(playerCount)
            return render_template("allRandom.html", title="All Random", decks = decks)

    @app.route('/randomDraft', methods=['POST', 'GET'])
    def randomDraft():
        pass

    @app.route('/singleDraft', methods=['POST', 'GET'])
    def singleDraft():
        pass


