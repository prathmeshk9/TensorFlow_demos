/*$(function($){			
	var socket = io.connect();
	
	//Nick Name 
	var $nickForm = $('#sendNick');
	var $nickError = $('#nickError')
	var $nickBox = $('#nickname');	
	var $users = $('#users')			
	
	// Message
	var $messageForm = $('#send-message');
	var $messageBox = $('#message');
	var $chat = $('#chat');
	
	
	// nick button submit
	$nickForm.submit(function(e){
		console.log("nick button called....");	
		e.preventDefault();
		socket.emit('new user',$nickBox.val(),function(data){
			if(data){
				$('#nickWrap').hide();
				$('#contentWrap').show();
			}else{
				$nickError.html("That UserName is Already Taken ! Try Again !");
			}
		});				
		
		$nickBox.val('');
	});
	
	// display the online user
	socket.on('usernames', function(data){
		console.log("online users....");		
		var html = '';
		for(i=0;i<data.length;i++){
			html += data[i] + '</br>';
		}
		$users.html(html);
	});
	
	// message submit button
	$messageForm.submit(function(e){
		e.preventDefault();
		socket.emit('send message', $messageBox.val());
		
		$messageBox.val('');
	});
	
	socket.on('new message', function(data){			
		$chat.append("<b> You : </b>"+ data.msg +"<br/>");

		//sendInfo();
					
		if(data.msg=="hi"){
			$chat.append("<b> Bot Says : </b> Hello "+ data.nick +"<br/>");
		}else if(data.msg=="hello"){
			$chat.append("<b> Bot Says : </b> I am Robot Fine.Nice To Meet you<br/>");
		}else{
			$chat.append("<b> Bot Says : </b> Hello "+ data.nick +"<br/>");
		}		
		
	});
});*/
function hello(){
	alert("hi....................");
}