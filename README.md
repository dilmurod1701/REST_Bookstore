## How to install
1. Clone this project
2. Install requirements.txt
3. To install requirements.txt run on the terminal pip install -r requirements.txt

## How to use this project
1. only GET request http://127.0.0.1:8000/api - Returns all available Books
2. only GET request http://127.0.0.1:8000/api/all - Returns all Books
3. only POST request http://127.0.0.1:8000/api/new - Endpoint for adding a new Book. (automatically added on behalf of the person who is logged in
4. only GET request http://127.0.0.1:8000/api/<id> - Show Book with <id> (detail view)
5. only DELETE request http://127.0.0.1:8000/api/<id>/delete - Deletes the Book with <id>
6. only PUT/PATCH request http://127.0.0.1:8000/api/<id>/update - Updates the information of the Book with <id>
7. only GET request http://127.0.0.1:8000/api/<username> - Returns all Books of user <username>
8. only GET request http://127.0.0.1:8000/api/sort/?sort=<field> - sorts Books by the given <filed>
9. only POST request http://127.0.0.1:8000/api/signup - View to sign up
10. only POST request http://127.0.0.1:8000/api/login - Endpoint for login
11. only POST request http://127.0.0.1:8000/api/password/reset/ - Endpoint to reset the password for those who have forgotten it
12. only GET request http://127.0.0.1:8000/api/subscribe - To subscribe to a blog post
13. only GET request http://127.0.0.1:8000/api/search/?search=<title> - search Books by the given title
14. only GET request http://127.0.0.1:8000/api/schema/swagger - Show schemes
