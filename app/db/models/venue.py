from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Venue(Base):
    __tablename__ = "venues"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    configurations: Mapped[list["VenueConfiguration"]] = relationship(
        back_populates="venue",
        cascade="all, delete-orphan",
    )

class VenueConfiguration(Base):
    __tablename__ = "venue_configurations"

    id: Mapped[int] = mapped_column(primary_key=True)
    venue_id: Mapped[int] = mapped_column(
        ForeignKey("rowdy.venues.id"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    venue: Mapped["Venue"] = relationship(
        back_populates="configurations",
    )
