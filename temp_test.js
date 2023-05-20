const Axios = require('axios')


let u = "https://dba.stackexchange.com/users?page=3&tab=reputation&filter=month"

Axios.get(u).then(d=>{
    console.log('dta = ',d.data)
})
