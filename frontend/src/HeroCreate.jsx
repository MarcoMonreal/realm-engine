import { useState } from "react";
import { createHero } from "./api";

export default function HeroCreate({ onHeroCreated }) {
    const [name, setName] = useState("");
    const [heroClass, setHeroClass] = useState("Warrior");
    const [error, setError] = useState(null);

    async function handleSubmit() {
        try {
            const hero = await createHero(name, heroClass);
            onHeroCreated(hero);
        } catch (err) {
            setError(err.message);
        }
    }

    return (
        <div>
            <h2>Create Your Hero</h2>
            {error && <p style={{color: "red"}}>{error}</p>}
            <input 
                placeholder = "Hero Name"
                value = {name}
                onChange = {e => setName(e.target.value)}
            />
            <select value={heroClass} onChange={e => setHeroClass(e.target.value)}>
                <option value="Warrior">Warrior</option>
                <option value="Mystic">Mystic</option>
                <option value="Assassin">Assassin</option>
            </select>
            <button onClick={handleSubmit}>Begin Adventure</button>
        </div>
    );
}