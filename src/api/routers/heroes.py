from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import HeroModel
from ..schemas import HeroResponse, HeroCreate, HeroUpdate
from src.game.hero import Warrior, Mystic, Assassin

router = APIRouter(prefix="/heroes", tags=["heroes"])

def hero_game_object(hero_record):
    # Converts database row into a game Hero object
    class_map = {"Warrior": Warrior, "Mystic": Mystic, "Assassin": Assassin}
    hero = class_map[hero_record.hero_class](hero_record.name)
    hero.hp = hero_record.hp
    hero.max_hp = hero_record.max_hp
    hero.attack = hero_record.attack
    hero.defense = hero_record.defense
    hero.crit_chance = hero_record.crit_chance
    hero.potions = hero_record.potions
    hero.gold = hero_record.gold
    hero.experience = hero_record.experience
    hero.level = hero_record.level
    hero.skill_cooldown = hero_record.skill_cooldown
    return hero

@router.post("/", response_model=HeroResponse)
def create_hero(hero_data: HeroCreate, db: Session = Depends(get_db)):
    class_map = {"Warrior": Warrior, "Mystic": Mystic, "Assassin": Assassin}

    if hero_data.hero_class not in class_map:
        raise HTTPException(status_code=400, detail="Invalid hero class")
    
    hero = class_map[hero_data.hero_class](hero_data.name)

    hero_model = HeroModel(
        name = hero.name,
        hero_class = hero.hero_class,
        hp = hero.hp,
        max_hp = hero.max_hp,
        attack = hero.attack,
        defense = hero.defense,
        crit_chance = hero.crit_chance,
        potions = hero.potions,
        gold = hero.gold,
        experience = hero.experience,
        level = hero.level,
        skill_cooldown = hero.skill_cooldown
    )

    db.add(hero_model)
    db.commit()
    db.refresh(hero_model)
    return hero_model

@router.get("/", response_model=list[HeroResponse])
def list_heroes(db: Session = Depends(get_db)):
    return db.query(HeroModel).all()

@router.get("/{hero_id}", response_model=HeroResponse)
def get_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.query(HeroModel).filter(HeroModel.id == hero_id).first()
    
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    return hero

@router.patch("/{hero_id}", response_model=HeroResponse)
def update_hero(hero_id: int, hero_data: HeroUpdate, db: Session=Depends(get_db)): # type: ignore
    hero = db.query(HeroModel).filter(HeroModel.id == hero_id).first()
    
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    if hero_data.hp is not None:
        hero.hp = hero_data.hp # type: ignore
    
    if hero_data.max_hp is not None:
        hero.max_hp = hero_data.max_hp # type: ignore
    
    if hero_data.attack is not None:
        hero.attack = hero_data.attack # type: ignore

    if hero_data.defense is not None:
        hero.defense = hero_data.defense # type: ignore
    
    if hero_data.crit_chance is not None:
        hero.crit_chance = hero_data.crit_chance # type: ignore
    
    if hero_data.potions is not None:
        hero.potions = hero_data.potions # type: ignore

    if hero_data.gold is not None:
        hero.gold = hero_data.gold # type: ignore   
    
    if hero_data.experience is not None:
        hero.experience = hero_data.experience # type: ignore

    if hero_data.level is not None:
        hero.level = hero_data.level # type: ignore

    db.commit()
    db.refresh(hero)
    return hero

@router.delete("/{hero_id}")
def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    hero = db.query(HeroModel).filter(HeroModel.id == hero_id).first()

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    db.delete(hero)
    db.commit()
    return {"detail": "Hero deleted successfully"}