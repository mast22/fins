from sqlalchemy import Column, String, Integer, Numeric, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class Currency(Base):
    id = Column(Integer, primary_key=True)
    code = Column(String(3))
    desc = Column(String, nullable=True)

    def __repr__(self):
        return f"<Currency code={self.code}>"
