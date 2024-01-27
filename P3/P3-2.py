n = int(input())
domains = {}

for _ in range(n):
    email = input().strip()
    if '@' in email and '.' in email.split('@')[-1]:
        domain = email.split('@')[-1]
        domains[domain] = 1

for domain in sorted(domains.keys()):
    print(domain)