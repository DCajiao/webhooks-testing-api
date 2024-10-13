# 🚀 Webhook Tester API 🌐

Welcome to **Webhook Tester API**! 🎉 This project is a simple API for testing your webhooks, logging the requests, and handling them easily. Perfect for ensuring everything is working smoothly before going live! 🛠️

## 💡 What does this API do?
This API has 3 endpoints:
1. **/post** – Receives `POST` requests and saves the data into a log file.
2. **/get** – Returns all the logged data.
3. **/delete** – Clears all logs, like nothing ever happened! ✨

## 📂 File Structure
```
├── logs/                # Folder to store the logs
│   └── data.txt         # File where the data is logged
├── main.py              # API code
├── Dockerfile           # Docker file to run the API
├── requirements.txt     # Project dependencies
└── README.md            # This awesome file
```

## 🚀 How to use the API

### 1. Clone the repository:
First, clone the repo to have everything ready on your machine.
```bash
git clone https://github.com/your-repo/webhook-tester-api.git
cd webhook-tester-api
```

### 2. Install dependencies:
Make sure you have Flask installed. If not, you can install it with:
```bash
pip install -r requirements.txt
```

### 3. Run the API:
Start the Flask server with the following command:
```bash
python main.py
```
Now your API should be running on `http://localhost:5000` 🎉

### 4. Use Docker 🐳 (the cool way to run your API!)
If you prefer using Docker (and of course you do), follow these steps:

#### 1. Create the Docker image:
```bash
docker build -t webhook-tester-api .
```

#### 2. Run the API in a container:
```bash
docker run -d -p 5000:5000 webhook-tester-api
```

And voilà! 🎉 Your API is ready at `http://localhost:5000`.

### 5. Test the endpoints:
#### **Send data to `/post`** 📨
Make a `POST` request to `/post` with a JSON to log data.
```bash
curl -X POST http://localhost:5000/post -H "Content-Type: application/json" -d '{"message": "Hello, webhook!"}'
```

#### **Retrieve logs at `/get`** 📜
Access all logged data with a `GET` request.
```bash
curl http://localhost:5000/get
```

#### **Clear logs with `/delete`** 🗑️
Clear all logs with a `DELETE` request.
```bash
curl -X DELETE http://localhost:5000/delete
```

## 📝 Notes:
- All data is stored in the `logs/data.txt` file in plain text format.
- Logs are saved with a timestamp 🕒, so you'll always know when a request was received.
- Remember not to expose this API in production without security! 🚨

## 🤖 What’s next?
- Implement basic authentication 🔒 so only you can access the logs.
- Integrate a database for more robust data storage.
- Or whatever you can think of! 🎨

---

Enjoy testing your webhooks with or without Docker! 🐳🌈