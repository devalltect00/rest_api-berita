from ..utils.db import db
from datetime import datetime

class New(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(100), nullable=False, unique=True)
    synopsis=db.Column(db.Text(), nullable=False)
    pictureLink=db.Column(db.String(), nullable=False)
    contentLink=db.Column(db.String(), nullable=False)
    date=db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    sourceNews=db.Column(db.String(20), nullable=False, default="internal")
    channelName=db.Column(db.String(20), nullable=True)
    videoLink=db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<News {self.id}>"
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()