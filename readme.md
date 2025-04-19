# Dependencies   
**Python dependencies**
* Python3/pip3  
* Packages listed in `requirements.txt`

**Node Dependencies**

-   Node.js/npm
-  ThreeJS
-   React
-   Packages listed in `package.json`
  
# Running from clone 
**Env variables/Key.json**
```
A Config file is provided on the trello board, if this is unavailable, 
the format of the file will be provided below.
Do note: this was extended from a firebase project provided. 
only the important variables are listed
```
**key.json**
```json
{  
  "type": "",  
  "project_id": "",  
  "private_key_id": "",  
  "private_key": "-",  
  "client_email": "",  
  "client_secret": "your_google_client_secret",  
  "client_id": "your_google_client_id",  
  "auth_uri": "",  
  "token_uri": "",  
  "auth_provider_x509_cert_url": "",  
  "client_x509_cert_url": "",  
  "genai_api_key": "your_gemini_key"  
}
```
**Dependency install/Flask Setup**
Running the backend
```bash
$ cd graveyard-backend 
$ pip install -r requirements.txt
$ flask init 
$ flask run
```  
Running the frontend
```bash
$ cd react-frontend 
$ npm i
$ npm start
```  
  
## Deployment differences VS Repository
  
```
The project, while deployed, runs a postgres implementation, for ease of access for 
future development the project is setup to use SQLite for QOL when testing.

Some of the api endpoints also append domain wide cookies due to the subdomain. This shouldn't
affect anything realistically, but mentioning it just to be sure.
```
  
# Flask Commands  
The only flask command that is important, is the flask test unit to run the unit tests.
```bash
$flask test unit
```

  
