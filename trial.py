class ex:
    l=0
    def change(self):
        ex.l = ex.l+1

m = ex()
print(ex.l)
m.change()
print(ex.l)