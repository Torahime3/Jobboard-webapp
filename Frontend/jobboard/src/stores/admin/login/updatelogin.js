//METHOD: PUT
//Ce store permet de mettre à jour un login dans la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function updateLogin(token, people){

    let url = "http://localhost:8000/login/"+token+"/update";

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body : JSON.stringify({
            "id": people.id,
            "username": people.username,
            "password": people.password,
            "email": people.email,
            "id_people": people.id_people,
        })
    });

    return await response.json();
}