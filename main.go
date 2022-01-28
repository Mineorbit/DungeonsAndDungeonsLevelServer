package main


import (

    "github.com/dgrijalva/jwt-go"
    "net/http"
	"database/sql"
    "fmt"

  _ "github.com/lib/pq"
    "io/ioutil"
  "os"
  "time"
    "strconv"
	"log"
	"proto"
)



const (
  host     = "localhost"
  port     = 5432
  dbuser     = "api"
  password = "api"
  dbname   = "dungeonsanddungeonsapi"
)


type User struct {
ID uint64            `json:"id"`
 Username string `json:"username"`
 Password string `json:"password"`
}
//A sample use
var user = User{
 ID:          1,
 Username: "Max",
 Password: "Test123",
}



var db *sql.DB

func Login(w http.ResponseWriter, r *http.Request) {
  r.ParseForm()
  var u User
  u.Username = r.Form.Get("username")
  u.Password = r.Form.Get("password")
  //compare the user from the request, with the one we defined:
  if user.Username != u.Username || user.Password != u.Password {
  fmt.Fprintf(w, "Login Wrong")
     return
  }
  token, err := CreateToken(user.ID)
  if err != nil {
     fmt.Fprintf(w, err.Error())
     return
  }
  fmt.Fprintf(w, token)
}


func CreateToken(userId uint64) (string, error) {
  var err error
  //Creating Access Token
  os.Setenv("ACCESS_SECRET", "jdnfksdmfksd") //this should be in an env file
  atClaims := jwt.MapClaims{}
  atClaims["authorized"] = true
  atClaims["user_id"] = userId
  atClaims["exp"] = time.Now().Add(time.Minute * 15).Unix()
  at := jwt.NewWithClaims(jwt.SigningMethodHS256, atClaims)
  token, err := at.SignedString([]byte(os.Getenv("ACCESS_SECRET")))
  if err != nil {
     return "", err
  }
  return token, nil
}


func handleLevel(w http.ResponseWriter, r *http.Request){

	proto_resp, err := strconv.ParseBool(r.URL.Query()["proto_resp"][0])
	if err != nil {
        fmt.Println(err)
    }
	switch r.Method {
	case "GET":
		getLevelList(w,r,proto_resp)
	case "POST":
		uploadFile(w,r,proto_resp)
	}
}


func getLevelList(w http.ResponseWriter, r *http.Request, proto_resp bool){
	fmt.Printf("Request /level/ \n")

	var (
	id int64
	name string
	)
	
	levelList := []*LevelMetaData{}
	
	if db == nil {
	
	fmt.Printf("DB IS NIL \n")
	
	}
	
	rows, err := db.Query("select id, name from levels")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()
	for rows.Next() {
		err := rows.Scan(&id, &name)
		
		if err != nil {
		log.Fatal(err)
		}
		
		level := LevelMetaData{
		UniqueLevelId: id,
		FullName: name,
		}
		
		levelList = append(levelList, &level)
	}
	err = rows.Err()
	
	if err != nil {
		log.Fatal(err)
	}

	levelListResult:= LevelMetaDataList{
	Levels: levelList,
	}
	var data []byte
	err = proto.Unmarshal(data, levelListResult)
    fmt.Fprintf(w,"Test")
}

func uploadFile(w http.ResponseWriter, r *http.Request, proto_resp bool) {

	description := r.URL.Query()["description"]
	
    // Parse our multipart form, 10 << 20 specifies a maximum
    // upload of 10 MB files.
    r.ParseMultipartForm(10 << 20)
    // FormFile returns the first file for the given key `myFile`
    // it also returns the FileHeader so we can get the Filename,
    // the Header and the size of the file
    file, handler, err := r.FormFile("levelFiles")
    if err != nil {
        fmt.Println("Error Retrieving the File")
        fmt.Println(err)
        return
    }
    defer file.Close()
    fmt.Printf("Uploaded File: %+v\n", handler.Filename)
    fmt.Printf("File Size: %+v\n", handler.Size)
    fmt.Printf("MIME Header: %+v\n", handler.Header)

    

    // read all of the contents of our uploaded file into a
    // byte array
    fileBytes, err := ioutil.ReadAll(file)
    if err != nil {
        fmt.Println(err)
    }
	
	err = ioutil.WriteFile("test",[]byte(fileBytes), 0644)
	
    // return that we have successfully uploaded our file!
    fmt.Fprintf(w, "Successfully Uploaded File\n")
	fmt.Println(description)
	fmt.Println(proto_resp)
}

func setupRoutes() {
    http.HandleFunc("/level/", handleLevel)
	http.HandleFunc("/auth/token",Login)

    fmt.Println("=== API Online ===\n")
    http.ListenAndServe(":8080", nil)
}

func setupTables() {
	fmt.Printf("=== Setting up database tables ===\n")
	db.Query("CREATE TABLE IF NOT EXISTS levels (id SERIAL ,name varchar(32));")
	fmt.Printf("Created level table\n")
}

func main() {

    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
    "password=%s dbname=%s sslmode=disable",
    host, port, dbuser, password, dbname)
	
	var err error
	db, err = sql.Open("postgres", psqlInfo)
if err != nil {
  panic(err)
}
defer db.Close()
	
err = db.Ping()
if err != nil {
  panic(err)
}
    setupTables()
    setupRoutes()
}
