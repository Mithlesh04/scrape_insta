const {GLOBAL} = require('../GLOBAL')
const robot = require('robotjs')
const ncp = require("copy-paste");

/**
 * @toggleConsole toggle console  
 * @status  open | close
 * @cb   callback
 */
function toggleConsole(status='open',cb){//open|close
    cb = typeof cb==='function' ? cb : null
    var f = _=>{
        robot.keyTap('J',['control','shift'])
        setTimeout(_=>{
            cb && cb()
        },2000)
    }

    if(status==='open'){
        if(GLOBAL.isConsoleOpen){
            cb && cb()
        }else f()
    }else if(status==='close'){
        if(GLOBAL.isConsoleOpen){
            f()
        }else{
          cb && cb()
        }
    };
     
}


/**
* @copyPaste copy function and paste inside the console
*
*/
function copyPaste(s,cb){
  cb = typeof cb==='function' ? cb : null
  ncp.copy(s,function(){
    cb && cb()
  })
 }


function Console(cb){ //cb = return html document 
    setTimeout(_=>{
        toggleConsole('open',_=>{
            const copyFunction = `function ${GLOBAL.copyFunctionName}(text){if (window.clipboardData && window.clipboardData.setData){return window.clipboardData.setData("Text", text)}else if (document.queryCommandSupported && document.queryCommandSupported("copy")){var textarea = document.createElement("textarea");textarea.textContent = text;textarea.style.position = "fixed";document.body.appendChild(textarea);textarea.select();try {return document.execCommand("copy")}catch(ex){return false}finally{document.body.removeChild(textarea)}}};${GLOBAL.copyFunctionName}($('html').innerHTML)`
            copyPaste(copyFunction,_=>{
                robot.keyTap("V",['control'])
                robot.setKeyboardDelay(20)
                robot.keyTap('enter')
                robot.setKeyboardDelay(700)
                setTimeout(_=>{
                  ncp.paste((e,d)=>{
                    if(!e){
                        cb = typeof cb==='function' ? cb(d) : null
                    }else{
                        throw new Error('unable to get clipbord data')
                    }
                  })
                },1200)
            })
        })
    },3000)
}

module.exports = { Console }
