checks = {
  "alpha"     : lambda uid: re.match(r".*[A-Z].*[A-Z].*", uid),
  "num"       : lambda uid: re.match(r".*[0-9].*[0-9].*[0-9].*", uid),
  "alpha_num" : lambda uid: re.match(r"[A-Za-z0-9]{10}", uid),
  "repeat"    : lambda uid: not re.match(r".*(.).*\1.*", uid)
}

def main():
  for _ in range(int(input())):
    uid = input()
    print("Valid" if all(checks[check](uid) for check in checks.keys()) else "Invalid")

if __name__ == "__main__":
  main()

  