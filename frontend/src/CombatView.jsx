import { useState, useEffect } from "react";
import { startCombat, takeTurn } from "./api";

export default function CombatView({ hero }) {
    const [session, setSession] = useState(null);
    const [log, setLog] = useState([]);
    const [outcome, setOutcome] = useState(null);

    useEffect(() => {
        startCombat(hero.id).then(setSession);
    }, []);

    async function handleAction(action) {
        try {
            const result = await takeTurn(session.id, action);
            setLog(prev => [...prev,
                `You dealt ${result.hero_damage} damage. Enemy dealt ${result.enemy_damage} damage.`
            ]);
            setSession(prev => ({...prev, enemy_hp: result.enemy_hp, hero_hp: result.hero_hp}));
            if (result.outcome) setOutcome(result.outcome);
        } catch (err) {
            console.error(err.message);
        }
    }

    if (!session) return <p>Loading battle...</p>;

    return (
        <div>
            <h2>Combat: {hero.name} vs {session.enemy_type}</h2>
            <p>{hero.name} HP: {session.hero_hp ?? hero.hp}</p>
            <p>Enemy HP: {session.enemy_hp}</p>
            {outcome ? (
                <h3>{outcome}</h3>
            ) : (
                <div>
                    <button onClick={() => handleAction("attack")}>Attack</button>
                    <button onClick={() => handleAction("potion")}>Use Potion</button>
                </div>
            )}
            <div>
                {log.map((entry, i) => <p key={i}>{entry}</p>)}
            </div>
        </div>
    )
}