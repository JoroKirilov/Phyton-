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
vip_list = []
normal_guest_list = []

for element in guest_code:
    if element[0].isdigit():
        vip_list.append(element)
for element in guest_code:
    if not element[0].isdigit():
        normal_guest_list.append(element)
print(len(vip_list) + len(normal_guest_list))
print('\n'.join(sorted(vip_list)))
print('\n'.join(sorted(normal_guest_list)))