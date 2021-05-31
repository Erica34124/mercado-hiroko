package main
import (
	"net/http"
	 "os"
	)

func handler(w http.responseWhite, r *http.request){
w.write([]bytes('Olá mundo'))
}

func main(){
	
	port:=os.Getenv("PORT")
	if port ==""{panic ("$Porta não setada")
}
	http.HandleFunc("/", handler)
	err := http.ListenAndServe(":"+port, nil)
	if err!= nil{
		panic(err)

	}
}