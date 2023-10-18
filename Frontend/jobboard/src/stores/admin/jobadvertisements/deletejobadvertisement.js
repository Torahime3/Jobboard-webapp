//METHOD: DELETE
//Ce store permet de supprimer une offre d'emploi
//Une réponse est retournée que si un token admin est passé en paramètre
export async function deleteJobAdvertisement(token, id){
    let url = "http://localhost:8000/jobadvertisements/"+token+"/delete";
    let response = await fetch(url, {
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