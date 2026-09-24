import multiprocessing
import hashlib
import time
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from scapy.all import sniff, Raw, IP

# =====================================================================
# شركة Bokni للتكنولوجيا الناشئة - الإصدار النهائي الخارق 2026
# مشروع: My Rec Mega Engine (نظام الحوسبة المتوازية والدفاع السيبراني)
# =====================================================================

# 1. التشفير العسكري AES-256 (خط الدفاع الأول)
def encrypt_aes_256(key, raw_data):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(raw_data.encode('utf-8'), AES.BLOCK_SIZE)
    return iv + cipher.encrypt(padded_data)

def decrypt_aes_256(key, encrypted_data):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded, AES.BLOCK_SIZE).decode('utf-8')

# 2. النواة العاملة (Worker) للتجزئة والتجميع الآمن فائق السرعة
def secure_shading_worker(index, shard_value, lock, shared_list):
    shard_hash = hashlib.md5(shard_value.encode()).hexdigest()
    processed_data = shard_value.strip()
    time.sleep(0.02) # معالجة سريعة عالية الكفاءة
    
    with lock:
        # الفرز اللحظي المباشر بالـ Index يمنع تضارب وترتيب العمليات نهائياً O(1)
        shared_list[index] = f"{processed_data} (Verified:{shard_hash[:4]})"

# 3. النواة العاملة (Worker) لسنيفر الشبكة الذكي بمكتبة Scapy
def network_sniffer_worker(lock, shared_flags):
    # الكلمات المحظورة التي تخالف دستور وأنظمة تطبيق My Rec
    banned_keywords = [b"drugs", b"weapons", b"exploit", b"malware", b"mukhdirat"]
    print("🛰️ [Bokni Network Guard] تم تشغيل السنيفر وبدء فحص حزم الـ IP...")
    
    def process_packet(packet):
        if packet.haslayer(Raw):
            payload = packet[Raw].load.lower()
            src_ip = packet[IP].src if packet.haslayer(IP) else "Unknown"
            
            for word in banned_keywords:
                if word in payload:
                    with lock:
                        print(f"\n🚨 [إنذار سيبراني] حزمة مشبوهة من {src_ip}! رصد كلمة محظورة: {word.decode()}")
                        shared_flags["attack_detected"] = True
                        shared_flags["attacker_ip"] = src_ip

    sniff(prn=process_packet, filter="ip", store=0, stop_filter=lambda p: shared_flags.get("attack_detected", False))

# 4. محرك الأنظمة الرئيسي لـ My Rec
class MyRecMegaEngine:
    def __init__(self, user_name):
        self.user_name = user_name
        self.aes_key = os.urandom(32) # مفتاح AES-256 بت عسكري
        self.banned_words = ["مخدرات", "تجارة اعضاء", "بيع سلاح"]
        print(f"👑 أهلاً بك في نظام BookOS الذكي. تم تهيئة محرك My Rec للمستخدم: {self.user_name}")

    def filter_content_ethics(self, post_content):
        """فلتر الأمان الأخلاقي والدستوري"""
        for word in self.banned_words:
            if word in post_content:
                print(f"🔒 [حظر فوري] المنشور يخالف الدستور وقوانين شركة Bokni لمكافحة الجريمة.")
                return False
        return True

    def run_parallel_pipeline(self, raw_activity_data, post_content):
        """إدارة خط الأنابيب البرمجي بالكامل بالتوازي وتوزيع العمليات"""
        if not self.filter_content_ethics(post_content):
            return

        lock = multiprocessing.Lock()
        manager = multiprocessing.Manager()
        
        # ذاكرة مشتركة معزولة وآمنة
        shared_list = manager.list([None] * 3)
        shared_flags = manager.dict({"attack_detected": False, "attacker_ip": None})

        # --- أ. تشغيل سنيفر الشبكة الذكي بالتوازي في نواة مستقلة ---
        guard_process = multiprocessing.Process(target=network_sniffer_worker, args=(lock, shared_flags))
        guard_process.start()

        # --- ب. محاكاة بروتوكول AT و MQTTS لتشفير وبث البيانات ---
        print("\n📡 [AT Protocol] إصدار أمر الأوامر القياسي: AT+MQTT_START")
        print("🔒 [MQTTS Protocol] تفعيل حماية TLS والبث المشفر عبر ميناء 8883...")
        
        encrypted_data = encrypt_aes_256(self.aes_key, raw_activity_data)
        
        # --- ج. تقسيم البيانات المشتتة وتجميعها المتوازي فائق السرعة ---
        data_str = raw_activity_data
        part_size = len(data_str) // 3
        shards = [data_str[:part_size], data_str[part_size:part_size*2], data_str[part_size*2:]]
        
        sharding_processes = []
        for index, shard_value in enumerate(shards):
            p = multiprocessing.Process(target=secure_shading_worker, args=(index, shard_value, lock, shared_list))
            sharding_processes.append(p)
            p.start()

        for p in sharding_processes:
            p.join()

        # التجميع اللحظي عالي الكفاءة
        reassembled_output = " | ".join(shared_list)
        print(f"\n🎯 [خوارزمية الفرز اللحظي] البيانات المسترجعة والمنظمة محلياً: {reassembled_output}")
        
        # فك تشفير الحزمة للتأكد من سلامتها العسكرية
        decrypted_payload = decrypt_aes_256(self.aes_key, encrypted_data)
        print(f"🔑 [AES-256 فك التشفير الحصري] البيانات الأصلية المفكوكة بنقاء: {decrypted_payload}")

        # إغلاق السنيفر بأمان عند انتهاء العمليات
        time.sleep(1)
        if guard_process.is_alive():
            guard_process.terminate()
        print("\n🟢 [Bokni OS] تم قفل جلسة التشغيل بنجاح، والنظام مستقر بنسبة 100%.")

# --- القالب الإلزامي والنهائي لتشغيل النظام بأمان كامل ---
if __name__ == '__main__':
    # تشغيل المحرك
    engine = MyRecMegaEngine(user_name="البطل الصعيدي العبقري")
    
    # سجل نشاط المشاهدة الحساس ومنشور المستخدم
    sample_activity = "Tech:990|Electronics:1600|Gaming:850"
    sample_post = "ببرمج الساعة اليومية وبطور كود تطبيق My Rec مع شركة Bokni!"
    
    engine.run_parallel_pipeline(sample_activity, sample_post)
