const robot = require('robotjs')
var fs = require("fs");
var Jimp = require('jimp');
var ncp = require("copy-paste");
const { Navigator } = require("node-navigator");
const navigator = new Navigator();

const chromedriver = require('./steps/chromedriver')

const opencv = require('./steps/manipulate')

function intervl(){
    robot.keyTap('I',['control','shift'])
    var mouse = robot.getMousePos();

    setTimeout(_=>{
        robot.moveMouse(mouse.x + 300, mouse.y);
        setTimeout(_=>{
            robot.mouseClick("right");
        },500)
    },500)
    // console.log('mouse = ',mouse)

}


function captureImage({ x, y, w, h }) {
    const pic = robot.screen.capture(x, y, w, h)
    const width = pic.byteWidth / pic.bytesPerPixel // pic.width is sometimes wrong!
    const height = pic.height
    const image = new Jimp(width, height)
    let red, green, blue
    pic.image.forEach((byte, i) => {
      switch (i % 4) {
        case 0: return blue = byte
        case 1: return green = byte
        case 2: return red = byte
        case 3: 
          image.bitmap.data[i - 3] = red
          image.bitmap.data[i - 2] = green
          image.bitmap.data[i - 1] = blue
          image.bitmap.data[i] = 255
      }
    })
    return image
  }

// setTimeout(_=>{
//     // intervl()
//     let sz = robot.getScreenSize()
//     let img = robot.screen.capture();
//     // robot.captureScreen()
//     console.log('img = ',img)
//     setTimeout(_=>{
//         // fs.writeFileSync('img.png',robot);
//         // captureImage({x : 0, y : 0 , w : sz.width , h : sz.height}).write('capture.png')


        
//     },500)

//     console.log('timeout call')
// },3000)

    
// setTimeout(_=>{
//     let sz = robot.getScreenSize()
    
//     // 1280 - 580
//     // robot.moveMouse(700,mouse.y)
//     // robot.moveMouse(5,200)
//     // window.innerWidth
//     setTimeout(_=>{
//         var mouse = robot.getMousePos();
//         // robot.moveMouse(( 1280 - ( 1280 - (705 - 5 )  )  ),mouse.y)
//     },1000)
//     console.log('sc = ',sz)
// },3000)


const copyFunction = `
  function copyToClipboard(text) {
    if (window.clipboardData && window.clipboardData.setData){return window.clipboardData.setData("Text", text)}
    else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
        var textarea = document.createElement("textarea");
        textarea.textContent = text;
        textarea.style.position = "fixed";
        document.body.appendChild(textarea);
        textarea.select();
        try {return document.execCommand("copy")}catch(ex){return false}finally{document.body.removeChild(textarea)}
    }
  } `
  // $("html").innerHTML
//   ncp.copy(copyFunction, function () {
//     // complete...
//   })

// console.log('p = ',ncp)

// ncp.paste((e,d)=>{
//   console.log('paste = ',d)
// })

// navigator.clipboard.readText().then(p=>{

  
// })



  
setTimeout(_=>{
//    robot.moveMouse(5,100)
//    robot.keyTap('J',['control','shift'])
//    setTimeout(_=>{
//     robot.keyTap('V',['control'])
//     robot.setKeyboardDelay(30); 
//     robot.keyTap('enter')
//     robot.setKeyboardDelay(20); 
//     robot.typeString('copyToClipboard(window.innerWidth)')
//     robot.setKeyboardDelay(20);
//     robot.keyTap('enter')
// },1000)




//    setTimeout(_=>{
//     let sz = robot.getScreenSize()
//     var mouse = robot.getMousePos();

//     robot.moveMouse(( 1280 - ( 1280 - (705 - 5 )  )  ),mouse.y)

    // robot.typeString(copyFunction)

//     robot.keyTap('enter')
//     setTimeout(_=>{
//         robot.mouseClick('right','double')
//         // robot.mouseClick('right')
//     },1000)
//    },2000)



// 642

  //  robot.moveMouse(5,100)

  //  setTimeout(_=>{
  //         let sz = robot.getScreenSize()
  //         var mouse = robot.getMousePos();
 
  //     robot.moveMouse((sz.width - 642) - 2,mouse.y+ 100)
  //   //   robot.setMouseDelay(20)

  //       setTimeout(_=>{
  //           robot.keyTap('C',['control','shift'])
  //           // robot.setMouseDelay(20)
  //           setTimeout(_=>{
  //               robot.keyTap('f2')
  //               robot.setMouseDelay(20)
  //               robot.keyTap('A',['control'])
  //               robot.setMouseDelay(20)
  //               robot.keyTap('C',['control'])
                 
  //               // robot.mouseClick()
  //           },2000)
            

  //       })
  //  },3000)

},3000)
