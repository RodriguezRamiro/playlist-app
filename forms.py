"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from models import db, Song, PlaylistSong

BaseModelForm = model_form_factory(FlaskForm)
class ModelForm(BaseModelForm):
    """Base form for using SQLAlchemy models with FlaskForm."""
    @classmethod
    def get_session(cls):
        """Get the database session for use with wtforms_alchemy."""
        return db.session

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Playlist Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Playlist')


class SongForm(ModelForm):
    """Form for adding songs."""
    title = StringField('Song Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    submit = SubmitField('Add Song')

    class Meta:
        model = Song


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song_id = SelectField('Song To Add', coerce=int)
    submit = SubmitField('Add Song')

    class Meta:
        model = PlaylistSong
        include = ['song_id']