//METHOD: POST
//Ce store permet de créer un compte utilisateur en fonction des données passées en paramètre
//Vérification des mots de passes
export async function createAccount(registerData){

    let url = "http://localhost:8000/peoples/create";

    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "firstname": registerData.first_name,
            "lastname": registerData.last_name,
            "email": registerData.email,
            "password": registerData.password,
            "date_of_birth": registerData.birthdate,
            "phone_number": registerData.tel,
            "domain": registerData.domain,
        }),
    });

    return await response.json();

}