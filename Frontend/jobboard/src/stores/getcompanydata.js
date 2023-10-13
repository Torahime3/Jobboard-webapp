//METHOD: GET
//Ce store permet de récupérer les données d'une entreprise en fonction de son id
export async function getCompanyData(id){

    let url = 'http://127.0.0.1:8000/companies/'+id;

    const response = await fetch(url);
    return await response.json();

}