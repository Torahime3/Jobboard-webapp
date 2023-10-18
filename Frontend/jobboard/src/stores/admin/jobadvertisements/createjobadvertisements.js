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
            "title": job.title,
            "job_domain": job.job_domain,
            "description": job.description, 
            "location": job.location,
            "contract_type": job.contract_type,
            "duration_week": job.duration_week,
            "id_company": job.id_company,
            "id_people": job.id_people,
        })
    });

    return await response.json();
}