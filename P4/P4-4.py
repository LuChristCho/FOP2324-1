class DAS:
    def __init__(self):
        self.P = {}
        self.V = {}

    def e_c(self, c):
        t = c.split()
        if len(t) == 0:
            print("invalid command")
            return
        if t[0] == "add" and t[1] == "patient":
            self.a_p(t[2:])
        elif t[0] == "display" and t[1] == "patient":
            self.d_p(t[2:])
        elif t[0] == "add" and t[1] == "visit":
            self.a_v(t[2:])
        elif t[0] == "delete" and t[1] == "patient":
            self.delete_p(t[2:])
        elif t[0] == "display" and t[1] == "visit" and t[2] == "list":
            self.d_v_l()
        elif t[0] == "exit":
            exit()
        else:
            print("invalid command")

    def a_p(self, a):
        p_i, n, f_n, a_g, h, w = map(str, a)
        if int(p_i) in self.P:
            print("error: this ID already exists")
        elif int(a_g) < 0:
            print("error: invalid age")
        elif int(h) < 0:
            print("error: invalid height")
        elif int(w) < 0:
            print("error: invalid weight")
        else:
            self.P[int(p_i)] = {
                "n": n,
                "f_n": f_n,
                "a": a_g,
                "h": h,
                "w": w
            }
            print("patient added successfully")

    def d_p(self, a):
        p_i = int(a[0])
        if p_i not in self.P:
            print("error: invalid ID")
        else:
            patient_info = self.P[p_i]
            print(f"patient name: {patient_info['n']}")
            print(f"patient family name: {patient_info['f_n']}")
            print(f"patient age: {patient_info['a']}")
            print(f"patient height: {patient_info['h']}")
            print(f"patient weight: {patient_info['w']}")

    def delete_p(self, a):
        p_i = int(a[0])
        if p_i not in self.P:
            print("error: invalid id")
        else:
            deleted_patient_info = self.P.pop(p_i)
            for t, v_i in list(self.V.items()):
                if v_i.startswith(f"({deleted_patient_info['n']}) ({deleted_patient_info['f_n']})"):
                    del self.V[t]
            print("patient deleted successfully!")

    def a_v(self, a):
        p_i, b_t = map(int, a)
        if p_i not in self.P:
            print("error: invalid id")
        elif b_t < 9 or b_t > 18:
            print("error: invalid time")
        elif b_t in self.V:
            print("error: busy time")
        else:
            self.V[b_t] = f"({self.P[p_i]['n']}) ({self.P[p_i]['f_n']})"
            print("visit added successfully!")

    def d_v_l(self):
        print("SCHEDULE:")
        for t, v_i in self.V.items():
            v_i = v_i.replace('(', '').replace(')', '')
            print(f"{t}:00 {v_i}")


if __name__ == "__main__":
    s = DAS()
    while True:
        try:
            c = input()
            s.e_c(c)
        except EOFError:
            break
