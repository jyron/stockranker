# Stockranker
## What It Is 
Website to view, like, and comment on stocks and coins.

## Todo

### Backend
#### API Endpoints
Stock:
- Post new stock (all info). [POST] /stocks/create/
- Get stocks (all info). [GET] /stocks/
- Get individual stock. [GET] /stocks/{id}/
- Get stock comments. [GET] /stocks/{id}/comments/
- Get stock likes. [GET] /stocks/{id}/likes/

User:
- Create User [POST] /user/create/
- User Logs In. [POST] /user/login/
- User views own profile. [GET] /user/me/
- View random user's profile [GET] /user/{id}/
- User updates own profile. [PUT] /user/{id}/update/
- User likes Stock. [POST] url tbd
- User Comments on Stock. [POST] url tbd
- User replies to Comments. [POST] url tbd

#### Background Tasks

- Update Stock info daily (in the future aim for realtime updates). This only includes price and percentage change.
- Add new stocks as they enter the S&P 500 (I think this list changes often).

### Frontend (i hate it)
Login Functionality:
- User Login (Include google login, otherwise whats the point. I think it's called "Oath2"?) Researh that.
- User Logout (easy, literally delete local storage token)
- User View Own Profile (maybe easy)
- User Update Own Profile (maybe easy)

Data Viewing (very important, very easy to do poorly):  
- List stocks in a table, include name, price.  (Maybe react-table, maybe D3 library, whichever has better documentation)
- Allow search by name.
- Allow sort by price.
- Allow sort by percent change (movement)
- Show yearly/monthly/daily stock data. (This requires lot of db space I think? Or a lot of api calls?) It's not my desire/job to save historical data but i want it.

### Missing pieces
-  Idk this section will grow exponentially.
-  Login flow is tough. Looking at linkedin or google for an example, minus all the required info. Maybe there's a third-party solution.

### Notes
- Listening to [Alfa Mist Antiphon](https://www.youtube.com/watch?v=BVO_R8uvMhE) while i make this project.
- Tracking work in [Jira](https://stockranker.atlassian.net/jira/software/projects/STOC/boards/1) (practice for work).
