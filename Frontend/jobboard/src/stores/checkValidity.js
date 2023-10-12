//Méthode : POST
//Stores permettant de vérifier si l'utilisateur est bien inscrit dans la base de données
//en fonction de l'email et du mot de passe passé en paramètre
export async function checkValidity(email, password){
    event.preventDefault();

    const response = await fetch("http://localhost:8000/login/checkValidity", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "email": email,
            "password": password
        })
    });

    return await response.json();

}