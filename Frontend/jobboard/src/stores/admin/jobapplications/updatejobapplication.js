//METHOD : PUT
//Ce store permet d'update une candidature
//Une réponse est retournée que si un token admin est passé en paramètre
export async function updateJobApplications(token, app){

    let url = "http://localhost:8000/jobapplications/"+token+"/update";

    let response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "id": app.id,
            "firstname": app.firstname,
            "lastname": app.lastname,
            "email": app.email,
            "phone_number": app.phone_number,
            "id_advertisement": app.id_advertisement,
            "id_people": app.id_people,
            "date_of_application": app.date_of_application,
        })
    });

    return await response.json();
}