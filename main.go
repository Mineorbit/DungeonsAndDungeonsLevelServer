package main


import (

    "github.com/dgrijalva/jwt-go"
    "net/http"

    "github.com/gin-gonic/gin"
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


// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
    c.IndentedJSON(http.StatusOK, albums)
}

type User struct {
ID uint64            `json:"id"`
 Username string `json:"username"`
 Password string `json:"password"`
}
//A sample use
var user = User{
 ID:          1,
 Username: "username",
 Password: "password",
}

func Login(c *gin.Context) {
  var u User
  if err := c.ShouldBindJSON(&u); err != nil {
     c.JSON(http.StatusUnprocessableEntity, "Invalid json provided")
     return
  }
  //compare the user from the request, with the one we defined:
  if user.Username != u.Username || user.Password != u.Password {
     c.JSON(http.StatusUnauthorized, "Please provide valid login details")
     return
  }
  token, err := CreateToken(user.ID)
  if err != nil {
     c.JSON(http.StatusUnprocessableEntity, err.Error())
     return
  }
  c.JSON(http.StatusOK, token)
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


    router := gin.Default()
    router.GET("/albums", getAlbums)
	router.POST("/login/auth",Login);

    router.Run("0.0.0.0:8080")
}