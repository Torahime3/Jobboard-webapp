let promise = getJobs();
async function getJobs(){
    const response = await fetch('http://127.0.0.1:8000/jobadvertisements/')
    return await response.json();
}

function refresh(){
    promise = getJobs();
}