//Méthode : GET
//Stores permettant de récupérer les informations de toutes les offres d'emploie
//ou que d'une seule en fonction de l'id passé en paramètre
export async function getJobsAdvertisements(jobId = null){

    let url = 'http://127.0.0.1:8000/jobadvertisements/'

    if(jobId !== null){
        url = url + jobId;
    }

    const response = await fetch(url)
    return await response.json();
}