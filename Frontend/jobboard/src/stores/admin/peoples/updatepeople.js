//METHOD: PUT
//Ce store permet de mettre à jour un people dans la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function updatePeople(token, people){

    let url = "http://localhost:8000/peoples/"+token+"/update";

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body : JSON.stringify({
            "id": people.id,
            "firstname": people.firstname,
            "lastname": people.lastname,
            "date_of_birth": people.date_of_birth,
            "phone_number": people.phone_number,
            "email": people.email,
            "domain": people.domain,
            "role": people.role,
            "id_company": people.id_company,
        })
    });

    return await response.json();
}