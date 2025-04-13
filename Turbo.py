import os, json, time, base64, random, requests, threading
#+------------------------------------------------------+
#| Author : L7N                                       |
#| Telegram : t.me/PyL7N                     |
#| Github : https://github.com/is-L7N  |
#+------------------------------------------------------+

accounts = {
    "account1": {"session": None, "info": None},
    "account2": {"session": None, "info": None}
}

class Instagram:
    def user_agent(self):
        rnd = str(random.randint(150, 999))
        agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
        return agent

    def Status(self) -> bool:
        url = "https://i.instagram.com/api/v1/users/check_username/"
        payload = {
            'signed_body': (
                "SIGNATURE.{\"username\":\"l7n\",\"_uuid\":\"6f8e51dd-6663-4d93-a5a2-9d9e23126837\"}"
            )
        }
        headers = {
            'User-Agent': self.user_agent()
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            return response.status_code == 200
        except Exception:
            return False

    def get_info(self, session):
        if "Bearer" in session:
            try:
                decoded = base64.urlsafe_b64decode(session.split('IGT:2:')[1]).decode("utf-8")
                session = json.loads(decoded)['sessionid']
            except Exception:
                return {"status": False, "message": "Token Bearer is bad!"}

        cookies = {'sessionid': str(session)}
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'user-agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0'
            ),
            'x-ig-app-id': '936619743392459',
        }

        try:
            response = requests.get(
                'https://www.instagram.com/api/v1/accounts/edit/web_form_data/',
                cookies=cookies,
                headers=headers
            ).json().get('form_data', {})
            return response
        except Exception:
            return {"status": False, "message": "erorr get info!"}


class L7N:
    def add_account(self, account_name):
        session = input(f"Enter session for {account_name}: ").strip()
        if not session:
            return {"status": False, "message": "Token or Sessionid is bad!"}

        accounts[account_name]["session"] = session
        print(accounts)
        ig = Instagram()
        response = ig.get_info(session)
        if not response:
            return {"status": False, "message": "bad info!"}

        accounts[account_name]["info"] = {
            'username': response.get('username', ''),
            'email': response.get('email', ''),
            'phone_number': response.get('phone_number', ''),
            'first_name': response.get('first_name', ''),
            'biography': response.get('biography', '')
        }
        return True

    def add(self):
        for account in accounts:
            if not self.add_account(account):
                return {"status": False, "message": "erorr add!"}
        print("All accounts added!")
        trans = Trans()
        trans.main()


class Trans:
    def __init__(self):
        self.rnd = "qwertyuiopasdfghjklzxcvbnm1234567890"
        self.old_username = accounts["account1"]["info"]["username"]
        self.nUserName = ''.join(random.choice(self.rnd) for _ in range(15))
        self.session1 = accounts["account1"]["session"]
        self.session2 = accounts["account2"]["session"]
        self.info1 = accounts["account1"]["info"]
        self.info2 = accounts["account2"]["info"]
        
    def change_username(self, session, info, new_username):
        url = "https://i.instagram.com/api/v1/accounts/edit_profile/"
        biography = "done trans username\nOwner ~> L7N 🐉"
        payload_data = {
            "primary_profile_link_type": "0",
            "external_url": "",
            "phone_number": info.get('phone_number', ''),
            "username": new_username,
            "show_fb_link_on_profile": "false",
            "first_name": info.get('first_name', ''),
            "_uid": "71659152784",
            "device_id": "android-ec0d029217328701",
            "biography": biography,
            "_uuid": "6f8e51dd-6663-4d93-a5a2-9d9e23126837",
            "email": info.get('email', '')
        }
        payload = {
            'signed_body': f"SIGNATURE.{json.dumps(payload_data, separators=(',', ':'))}"
        }
        headers = {
            'User-Agent': Instagram().user_agent(),
            'authorization': str(session),
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            print(response.text) 
            return response.json()
        except Exception:
            return {"status": False, "message": "bad Trans UserName!"}

    def main(self):
        def change1():
            print(f"[*] Changing account1 username from {self.old_username} to '{self.nUserName}'")
            res1 = self.change_username(self.session1, self.info1, self.nUserName)
            if res1['status'] == "ok":
                print("[+] account1 change ")

        def change2():
            print(f"[*] Changing account2 username to '{self.old_username}'")
            res2 = self.change_username(self.session2, self.info2, self.old_username)
            if res2['status'] == "ok":
                print("[+] account2 change ")

        t1 = threading.Thread(target=change1)
        t2 = threading.Thread(target=change2)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

class Fun:
    @staticmethod
    def trans_sessionid(ses):
        try:
            inp = ses.strip()
            if inp.startswith("Bearer IGT:2:"):
                b64 = inp.split("Bearer IGT:2:")[1]
                data = json.loads(base64.b64decode(b64).decode())
                return "[+] SessionID:\n" + data["sessionid"]
            else:
                uid = inp.split(":")[0]
                payload = json.dumps({"ds_user_id": uid, "sessionid": inp})
                token = base64.b64encode(payload.encode()).decode()
                return "[+] Bearer Token:\nBearer IGT:2:" + token
        except Exception:
            return {"status": False, "message": "Fuck!"}

if __name__ == "__main__":
    info = [
    "Author : L7N 🇮🇶",
    "Telegram : t.me/PyL7N",
    "Github : https://github.com/is-L7N"
]

    width = max(len(line) for line in info) + 4
    border = "+" + "-" * (width - 2) + "+"
    
    print(border)
    for line in info:
        print("| " + line.ljust(width - 3) + " |") 
    print(border)
    print("\n[1] Trans Sessionid To Token (Bearer) or opposite !\n[2] Trans UserNames !\n[3] Check if you are banned or not !\n")
    cho = input("[*] Choose : ")
    if cho == 1 or cho == "1":
        inp = input("[×] Your Sessiond or Token : ")
        print(Fun.trans_sessionid(inp))
    elif cho == 2 or cho == "2":
        os.system('clear')
        L7N().add()
    else:
        print(Instagram().Status())

# This Code By L7N 🇮🇶