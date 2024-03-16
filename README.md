# Maverick Analytics Microservice
### Installation:

- Clone the repository to your local machine.
- Install the required dependencies using `pip install -r requirements.txt`

### Running the application:
- Navigate to the project directory.
- Run the Flask application using python app.py.
- The application will start running on `http://localhost:5000`.

### API Endpoints:
 ### - Uploading CSV Files:
- Send a `POST` request to `/upload` endpoint with a CSV file attached.
Example using cURL:
```bash
curl -X POST -F "file=@/path/to/your/file.csv" http://localhost:5000/upload
```
- The response will be a JSON object containing the status of the upload and the name of the file uploaded.

###  - Performing Queries:
- Send a `GET` request to `/query` endpoint with a JSON object containing the query parameters.
Example using cURL:
```bash
curl -X GET -d "query=YourQueryHere" http://localhost:5000/query
```
