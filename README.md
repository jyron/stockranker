# Stockranker
## Free Stock Ranking Api

### Purpose
This app lists every stock in the [S&P 500](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) and allows users to upvote/downvote each stock. The backend is a python API built upon Fastapi and Postgresql, and the frontend is (IDK ANY FRONTEND EXCEPT HTML and JAVASCRIPT).

### Backend

#### Database Models (Work in Progress)

1. Stock
    - id
    - name
    - symbol
    - industry
    - price
    - votes(fk StockVote.stock_id)
    - comments(fk Comment.stock_id)
2. User
    - id
    - email
    - comments(fk Comment.author)
    - stockvotes(fk StockVote.user_id)
    - commentvotes(fk CommentVote.user_id)
3. Comment
    - id
    - datetime
    - text
    - author(fk User.id)
    - stock_id(fk Stock.id)
    - votes(fk CommentVote.comment_id)
4. StockVote
    - id
    - user_id
    - stock_id
    - vote(-1/+1)
5. CommentVote
    - id
    - user_id
    - comment_id
    - vote(-1/+1)
    
^Work in Progress using [this](https://stackoverflow.com/questions/52665707/how-do-i-implement-a-like-button-function-to-posts-in-python-flask) and [this](https://stackoverflow.com/questions/55074867/posts-comments-replies-and-likes-database-schema) for reference.

#### User accesible API Functions

Selectors (for reading from database)

  **Stock Selectors**
      
      - get_all_stocks() -> return all stocks
      - get_stock_by_id(stock_id) -> return one stock
      - get_stocks_by_industry(industry) -> return list of stocks
      - get_stock_comments(stock_id) -> return list of comments based on stock
        
  **User Selectors**
  
      - get_all_users() -> return all users
      - get_user_by_id(id) -> return one user
      - get_user_comments(user_id) -> return list of comments based on user
      - get_user_votes(user_id) -> return list of stocks user has voted on
    
Services (for create,edit,delete in database)

  **Stock Services**
  
      - update_stock_price(price,id)
      - like_stock(stock_id,user_id)
      - dislike_stock(stock_id,user_id)
      

  **User Services**
  
      - create_user(email)
      - update_user(id,attributes)
      - delete_user(id)
      
  **Comment Services**
      - add_comment(stock_id,user_id)
      - delete_comment(comment_id)

#### Endpoints

**Stock Endpoints**

    - GET /stocks -> get_all_stocks
    - GET /stocks/:id -> get_stock_by_id
    - GET /stocks/:id/comments -> get_stock_comments
    - POST /stocks/:id/like -> like_stock
    - POST /stocks/:id/dislike -> dislike_stock
    - POST /stocks/:id/comment -> add_comment

**User Endpoints**

    - GET /users -> get_all_users
    - GET /users/:id -> get_user_by_id
    - GET /users/:id/comments -> get_user_comments
    - POST /users -> create_user
    - PUT /users -> edit_user
    - DELETE /users -> delete_user

### Git Methods
(todo)


    
    
