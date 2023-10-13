//Méthode : POST
//Stores permettant de vérifier si l'utilisateur est bien inscrit dans la base de données
//en fonction de l'email et du mot de passe passé en paramètre
export async function checkValidity(login){
    event.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/login/checkValidity", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "email": login.email,
            "password": login.password
        })
    });

    return await response.json();

}