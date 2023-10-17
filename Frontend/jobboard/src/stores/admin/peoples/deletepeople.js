//METHOD : DELETE
//Ce store permet de supprimer un people de la base de données
//les données sont retournés que si un token administrateur est passé en paramètre
export async function deletePeople(token, id){

    let url = "http://localhost:8000/peoples/"+token+"/delete";

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