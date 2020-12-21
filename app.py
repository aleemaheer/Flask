from flask import Flask, redirect, render_template, request

# Creating a game in flask that's work well.

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# making our game

@app.route('/game')
def game1():

    return render_template('game.html')


@app.route('/right')
def path():
    path = request.args.get('name')
    
    if path.lower() == 'right':
        return render_template('right.html')
    elif path.lower() == 'left':
        return render_template('left.html')
    else:
        return "Invalid path."

@app.route('/swim')
def swim():
    swim = request.args.get('name2')

    if swim.lower() == 'swim':
        return render_template('swim.html')
    elif swim.lower() == 'go home':
        return render_template('gohome.html')
    else:
        return "Invalid path"

@app.route('/action')
def action():
    action = request.args.get('name3')

    if action == 'fight':
        return render_template('fight.html')
    elif action.lower() == 'surrender':
        return render_template('surrender.html')
    else:
        return "<h1>Invalid Input!</h1>"

@app.route('/weaponsword')
def weaponsword():
    weaponsword = request.args.get('weapon')

    if weaponsword.lower() == 'sword':
        return render_template('weaponsword.html')
    elif weaponsword.lower() == 'pistol':
        return render_template('weaponpistol.html')
    else:
        return "<h2>Invalid Input!</h2>"


if __name__ == '__main__':
    app.run(debug=True)