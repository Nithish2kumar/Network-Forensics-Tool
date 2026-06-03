# 📡 PCAP Traffic Analyzer

A lightweight Python-based network traffic analysis tool built using Scapy for offline PCAP inspection and suspicious activity detection.

---

## 🚀 Features

* 📂 Offline `.pcap` file analysis
* 🌐 Source and destination IP tracking
* 📊 Protocol statistics
* ⚠️ Suspicious port access detection
* 🧠 TCP SYN packet analysis
* 📈 Traffic summary reporting

---

## 🛠️ Technologies Used

* Python 3
* Scapy
* Linux
* TCP/IP Networking

---

## 📂 Project Structure

```bash
PCAP-Traffic-Analyzer/
│
├── pcap.py
├── README.md
├── requirements.txt
└── captured.pcap
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nithish2kumar/PCAP-Traffic-Analyzer.git
```

Move into project directory:

```bash
cd PCAP-Traffic-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Analyzer

```bash
python3 pcap.py
```

---

## 🔍 Detection Capabilities

### Suspicious Port Monitoring

The analyzer detects traffic targeting commonly attacked ports:

| Port | Service |
| ---- | ------- |
| 22   | SSH     |
| 23   | Telnet  |
| 445  | SMB     |
| 3389 | RDP     |

---

### SYN Packet Analysis

Tracks TCP SYN packets to identify:

* Reconnaissance activity
* Port scanning behavior
* Possible SYN flood attempts

---

## 📊 Example Output

```bash
⚠️ Suspicious port Access from: 192.168.1.7 to: 45.33.32.156 at port: 22

--------------------------------------------------

------ PCAP ANALYSIS REPORT ------

Total packets: 2599
Total SYN packets: 1199

------ Protocol Used ------

protocol 17: 27
protocol 6: 2484

------ Source IP Used ------

192.168.1.7: 1304
45.33.32.156: 1192
```

---

## 🧠 Concepts Used

* Packet Parsing
* TCP/IP Analysis
* PCAP File Processing
* Protocol Inspection
* Traffic Statistics
* Threat Detection Basics
* Network Forensics

---

## 🔮 Future Improvements

* Port Scan Detection Logic
* Duplicate Alert Reduction
* Protocol Name Mapping
* GUI Dashboard
* CSV Report Export
* GeoIP Tracking
* DNS Monitoring

---

## ⚠️ Disclaimer

This project is developed strictly for:

* Educational purposes
* Cybersecurity learning
* Network traffic analysis in lab environments

Do not use against unauthorized systems or networks.

---

## 👨‍💻 Author

**NK (Nithish Kumar)**

Cybersecurity and Blockchain Technology Student

---

## ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Contribute improvements
