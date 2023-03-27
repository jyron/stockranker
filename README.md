# Stockranker

Stockranker is a website that allows users to view, like, and comment on stocks and coins. The application has both frontend and backend components.

## Backend
The backend serves the following API endponts:

Stock Endpoints:

- Post new stock (all info). [POST] /stocks/create/
- Get stocks (all info). [GET] /stocks/
- Get individual stock. [GET] /stock/{id}/
- Get stock comments. [GET] /stock/{id}/comments/
- Get stock likes. [GET] /stock/{id}/likes/

User Endpoints:
- Create User [POST] /users/create/
- User Logs In. [POST] /users/login/
- User views own profile. [GET] /users/me/
- View random user's profile [GET] /users/{id}/
- User updates own profile. [PUT] /users/me/update/
- User likes Stock. [POST] /stock/{id}/like/
- User Comments on Stock. [POST] /stock/{id}/comments/
- User replies to Comments. [POST] /stock/comments/{id}/reply/

### Background Tasks

- Daily updates of stock info, specifically price and percentage change.
- Automatic addition of new stocks as they enter the S&P 500.

## Frontend
The Frontend includes the following features:

Login Functionality:
- User Login (Include Google login).
- User Logout.
- User View Own Profile.
- User Update Own Profile.

Data Viewing:  
- List stocks in a table.
- Allow search by name.
- Allow sort by price.
- Allow sort by percent change.
- Show yearly/monthly/daily stock data.

### Nice To Haves
--Dockerise Backend  
--Dockerise Frontend
### Notes
- Listening to [Alfa Mist Antiphon](https://www.youtube.com/watch?v=BVO_R8uvMhE) March 26, 2023.
- Listening to [Weeknd Die For You](https://www.youtube.com/watch?v=QLCpqdqeoII) March 27, 2023.
- Tracking work in [Jira](https://stockranker.atlassian.net/jira/software/projects/STOC/boards/1).
