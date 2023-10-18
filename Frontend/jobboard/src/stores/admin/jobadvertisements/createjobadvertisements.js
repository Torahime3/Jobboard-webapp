//METHOD : POST
//Ce store permet de créer une annonce d'emploi
//Une réponse est retournée que si un token admin est passé en paramètre
export async function createJobAdvertisement(token, job){

    let url = "http://localhost:8000/jobadvertisements/"+token+"/create";

    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            job: job
        })
    });

    return await response.json();
}