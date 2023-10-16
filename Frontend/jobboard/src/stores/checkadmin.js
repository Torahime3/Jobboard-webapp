//METHOD : POST
//Ce store permet de vérifier qu'un token est bien associé a un compte ayant le role Admin
//ce qui lui permettra d'accéder à la page d'administration
export async function checkAdmin(token){

    let url = 'http://localhost:8000/login/checkAdmin';

    // fetch post
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "token": token,
        })
    });

    return await response.json();


}