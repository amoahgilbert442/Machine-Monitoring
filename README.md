# Machine Monitoring and Alert System  

## 📌 Project Overview  
The **Machine Monitoring and Alert System** is a **Python-based** tool that continuously checks the availability of machines within a network. It logs machine statuses, provides **real-time notifications** via **email and desktop alerts**, and includes a **Flask-based web dashboard** for visualizing machine uptime trends.  

## 🚀 Features  
- ✅ **Real-time Machine Monitoring** using ICMP (ping requests)  
- ✅ **Web Dashboard** for visualizing machine status trends  
- ✅ **Automated Email Alerts** when a machine goes offline  
- ✅ **Desktop Notifications** for quick issue awareness  
- ✅ **Logging System** to track machine status changes over time  

## 🛠️ Technologies Used  
- **Python** – Core programming language  
- **Flask** – Web framework for the dashboard  
- **Ping3** – Python library for ICMP ping requests  
- **Plyer** – Used for desktop notifications  
- **SMTP (Simple Mail Transfer Protocol)** – For sending email alerts  
- **HTML, CSS, JavaScript** – For the web dashboard UI  

## 📂 Project Structure  

Machine-Monitoring-System/ │── app.py # Flask web application │── monitor.py # Main monitoring script │── machines.txt # List of machines (IP addresses/hostnames) │── machine_logs.txt # Log file for status changes │── trend_data.json # Stores historical machine trends │── templates/ # HTML templates for web UI │── static/ # CSS, JavaScript files │── README.md # Project documentation │── requirements.txt # Python dependencies



## 🔧 Installation and Setup  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-username/machine-monitoring-system.git
cd machine-monitoring-system

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Configure Machine List
192.168.1.1
192.168.1.2
server1.domain.com


Step 4: Configure Email Alerts
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
RECIPIENT_EMAIL = "admin@example.com"


Step 5: Run the Monitoring Script
python monitor.py



Step 6: Start the Web Dashboard
python app.py
http://localhost:5000



📊 How It Works
The system reads machine IPs from machines.txt.
It sends ping requests to each machine.
Machine statuses are logged in machine_logs.txt.
If a machine goes offline, email & desktop notifications are triggered.
The Flask web dashboard displays machine statuses & trends.
📝 Future Enhancements
🔹 Add SNMP support for detailed system monitoring.
🔹 Improve dashboard UI with advanced filtering and real-time charts.
🔹 Integrate mobile push notifications for better alerting.
🔹 Automated machine recovery (restart offline machines if possible).
👨‍💻 Contributing
Contributions are welcome! To contribute:

Fork this repository.
Create a feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to your branch (git push origin feature-branch).
Open a Pull Request.



💬 Support
If you have any questions or issues, feel free to open an issue on GitHub or contact me at amoahgilbert442@gmail.com




---

This README is **fully detailed** and formatted for GitHub. Let me know if you want any changes before you upload it! 🚀
