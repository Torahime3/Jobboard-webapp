//METHOD : DELETE
//Ce store permet de supprimer un login de la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function deleteLogin(token, id){

    let url = "http://localhost:8000/login/"+token+"/delete";

    const response = await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "id": id,
        })
    });

    return await response.json();

}