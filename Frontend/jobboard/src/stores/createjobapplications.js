//METHOD: POST
//Ce store permet de créer une candidature à une offre d'emploi
export async function createJobApplication(jobApplication) {

    console.log(
        "firstname:", jobApplication.first_name,
        "lastname:", jobApplication.last_name,
        "email:", jobApplication.email,
        "phone_number:", jobApplication.phone_number,
        "id_user:", jobApplication.id_user,
        "id_advertisement:", jobApplication.id_advertisement,
    )

    let url = "http://localhost:8000/jobapplications/create";

    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "firstname": jobApplication.first_name,
            "lastname": jobApplication.last_name,
            "email": jobApplication.email,
            "phone_number": jobApplication.phone_number,
            "id_user": jobApplication.id_user,
            "id_advertisement": jobApplication.id_advertisement,
        }),

    });

    return await response.json();

}