from galeria import database, app
from galeria.models import Usuario, Foto

with app.app_context():
    database.create_all()