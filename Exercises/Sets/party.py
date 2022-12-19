n = int(input())
guest_code = set()

for _ in range(n):
    code = input()
    guest_code.add(code)

while True:
    living_codes = input()
    if living_codes == "END":
        break
    guest_code.discard(living_codes)

print(len(guest_code))
print("\n".join(sorted(guest_code)))
