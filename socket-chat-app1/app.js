var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io').listen(server),
	nicknames = [];
	
//var apiai = require('apiai');
//var app = apiai("e5e89ef426ac40c5b13d2f08d7aafbc3");
	
server.listen(3000);


app.get('/', function(req,res){	
	console.log("hi....");	
	res.sendFile(__dirname+ '/index.html');
});

// create the connection
io.sockets.on('connection', function(socket){
	
	// new user creation
	socket.on('new user', function(data,callback){		
		console.log("new user create");	
		if(nicknames.indexOf(data)!=-1){
			callback(false);
		}else{
			callback(true);
			socket.nickname = data;
			nicknames.push(socket.nickname);
			io.sockets.emit('usernames',nicknames);
		}
	});
	
	function updateNicknames(){
		io.sockets.emit('usernames',nicknames);
	}
	
	//sending an message
	socket.on('send message', function(data){
		io.sockets.emit('new message',{msg : data, nick : socket.nickname});
		//socket.broadcast.emit('new message',data);
	});
	
	//disconnect
	socket.on('disconnect', function(data){
		if(!socket.nickname) return;
		nicknames.splice(nicknames.indexOf(socket.nickname),1);
		
	});
});

console.log("server started at : 3000");