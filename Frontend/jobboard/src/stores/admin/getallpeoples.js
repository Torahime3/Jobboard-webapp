//METHOD : GET
//Ce store permet de récupérer tous les peoples présents dans la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function getPeoples(token){

    let url = "http://localhost:8000/peoples/"+token+"/all";

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });

    return await response.json();
}