from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)  # Changed to db.Text

    # Relationship to connect playlists to songs via the PlaylistSong table
    songs = db.relationship('Song', secondary='playlist_song', backref='playlists')

    def __repr__(self):
        return f'<Playlist {self.name}>'

class Song(db.Model):
    """Song."""

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

    # Relationships back to Playlist and Song
    playlist = db.relationship('Playlist', backref='playlist_song_associations')
    song = db.relationship('Song', backref='playlist_song_associations')

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
