
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL","postgresql://twin:twinpass@db:5432/twin_db")
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
def init_db():
    with engine.begin() as conn:
        conn.execute(text("""CREATE TABLE IF NOT EXISTS observations (
            id serial PRIMARY KEY,
            ts timestamptz DEFAULT now(),
            features jsonb,
            outcome double precision
        );"""))
