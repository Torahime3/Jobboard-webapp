//METHOD: POST
//Ce store permet de mettre à jour une company dans la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function updateCompany(token, company){

    let url = "http://localhost:8000/companies/"+token+"/update";

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body : JSON.stringify({
            "id": company.id,
            "name": company.name,
            "description": company.description,
            "address": company.address,
            "city": company.city,
            "country": company.country,
            "url_website": company.url_website,
        })
    });

    return await response.json();
}