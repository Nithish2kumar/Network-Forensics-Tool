# 📡 PCAP Traffic Analyzer

A lightweight network traffic analysis tool built using Python and Scapy for analyzing `.pcap` files and detecting suspicious network activities.

---

## 🚀 Features

* 📂 Offline PCAP analysis
* 🌐 Source and destination IP tracking
* 📊 Protocol statistics
* ⚠️ Suspicious port detection
* 🧠 SYN packet analysis
* 📈 Traffic summary reporting

---

## 🛠️ Technologies Used

* Python 3
* Scapy
* Linux
* Networking Fundamentals

---

## 📂 Project Structure

```bash
PCAP-Traffic-Analyzer/
│
├── pcap.py
├── requirements.txt
├── README.md
└── sample.pcap
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nithish2kumar/PCAP-Traffic-Analyzer.git
```

Move into the project directory:

```bash
cd PCAP-Traffic-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Analyzer

```bash
python3 pcap.py
```

---

## 🔍 Detection Capabilities

### Suspicious Port Monitoring

Detects traffic targeting commonly attacked services:

| Port | Service |
| ---- | ------- |
| 22   | SSH     |
| 23   | Telnet  |
| 445  | SMB     |
| 3389 | RDP     |

---

### SYN Packet Analysis

Tracks TCP SYN packets to identify:

* Port scanning activity
* Reconnaissance behavior
* Possible SYN flood patterns

---

## 📊 Example Output

```bash
⚠️ Suspicious Port Access from: 192.168.1.7 to: 45.33.32.156 at port: 22

------ PCAP ANALYSIS REPORT ------

Total packets: 2599
Total SYN packets: 1199

Most Active Source IP: 192.168.1.7
Most Active Destination IP: 45.33.32.156
```

---

## 🧠 Concepts Learned

* Packet Parsing
* TCP/IP Analysis
* PCAP File Handling
* Protocol Statistics
* Traffic Investigation
* Threat Detection Basics
* Network Forensics

---

## 🔮 Future Improvements

* GUI Dashboard
* CSV Report Export
* GeoIP Mapping
* Port Scan Detection Logic
* DNS Analysis
* HTTP Traffic Extraction
* Malware Traffic Detection

---

## ⚠️ Disclaimer

This project is intended strictly for:

* Educational purposes
* Cybersecurity practice
* Lab environment analysis

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
