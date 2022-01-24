package main


import (
    "net/http"

    "github.com/gin-gonic/gin"
	"database/sql"
    "fmt"

  _ "github.com/lib/pq"
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
  user     = "api"
  password = "api"
  dbname   = "dungeonsanddungeonsapi"
)


// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
    c.IndentedJSON(http.StatusOK, albums)
}

func main() {
    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
    "password=%s dbname=%s sslmode=disable",
    host, port, user, password, dbname)
	
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

    router.Run("localhost:8080")
}