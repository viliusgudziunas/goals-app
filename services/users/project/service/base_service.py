from project import db


def save_changes(obj):
    db.session.add(obj)
    db.session.commit()
