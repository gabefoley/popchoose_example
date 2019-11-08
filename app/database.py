from app import db
from app.models import Artist, MatchUp
from sqlalchemy.sql.expression import func


def get_artists():
    """
    Get two artists, their Spotify IDs, popularity, and a link to their image
    :return: List of two dictionaries containing the artist information
    """

    a1 = db.session.query(Artist).order_by(func.rand()).first()
    a2 = db.session.query(Artist).filter(Artist.popularity != a1.popularity).order_by(func.rand()).first()

    artists = {'a1': a1, 'a2': a2}
    return artists

def get_matchup(id):
    """
    Get the match up score between two Artists
    :param id: The joint ID for the Artists
    :return:
    """

    query = MatchUp.query.filter_by(id=id).first()

    if query:
        return f"This match up has been guessed correctly {query.correct} out of a total {query.correct + query.incorrect} times "

    else:
        return "This is the first time anyone has guessed between these two atists!"

def update_matchup(id, correct):
    """
    Update the match up score between two Artists, based on whether the user guessed it correctly or not
    :param id: The joint ID for the Artists
    :param correct: Boolean stating whether the user guessed correctly
    """
    query = MatchUp.query.filter_by(id=id).first()

    if query:
        if correct:
            query.correct += 1
        else:
            query.incorrect += 1

    else:
        if correct:
            query = MatchUp(id, 1, 0)
        else:
            query = MatchUp(id, 0, 1)

    db.session.add(query)
    db.session.commit()
