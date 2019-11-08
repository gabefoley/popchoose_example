from flask import render_template, flash, redirect, url_for, request
from app import app, spotify, database

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    # Get two artists
    artists = database.get_artists()


    # Work out the most popular
    correct = 'a1' if artists['a1'].popularity > artists['a2'].popularity else 'a2'

    print ('correct is ')
    print (correct)

    # Get previous scores from this matchup
    sorted_ids = sorted([artists['a1'].id, artists['a2'].id])
    joint_id = "_".join(sorted_ids)

    matchup_text = database.get_matchup(joint_id)

    return render_template('index.html', title='Home', artists=artists, correct=correct, matchup_text=matchup_text)

@app.route('/update_scores', methods=['POST'])
def update_scores():
    if request.method == 'POST':
        info = request.get_json()
        sorted_ids = sorted([info['a1'], info['a2']])
        print ('here da ids')

        print (sorted_ids)
        database.update_matchup("_".join(sorted_ids), info['correct'])

    return redirect(url_for('index'))




