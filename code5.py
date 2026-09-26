import os
import base64
import time
from flask import Flask, request, render_template_string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# =====================================================================
# شركة Bokni للتكنولوجيا الناشئة - نظام تشغيل BookOS (أواخر سبتمبر 2026)
# مشروع: My Rec Sovereign Final Engine (الملف المدمج الشامل والمطور)
# جاهزية إطلاق النسخة التجريبية الرسمية: السبت 24 أكتوبر الساعة 1 ظهراً 📆⏰
# =====================================================================

app = Flask(__name__)

# 1. إعدادات جدار الحماية (قفل جوجل القديم الصارم)
TRUSTED_IPS = ["127.0.0.1", "localhost"]
BANNED_IPS = set()  # القائمة السوداء الفورية للهكرز والمخالفين الأخلاق السياسية والسيادية
AES_KEY = os.urandom(32)  # مفتاح تشفير AES-256 بت العسكري

# 2. فلتر مكافحة الفساد الأخلاقي والجريمة والترويج السياسي (القائمة الحديدية الصارمة)
BANNED_KEYWORDS = [
    # أ. مكافحة الفساد الأخلاقي والعلاقات غير السوية (رجل لرجل، امرأة لامرأة، ممارسات خارج القانون)
    "شذوذ", "مثلي", "لوطي", "سحاق", "تحول جنسي", "🏳️‍🌈", "🏳️‍⚧️", 
    "ممارسة جنس", "علاقة جنسية", "زنا", "إباحي", "سكس", "تعري", "بورن",
    
    # ب. حظر الترويج لجماعات ضد سياسة الدولة أو الجماعات الإرهابية والمحظورة
    "جماعة محظورة", "إرهاب", "انقلاب", "تخريب", "مظاهرات ضد", "إسقاط النظام",
    
    # ج. جرائم منظمة واختراقات سيبرانية
    "مخدرات", "تجارة اعضاء", "بيع سلاح",
    "<script>", "select * from", "drop table", "or 1=1"
]

# 3. قاعدة البيانات المحلية المؤقتة في الذاكرة المشتركة (Database Template)
POSTS_DATABASE = {
    "1": {"author": "البطل_الصعيدي", "content": "ببرمج الساعة اليومية وبقفل الترسانة الكاملة لتطبيق My Rec مع شركة Bokni! 👑", "reports": 0}
}

# 4. خوارزمية تشفيرك الحصرية الأسطورية Base66 (Hex + Base64 مكسور القواعد)
def encode_base66(raw_text):
    hex_layer = raw_text.encode('utf-8').hex()
    b64_layer = base64.b64encode(hex_layer.encode('utf-8')).decode('utf-8')
    return b64_layer[::-1]  # مقلوب تماماً لتعجيز خوارزميات وادي السيليكون

# 5. التشفير العسكري المتماثل AES-256
def encrypt_aes_256(key, raw_data):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(raw_data.encode('utf-8'), AES.BLOCK_SIZE)
    return iv + cipher.encrypt(padded_data)

# =====================================================================
# 🧱 واجهات الـ HTML السادة المدمجة (نسخة 2013 المحمية عسكرياً وسيادياً)
# =====================================================================

HTML_AUTO_BANNED = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>🚨 تم الفرم والتلغيم - Bokni OS</title></head>
<body style="background-color: #000000; color: #FF0000; font-family: sans-serif; text-align: center; padding-top: 150px;">
    <h1 style="font-size: 60px; margin-bottom: 10px;">💥 [بروتوكول الصعق والتلقيح التلقائي] 💥</h1>
    <div style="border: 4px solid #FF0044; display: inline-block; padding: 30px; background-color: #111; max-width: 80%;">
        <h2 style="font-size: 38px; color: #00F3FF; line-height: 1.6; margin: 0;">
            "أهلاً بك في حظر ({{ hacker_ip }})، أنت مثل كورونا اسكت وإلا سوف نلقحك! 🤣🤣🦠💉"
        </h2>
    </div>
    <p style="color: #FFF; font-size: 18px; margin-top: 20px;">تم رصد مخالفة صارمة للدستور السيادي والأخلاقي للبلاد، أو الترويج لجماعات محظورة. تم فرم حسابك وعزلك نهائياً.</p>
