from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class UrlModel(Base):
    __tablename__ = 'urls'

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(unique=True)
    short_url: Mapped[str] = mapped_column(unique=True)
