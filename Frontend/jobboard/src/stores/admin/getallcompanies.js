//METHOD : GET
//Ce store permet de récupérer toutes les companies présentes dans la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function getCompanies(token){

    let url = "http://localhost:8000/companies/"+token;

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });

    return await response.json();
}