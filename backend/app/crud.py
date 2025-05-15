from sqlalchemy.orm import Session  # para hacer consultas a la base con SQLAlchemy
from app import models, schemas  # importamos los modelos de la base y los esquemas de validación
from passlib.context import CryptContext  # para encriptar y verificar contraseñas

# configuramos bcrypt como método de encriptación de claves
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# busca un usuario por su email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# crea un nuevo usuario y guarda la clave encriptada
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)  # encriptamos la clave
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)  # lo agregamos a la base
    db.commit()      # confirmamos los cambios
    db.refresh(db_user)  # actualizamos el objeto con los datos que se guardaron
    return db_user  # lo devolvemos

# busca un usuario por su ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# compara la clave escrita con la clave guardada (encriptada)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# crea una nueva nota vinculada a un usuario
def create_note(db: Session, note: schemas.NoteCreate, user_id: int):
    # se crea usando los datos de Note más el ID del user que la crea
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# trae todas las notas que pertenecen a un usuario específico
def get_notes_by_user(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.owner_id == user_id).all()
