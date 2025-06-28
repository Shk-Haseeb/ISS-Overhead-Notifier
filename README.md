## 🛰 ISS Overhead Notifier

This little Python script lets you know when the **International Space Station** is flying above you **at night**

It checks two things:
- Is the **ISS near your location** (within ±5°)?
- Is it **currently dark** where you are?

If both are true, it sends you an **email alert** that says:  
**"LOOK UP!"**

---

### How It Works

- Uses real-time data from [ISS Location API](http://api.open-notify.org/iss-now.json) and [Sunrise-Sunset API](https://sunrise-sunset.org/api)
- Runs on a loop, checking every 60 seconds
- Sends you an email using Gmail when conditions are right

---

### Setup

1. Add your coordinates to `MY_LAT` and `MY_LONG`
2. Replace email fields with your Gmail and App Password
3. Run the script!

---

> Built as part of  **Advanced Programming** course (BSCS1002) at University of Helsinki to reinforce real-world Python skills like working with APIs, automation, and simple logic.
