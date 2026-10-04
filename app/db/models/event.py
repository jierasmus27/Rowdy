from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    organisation_id: Mapped[int] = mapped_column(
        ForeignKey("rowdy.organisations.id"),
        nullable=False,
    )
    organisation: Mapped["Organisation"] = relationship(
        back_populates="events",
    )

    venue_id: Mapped[int] = mapped_column(
        ForeignKey("rowdy.venues.id"),
        nullable=False,
    )
    venue: Mapped["Venue"] = relationship(
        back_populates="events",
    )