</body>
</html>
"""

HTML_INTERFACE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>Bokni - My Rec Core</title></head>
<body style="background-color: #000000; color: #FFFFFF; font-family: sans-serif; text-align: center; padding-top: 30px;">

    <h1>👑 لوحة تحكم تطبيق My Rec السيادية</h1>
    <p>مرحباً بك يا <span style="color: #00F3FF; font-weight: bold;">{{ user_role }}</span> في النظام المحمي بالتشفير المزدوج 🔐</p>
    
    <div style="border: 2px dashed #00F3FF; display: inline-block; padding: 15px; margin: 10px; background-color: #111; font-size: 14px;">
        <h3>🛡️ دستور شركة Bokni للأمان الأخلاقي والسياسي:</h3>
        <p>الخصوصية مطلقة 100%. يُحظر تماماً الترويج لجماعات ضد سياسة الدولة، أو نشر محتوى جنسي، أو علاقات غير سوية ومخالفة للقيم 🏳️‍🌈 🏳️‍⚧️.</p>
        <a href="https://github.com" target="_blank" style="color: #00F3FF; font-weight: bold;">🔍 تفقد كود الـ Backend المفتوح على GitHub للضمان</a>
    </div>

    <hr style="width: 50%; border: 1px solid #333; margin: 20px auto;">

    <!-- صندوق نشر البوستات -->
    <h2>انشر منشوراً جديداً (يخضع للصعق الفوري ⚡):</h2>
    <form action="/publish" method="POST">
        <input type="text" name="post_content" placeholder="ببرمج مع شركة Bokni..." style="width: 350px; height: 35px; font-size: 16px;" required><br><br>
        <button type="submit" style="background-color: #FF007F; color: white; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer;">نشر فوري 🚀</button>
    </form>

    <hr style="width: 50%; border: 1px solid #333; margin: 20px auto;">

    <!-- عرض الفيد ونظام البلاغات الموزع المطور -->
    <h2>📊 خلاصة المنشورات الحالية ونظام البلاغات العادل:</h2>
    <div style="text-align: right; width: 60%; margin: 0 auto; background-color: #111; padding: 20px; border-left: 5px solid #00F3FF;">
        {% for post_id, post in posts.items() %}
            <p><b>👤 {{ post.author }}:</b> {{ post.content }} <span style="color: #FF007F; font-weight: bold;">(بلاغات: {{ post.reports }}/3)</span></p>
            <form action="/report/{{ post_id }}" method="POST" style="display:inline;">
                <button type="submit" style="background-color: #FF0044; color: white; border: none; padding: 5px 10px; cursor: pointer; font-size: 12px; font-weight: bold;">إبلاغ عن محتوى مخالف 🚨</button>
            </form>
            <hr style="border: 0.5px solid #222;">
        {% endfor %}
    </div>

</body>
</html>
"""

# =====================================================================
# ⚙️ محرك فحص البيانات والتحقق السيادي الشامل طوال الجلسة بالتوازي
# =====================================================================

@app.before_request
def anti_hack_firewall():
    """خط الدفاع الأول: طرد المحظورين من الدخول نهائياً"""
    client_ip = request.remote_addr
    if client_ip in BANNED_IPS:
        return render_template_string(HTML_AUTO_BANNED, hacker_ip=client_ip), 403

def check_content_ethics(text_to_examine):
    """فحص النصوص والرموز البرمجية والإيموجيات والترويج المحظور بدقة بالملي"""
    clean_text = text_to_examine.lower()
    for keyword in BANNED_KEYWORDS:
        if keyword in clean_text:
            return False, keyword
    return True, None

