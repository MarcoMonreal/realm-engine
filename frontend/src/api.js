const BASE_URL = "http://localhost:8000";

export async function createHero(name, heroClass) {
    const response = await fetch(`${BASE_URL}/heroes/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, hero_class: heroClass})
    });

    if (!response.ok) throw new Error("Failed to create hero.");
    return response.json();
}

export async function listHeroes() {
    const response = await fetch(`${BASE_URL}/heroes/`);
    if (!response.ok) throw new Error("Failed to fetch heroes list.");
    return response.json();
}

export async function getHero(heroID) {
    const response = await fetch(`${BASE_URL}/heroes/${heroID}`);
    if (!response.ok) throw new Error("Unable to locate hero.");
    return response.json();
}

export async function deleteHero(heroID) {
    const response = await fetch(`${BASE_URL}/heroes/${heroID}`, {
        method: "DELETE"
    });

    if (!response.ok) throw new Error("Unable to delete hero.");
    return response.json();
}

export async function startCombat(heroID, enemyType = "Goblin") {
    const response = await fetch(`${BASE_URL}/combat/start/${heroID}?enemy_type=${enemyType}`, {
        method: "POST"
    });

    if (!response.ok) throw new Error("Failed to start combat.");
    return response.json();
}

export async function takeTurn(sessionID, action) {
    const response = await fetch(`${BASE_URL}/combat/${sessionID}/turn?action=${action}`, {
        method: "POST",
    });

    if (!response.ok) throw new Error("Failed to take turn.");
    return response.json();
}

export async function getSession(sessionID) {
    const response = await fetch(`${BASE_URL}/combat/${sessionID}`);
    if (!response.ok) throw new Error("Failed to fetch session ID.");
    return response.json();
}