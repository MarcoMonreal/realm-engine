import { useState, useEffect } from "react";
import { listHeroes, deleteHero } from "./api";

export default function HeroList({ onSelectHero }) {
    const [heroes, setHeroes] = useState([]);

    useEffect(() => {
        listHeroes().then(setHeroes);
    }, []);

    async function handleDelete(heroID) {
        try {
            await deleteHero(heroID);
            const updated = await listHeroes();
            setHeroes(updated)
        } catch (err) {
            console.error(err.message);
        }
    }

    return (
        <div>
            <h2>Your Heroes</h2>
            {heroes.map(hero => (
                <div key={hero.id}>
                    <span>{hero.name} the {hero.hero_class} - Level {hero.level}</span>
                    <button onClick={() => onSelectHero(hero)}>Play</button>
                    <button onClick={() => handleDelete(hero.id)}>Delete</button>
                </div>
            ))}
        </div>
    )
}