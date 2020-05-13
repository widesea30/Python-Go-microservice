package main

import "C"
import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

var g_dict_data map[string]interface{}

//export init_dict
func init_dict(path *C.char) {
	// Open our jsonFile
	jsonFile, err := os.Open(C.GoString(path))
	// if we os.Open returns an error then handle it
	if err != nil {
		fmt.Println(err)
	}
	// defer the closing of our jsonFile so that we can parse it later on
	defer jsonFile.Close()

	// g_dict_data = make(map[string]interface{}, 1024*1024*1024*8)
	byteValue, _ := ioutil.ReadAll(jsonFile)

	json.Unmarshal([]byte(byteValue), &g_dict_data)

	// fmt.Println(g_dict_data)
}

//export get_word
func get_word(word *C.char) *C.char {
	j, _ := json.Marshal(g_dict_data[C.GoString(word)])

	return C.CString(string(j))
}

func main() {}
