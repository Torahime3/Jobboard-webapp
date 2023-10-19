//METHOD : GET
//Ce store permet de récupérer toutes les offres d'emplois
//Ne retourne un résultat que si un token admin est passé en paramètre
export async function getAllJobAdvertisements(token){

    let url = "http://localhost:8000/jobadvertisements/"+token+"/all";

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    return await response.json();
}

export async function getAllJobAdvertisementsByCompany(token){

    let url = "http://127.0.0.1:8000/jobadvertisements/"+token+"/company";

    const response = await fetch(url)
    return await response.json();

}