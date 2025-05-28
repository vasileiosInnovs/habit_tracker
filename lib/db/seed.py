from lib.db.session import engine, session
from lib.models import Base

Base.metadata.create_all(engine)
