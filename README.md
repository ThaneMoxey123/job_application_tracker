# 📋 Job Application Tracker

A Python CLI tool to help you manage and track job applications during your job search. Built as a practical learning project while studying Python.

---

## 🚀 Features

- **Add** new job applications with company name, role, date and status
- **View** all applications in a clean, numbered list
- **Update** the status of any application as it progresses
- **Auto-save** to a CSV file so your data persists between sessions
- **Auto-load** your previous applications every time you open the program

---

## 📸 Preview

```
===== Job Application Tracker =====
1. Add new application
2. View all applications
3. Update application status
4. Quit

Choose an option: 2

----- All Applications -----

[1] Company:  Apex K.K.
    Role:     IT Specialist
    Date:     10/04/2026
    Status:   Interview

[2] Company:  Google Tokyo
    Role:     UX Designer
    Date:     08/04/2026
    Status:   Applied

Total applications: 2
```

---

## 🛠️ Built With

- Python 3
- `csv` — built-in Python library for reading and writing CSV files
- `os` — built-in Python library for file system operations

No external dependencies required.

---

## ▶️ How to Run

**1. Make sure Python 3 is installed:**
```bash
python --version
```

**2. Clone or download this repository:**
```bash
git clone https://github.com/ThaneMoxey123/job-application-tracker
```

**3. Navigate to the project folder:**
```bash
cd job-application-tracker
```

**4. Run the program:**
```bash
python job_tracker.py
```

---

## 📂 How It Works

When you add or update an application, the program automatically saves everything to a file called `applications.csv` in the same folder. Next time you run the program, it loads that file back in so none of your data is lost.

The CSV file can also be opened in Excel or Google Sheets if you want to view your applications in a spreadsheet.

---

## 📊 Application Statuses

| Status | Meaning |
|--------|---------|
| Applied | Application submitted |
| Interview | Interview scheduled or completed |
| Offer 🎉 | Job offer received |
| Rejected | Application unsuccessful |

---

## 🗺️ Planned Features

- Search applications by company name or status
- Statistics dashboard (total applied, interview rate, offer rate)
- Filter by date range
- Export summary report

---

## 👤 Author

**Jack Moxey**
- Portfolio: [jackmoxey.framer.website](https://jackmoxey.framer.website)
- LinkedIn: [linkedin.com/in/jack-moxey-8808b0308](https://linkedin.com/in/jack-moxey-8808b0308)
- GitHub: [ThaneMoxey123](https://github.com/ThaneMoxey123)

---

## 📝 Notes

This project was built during my first week of learning Python as a practical, real-world alternative to tutorial exercises. I'm currently based in Tokyo, Japan and actively job hunting — so this tool gets used daily!
