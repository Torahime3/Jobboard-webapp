//METHOD : GET
//Cette méthode permet de récupérer toutes les candidatures d'un utilisateur
//en passant en paramètre son token
export async function getJobsAdvertisements(token){

    let url = 'http://127.0.0.1:8000/jobadvertisements/'

    const response = await fetch(url)
    return await response.json();
}