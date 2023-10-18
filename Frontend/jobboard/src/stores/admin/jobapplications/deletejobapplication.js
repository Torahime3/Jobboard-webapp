//METHOD: DELETE
//Ce store permet de supprimer une candidature
//Une réponse est retournée que si un token admin est passé en paramètre
export async function deleteJobApplication(token, id){

    let url = "http://localhost:8000/jobapplications/"+token+"/delete";
    
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