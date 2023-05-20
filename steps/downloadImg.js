const fs = require('fs') , axios = require('axios');

function DownloadImage(url, path,cb){
  cb='function'===typeof cb ? cb : null
    return new Promise((resolve, reject) => {
     axios({url,responseType: 'stream'}).then(r=>r.data.pipe(fs.createWriteStream(path))
        .on('finish',()=>{
                cb(false,true)
                resolve()
            })
        .on('error',e=>{
                cb(e,false)
                reject(e)
            })
      )
   });
}

// DownloadImage(
//     'https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s150x150/201183122_1196226470814700_77492436918662027_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=2gA2d6kj8ZgAX_oSmqv&edm=ABfd0MgBAAAA&ccb=7-4&oh=cdc4702ffe91eeed6d8962c7ae45dcba&oe=6113C884&_nc_sid=7bff83',
//     './steps/ram.png',
//     (e,r)=>{
//         console.log('err = ',e)
//         console.log('res = ',r)
//     }
// )

module.exports = { DownloadImage }
