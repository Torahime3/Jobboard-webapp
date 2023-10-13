//METHOD: GET
//Ce store permet de récupérer les données d'un utilisateur en fonction de son token
export async function getUserData(token){

    let url = 'http://127.0.0.1:8000/peoples/'+token;

    const response = await fetch(url);
    return await response.json();

}