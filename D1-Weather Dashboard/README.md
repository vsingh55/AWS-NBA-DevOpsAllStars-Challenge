# Weather-Dashboard

## 📜 Description
This project fetches weather data from the OpenWeather API for specified cities, processes the data, and stores it in an AWS S3 bucket. The stored data can be used for creating dashboards using tools like AWS QuickSight.

## 🛠 Features
- Fetch real-time weather data for multiple cities.
- Extract specific weather metrics (e.g., temperature, humidity, description).
- Save data locally in JSON format.
- Upload weather data to an S3 bucket.
- Includes error handling for API requests and AWS operations.

---

## 🚀 Prerequisites

1. **API Key**: Obtain an API key from [OpenWeather API](https://openweathermap.org/).
2. **AWS Credentials**:
   - Configure AWS credentials using the AWS CLI:
     ```bash
     aws configure
     ```
   - Ensure the IAM role/user has access to S3.
3. **Environment Variables**:
   Create a `.env` file in the project root with the following keys:
   ```env
   API_KEY=<your_openweather_api_key>
   S3_BUCKET_NAME=<your_s3_bucket_name>
   ```

4. **Python Requirements**:
   - Python 3.8+
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

---

## 📂 File Structure
```plaintext
├── weather_dashboard.py               # Main script for fetching and uploading data
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── weather-data/         # Directory for locally saved weather data
```

---

## ⚙️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vsingh55/AWS-NBA-DevOpsAllStars-Challenge-2025.git
   cd AWS-NBA-DevOpsAllStars-Challenge-2025/D1-Weather-Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in the `.env` file.

4. Run the script:
   ```bash
   python3 weather_dashboard.py
   ```

---

## 🌐 Usage

1. **Run the Script**
   - The script will:
     1. Check if the specified S3 bucket exists.
     2. Create the bucket if it doesn’t exist.
     3. Fetch weather data from the OpenWeather API.
     4. Save the data locally in the `weather-data/` directory.
     5. Upload the data to the S3 bucket.

2. **Sample Output**
   - Local file: `weather-data/London_weather.json`
   - S3 object: `s3://<bucket-name>/weather-data/London_weather.json`

---

## 🖥 Dashboard Creation

1. Use AWS QuickSight to create a dashboard from the S3 data.
2. Connect the S3 bucket to QuickSight as a data source.
3. Create visuals (e.g., bar charts, tables) for metrics like temperature, humidity, etc.

---

## 🐛 Error Handling
- Ensures bucket existence before uploading.
- Handles HTTP errors during API calls (e.g., 401 Unauthorized).
- Provides fallback for AWS operations.

---

## 📋 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🫱🏻‍🫲🏼 Let's Connect
For any inquiries or suggestions, please contact:
- **Vijay Kumar Singh**
- [Email](mailto:vijay@example.com)
- [GitHub Profile](https://github.com/username)