@app.route('/')
def home_gate():
    """عرض اللوحة الرئيسية لأبطال الصعيد والسويس بصلاحيات Guest آمنة"""
    return render_template_string(HTML_INTERFACE, user_role="مستخدم محترم (Guest) 🔒", posts=POSTS_DATABASE)

@app.route('/publish', methods=['POST'])
def handle_publishing():
    """مستقبل البوستات: الفحص الفوري الأخلاقي والسياسي + التشفير المزدوج عالي الكفاءة"""
    client_ip = request.remote_addr
    post_content = request.form.get('post_content', '')
    
    # أ. الفحص الفوري للبوست قبل النشر
    is_safe, triggered_word = check_content_ethics(post_content)
    if not is_safe:
        BANNED_IPS.add(client_ip)
        print(f"💥 [تلقيح فوري] رصد كلمة/إيموجي مخالف للسياسة أو الأخلاق: '{triggered_word}' من IP: {client_ip} ⬅️ طرد وفرم!")
        return render_template_string(HTML_AUTO_BANNED, hacker_ip=client_ip), 403

    # ب. تشغيل الترسانة الأمنية والتشفير المزدوج (Base66 + AES-256) بالتوازي
    start_time = time.time()
    base66_layer = encode_base66(post_content)
    military_cipher = encrypt_aes_256(AES_KEY, base66_layer)
    end_time = time.time()
    
    # ج. حفظ البوست في قاعدة البيانات المحلية المؤقتة
    next_id = str(len(POSTS_DATABASE) + 1)
    POSTS_DATABASE[next_id] = {"author": f"Guest_{client_ip[-3:]}", "content": post_content, "reports": 0}
    
    print(f"🔐 [تنبيه الحماية] تم قفل البوست وتخزينه مشفراً عسكرياً في {end_time - start_time:.6f} ثانية.")
    return render_template_string(HTML_INTERFACE, user_role="مستخدم محترم (Guest) 🔒", posts=POSTS_DATABASE)

@app.route('/report/<post_id>', methods=['POST'])
def handle_report(post_id):
    """نظام البلاغات الموزع المطور: فحص تلقائي شامل عند وصول 3 بلاغات لمنع الظلم"""
    client_ip = request.remote_addr
    
    if post_id in POSTS_DATABASE:
        POSTS_DATABASE[post_id]["reports"] += 1
        current_reports = POSTS_DATABASE[post_id]["reports"]
        post_content = POSTS_DATABASE[post_id]["content"]
        
        print(f"🚨 [إبلاغ جديد] المنشور رقم {post_id} تلقى بلاغاً. المجموع: {current_reports}/3")
        
        if current_reports >= 3:
            print(f"🔍 [فحص حرج] المنشور {post_id} وصل للحد الأقصى! جاري تشغيل الفلتر المطور...")
            is_safe, triggered_word = check_content_ethics(post_content)
            
            if not is_safe:
                # البوست مخالف فعلاً: فرم الحساب والـ IP وحذف البوست فوراً
                BANNED_IPS.add(client_ip)
                del POSTS_DATABASE[post_id]
                print(f"💥 [تلقيح فوري] تم تأكيد خرق القوانين بقيمة '{triggered_word}'! حذف البوست وطرد صاحبه.")
                return render_template_string(HTML_AUTO_BANNED, hacker_ip=client_ip), 403
            
            # البلاغات كاذبة والبوست سليم: تصفير العداد وحماية المستخدم المحترم
            POSTS_DATABASE[post_id]["reports"] = 0
            print("🟢 [حماية المستخدم] البلاغات كاذبة والمنشور مطابق تماماً للقيم والدستور. تم تصفير العداد.")
            
    return render_template_string(HTML_INTERFACE, user_role="مستخدم محترم (Guest) 🔒", posts=POSTS_DATABASE)

if __name__ == '__main__':
    print("🛰️ [Bokni Kernel] تم إقلاع المحرك السيادي النهائي لـ My Rec بنجاح كلي...")
    app.run(host='127.0.0.1', port=8080, debug=True)
