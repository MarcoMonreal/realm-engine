import { useState } from 'react'
import HeroCreate from "./HeroCreate";
import HeroList from "./HeroList";
import CombatView from "./CombatView";

export default function App() {
  const [screen, setScreen] = useState("home");
  const [selectedHero, setSelectedHero] = useState(null);

  function handleHeroCreated(hero) {
    setSelectedHero(hero);
    setScreen("combat");
  }

  function handleSelectHero(hero) {
    setSelectedHero(hero);
    setScreen("combat");
  }

  return (
    <div>
      <h1>Veilborn</h1>
      {screen === "home" && (
        <div>
          <button onClick={() => setScreen("create")}>New Hero</button>
          <button onClick={() => setScreen("list")}>Load Hero</button>
        </div>
      )}

      {screen === "create" && (
        <HeroCreate onHeroCreated={handleHeroCreated} />
      )}

      {screen === "list" && (
        <HeroList onSelectHero={handleSelectHero} />
      )}

      {screen === "combat" && selectedHero && (
        <CombatView hero={selectedHero} />
      )}
    </div>
  )
}