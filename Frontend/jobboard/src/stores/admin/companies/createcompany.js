//METHOD: POST
//Ce store permet de créer des compagnies
//Un résultat est retourné si le token appartient à un administrateur
export async function createCompany(token, company){

    let url = "http://localhost:8000/companies/"+token+"/create"

    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "name": company.name,
            "description": company.description,
            "address": company.address,
            "city": company.city,
            "zipcode": company.zipcode,
            "url_website": company.url_website,
        })
    });

    return await response.json();

}