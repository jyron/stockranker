# Stockranker
App to like and comment on stocks

## Todo (in order)

### Backend
#### API Endpoints
Stock:
- Post new stock (all info).
- Get stocks (all info).
- Get individual stock.
- Get stock comments.
- Get stock likes.

User:
- Create User (email, password, optional nickname [don't want to identify people by email? idc idk].
- User Logs In
- User views own profile.
- User updates own profile (nickname, password).
- User Likes Stock.
- User Comments on Stock.
- User replies to Comments.

Damn this is a lot of endpoints

#### Background Tasks

- Update Stock info daily (in the future aim for realtime updates). This only includes price and percentage change.
- Add new stocks as they enter the S&P 500 (I think this list changes often).

### FrontEnd (i hate it and the feeling is mutual :/)
#### Login Functionality
- User Login (Include google login, otherwise whats the point. I think it's called "Oath2"?) Researh that.
- User Logout (easy, literally delete local storage token)
- User View Own Profile (maybe easy)
- User Update Own Profile (maybe easy)

#### Data Viewing (very important, very easy to do poorly)
- List stocks in a table, include name, price.  (Maybe react-table, maybe D3 library, whichever has better documentation)
- Allow search by name.
- Allow sort by price.
- Allow sort by percent change (movement)
- Show yearly/monthly/daily stock data. (This requires lot of db space I think? Or a lot of api calls?) It's not my desire/job to save historical data but i want it!

### Missing pieces
-  Idk this section will grow exponentially.
-  Login is going to be tough. Lookingat linkedin or google for an example, minus all the required info.

### Notes
- Listening to Alfa Mist Antiphon https://www.youtube.com/watch?v=BVO_R8uvMhE while i make this project
- Tracking my work in [Jira](https://stockranker.atlassian.net/jira/software/projects/STOC/boards/1) (practice for work)
