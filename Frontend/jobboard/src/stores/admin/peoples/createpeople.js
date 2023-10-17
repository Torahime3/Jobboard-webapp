//METHOD: POST
//Ce store permet de créer des peoples
//Un résultat est retourné si le token appartient à un administrateur
export async function createPeople(token, people){

    let url = "http://localhost:8000/peoples/"+token+"/create"

    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            "firstname": people.firstname,
            "lastname": people.lastname,
            "date_of_birth": people.date_of_birth,
            "phone_number": people.phone_number,
            "email": people.email,
            "domain": people.domain,
            "password": people.password,
        })
    });

    return await response.json();

}