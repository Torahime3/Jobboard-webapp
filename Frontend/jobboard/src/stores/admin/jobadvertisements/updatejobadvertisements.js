//METHOD : PUT
//Ce store permet d'update une offre d'emploi
//Une réponse est retournée que si un token admin est passé en paramètre
export async function updateJobAdvertisement(token, job){

    let url = "http://localhost:8000/jobadvertisements/"+token+"/update";

    console.log({
        "id": job.id,
        "title": job.title,
        "job_domain": job.job_domain,
        "description": job.description,
        "contract_type": job.contract_type,
        "date_of_jobadvertisements": job.date_of_jobadvertisements,
        "location": job.location,
        "duration_week": job.duration_week,
        "id_company": job.id_company,
        "id_people": job.id_people,
})

    let response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "id": job.id,
            "title": job.title,
            "job_domain": job.job_domain,
            "description": job.description,
            "contract_type": job.contract_type,
            "date_of_jobadvertisements": job.date_of_jobadvertisements,
            "location": job.location,
            "duration_week": job.duration_week,
            "id_company": job.id_company,
            "id_people": job.id_people,
        })
    });

    return await response.text();
}