package main


import (

    "github.com/dgrijalva/jwt-go"
    "net/http"
	"database/sql"
    "fmt"

  _ "github.com/lib/pq"
  "os"
  "time"
)

// album represents data about a record album.
type album struct {
    ID     string  `json:"id"`
    Title  string  `json:"title"`
    Artist string  `json:"artist"`
    Price  float64 `json:"price"`
}

// albums slice to seed record album data.
var albums = []album{
    {ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
    {ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
    {ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

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
 Username: "Ma",
 Password: "Test123",
}

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





func uploadFile(w http.ResponseWriter, r *http.Request) {
    fmt.Println("File Upload Endpoint Hit")

    // Parse our multipart form, 10 << 20 specifies a maximum
    // upload of 10 MB files.
    r.ParseMultipartForm(10 << 20)
    // FormFile returns the first file for the given key `myFile`
    // it also returns the FileHeader so we can get the Filename,
    // the Header and the size of the file
    file, handler, err := r.FormFile("myFile")
    if err != nil {
        fmt.Println("Error Retrieving the File")
        fmt.Println(err)
        return
    }
    defer file.Close()
    fmt.Printf("Uploaded File: %+v\n", handler.Filename)
    fmt.Printf("File Size: %+v\n", handler.Size)
    fmt.Printf("MIME Header: %+v\n", handler.Header)

    // Create a temporary file within our temp-images directory that follows
    // a particular naming pattern
    tempFile, err := ioutil.TempFile("temp-images", "upload-*.png")
    if err != nil {
        fmt.Println(err)
    }
    defer tempFile.Close()

    // read all of the contents of our uploaded file into a
    // byte array
    fileBytes, err := ioutil.ReadAll(file)
    if err != nil {
        fmt.Println(err)
    }
    // write this byte array to our temporary file
    tempFile.Write(fileBytes)
    // return that we have successfully uploaded our file!
    fmt.Fprintf(w, "Successfully Uploaded File\n")
}

func setupRoutes() {
    http.HandleFunc("/upload", uploadFile)
	http.HandleFunc("/auth/token",Login)
    http.ListenAndServe(":8080", nil)
}

func main() {

    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
    "password=%s dbname=%s sslmode=disable",
    host, port, dbuser, password, dbname)
	
	db, err := sql.Open("postgres", psqlInfo)
if err != nil {
  panic(err)
}
defer db.Close()
	
err = db.Ping()
if err != nil {
  panic(err)
}

    fmt.Println("Hello World")
    setupRoutes()
}
