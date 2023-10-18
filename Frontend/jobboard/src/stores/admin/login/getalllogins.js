//METHOD : GET
//Ce store permet de récupérer tous les logins présents dans la base de données sauf les tokens
//les données sont retournés que si un token administrateur est passé en paramètre
export async function getAllLogins(token){

    let url = "http://localhost:8000/login/"+token+"/all";

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });

    return await response.json();
}