from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class HeroModel(Base):
    __tablename__ = "heroes"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Hero attributes
    name = Column(String, nullable=False)
    hero_class = Column(String, nullable=False)
    hp = Column(Integer)
    max_hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    crit_chance = Column(Float)
    potions = Column(Integer)
    gold = Column(Integer)
    experience = Column(Integer)
    level = Column(Integer)
    skill_cooldown = Column(Integer, default=0)

    # One hero can have many combat sessions
    combat_sessions = relationship("CombatSessionModel", back_populates="hero")

class CombatSessionModel(Base):
    __tablename__ = "combat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey("heroes.id"))
    enemy_type = Column(String)
    enemy_hp = Column(Integer)
    enemy_max_hp = Column(Integer)
    is_active = Column(Boolean)
    outcome = Column(String, nullable=False)

    hero = relationship("HeroModel", back_populates="combat_sessions")