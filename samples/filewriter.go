package main

import (
	"http"
	"log"
	"io"
	"os"
)

func WriteToFileHandler(w http.ResponseWriter, r *http.Request) {
	f, _ := os.Create("file.txt")
	defer f.Close()
	io.WriteString(f, r.RawURL)
	io.WriteString(w, "Ok")
}

func main() {
	http.HandleFunc("/", WriteToFileHandler)
	if err := http.ListenAndServe(":9090", nil); err != nil {
		log.Fatal("Error listening", err.String())
	}
}
